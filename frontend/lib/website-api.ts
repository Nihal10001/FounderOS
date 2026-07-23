const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export type WebsiteFiles = Record<string, string>;

export async function generateWebsite(idea: string): Promise<WebsiteFiles> {
  const res = await fetch(`${API_BASE}/api/v1/website/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idea }),
  });
  if (!res.ok) throw new Error(await res.text());
  const data = await res.json();
  return data.files as WebsiteFiles;
}

export async function deployToVercel(
  files: WebsiteFiles,
  repoName: string,
  githubToken: string
): Promise<{ repo_url: string; vercel_deploy_url: string }> {
  const res = await fetch(`${API_BASE}/api/v1/website/deploy`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ files, repo_name: repoName, github_token: githubToken }),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
