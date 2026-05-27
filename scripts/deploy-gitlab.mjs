/**
 * Create/update GitLab project and push lillybabe-partner-gitlab for Pages.
 * Usage: set GITLAB_TOKEN=glpat-xxx && node scripts/deploy-gitlab.mjs
 */
import { execSync } from "node:child_process";
import fs from "node:fs";
import https from "node:https";
import path from "node:path";
import { fileURLToPath } from "node:url";

const TOKEN = process.env.GITLAB_TOKEN;
const NAMESPACE = process.env.GITLAB_NAMESPACE || "hellomahicom";
const PROJECT = "lillybabe-partner-gitlab";
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "gitlab");

if (!TOKEN) {
  console.error("Set GITLAB_TOKEN (api + write_repository scopes).");
  process.exit(1);
}

function api(method, apiPath, body) {
  return new Promise((resolve, reject) => {
    const data = body ? JSON.stringify(body) : null;
    const req = https.request(
      {
        hostname: "gitlab.com",
        path: `/api/v4${apiPath}`,
        method,
        headers: {
          "PRIVATE-TOKEN": TOKEN,
          ...(data && {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(data),
          }),
        },
      },
      (res) => {
        let d = "";
        res.on("data", (c) => (d += c));
        res.on("end", () => {
          let parsed = d;
          try {
            parsed = d ? JSON.parse(d) : {};
          } catch {
            /* keep raw */
          }
          resolve({ status: res.statusCode, data: parsed });
        });
      }
    );
    req.on("error", reject);
    if (data) req.write(data);
    req.end();
  });
}

function walk(dir, base = "") {
  const out = [];
  for (const name of fs.readdirSync(dir)) {
    if (name === ".git" || name === ".netlify" || name === ".vercel" || name === ".github") continue;
    const full = path.join(dir, name);
    const rel = base ? `${base}/${name}` : name;
    if (fs.statSync(full).isDirectory()) out.push(...walk(full, rel));
    else out.push({ rel, full });
  }
  return out;
}

async function ensureProject() {
  const enc = encodeURIComponent(`${NAMESPACE}/${PROJECT}`);
  let res = await api("GET", `/projects/${enc}`);
  if (res.status === 200) return res.data;

  res = await api("POST", "/projects", {
    name: PROJECT,
    path: PROJECT,
    namespace_id: null,
    visibility: "public",
    initialize_with_readme: false,
  });
  if (res.status === 201) return res.data;

  throw new Error(`Create project failed: ${res.status} ${JSON.stringify(res.data)}`);
}

async function upsertFile(projectId, filePath, content, branch, message) {
  const encoded = encodeURIComponent(filePath);
  const payload = {
    branch,
    content: Buffer.from(content).toString("base64"),
    encoding: "base64",
    commit_message: message,
  };
  let res = await api("PUT", `/projects/${projectId}/repository/files/${encoded}`, payload);
  if (res.status === 200) return;
  res = await api("POST", `/projects/${projectId}/repository/files/${encoded}`, payload);
  if (res.status === 201) return;
  throw new Error(`${filePath}: ${res.status} ${JSON.stringify(res.data)}`);
}

async function main() {
  const project = await ensureProject();
  const branch = project.default_branch || "main";
  console.log("Project:", project.web_url);

  const files = walk(ROOT);
  for (const { rel, full } of files) {
    const content = fs.readFileSync(full);
    const isText = /\.(html|css|js|txt|xml|yml|md)$/i.test(rel);
    await upsertFile(
      project.id,
      rel.replace(/\\/g, "/"),
      isText ? content.toString("utf8") : content,
      branch,
      `Deploy ${rel}`
    );
    console.log("Uploaded:", rel);
  }

  console.log("\nGitLab Pages URL (after pipeline):");
  console.log(`https://${NAMESPACE}.gitlab.io/${PROJECT}/`);
}

main().catch((e) => {
  console.error(e.message || e);
  process.exit(1);
});
