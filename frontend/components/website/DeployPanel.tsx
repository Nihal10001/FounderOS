"use client";

import { useState } from "react";
import { deployToVercel, WebsiteFiles } from "@/lib/website-api";

export function DeployPanel({ files }: { files: WebsiteFiles }) {
  const [repoName, setRepoName] = useState("my-idea-site");
  const [token, setToken] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<{ repo_url: string; vercel_deploy_url: string } | null>(
    null
  );
  const [error, setError] = useState<string | null>(null);

  async function handleDeploy() {
    setError(null);
    setLoading(true);
    try {
      const res = await deployToVercel(files, repoName, token);
      setResult(res);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Deploy failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-md border border-outline-variant bg-surface-container-low p-4">
      <h3 className="mb-2 text-sm font-semibold text-on-surface">Deploy this site</h3>
      <p className="mb-3 text-xs text-on-surface-variant">
        Pushes the generated code to a new GitHub repo under your account, then hands off to
        Vercel&apos;s own import page — Vercel login happens on their site, not here. Your token
        is used once for this request and never stored.{" "}
        <a
          href="https://github.com/settings/tokens/new?scopes=repo&description=ai-org-chart-deploy"
          target="_blank"
          rel="noreferrer"
          className="underline text-primary"
        >
          Create a token
        </a>{" "}
        with the <code>repo</code> scope.
      </p>

      <div className="flex flex-col gap-2 sm:flex-row">
        <input
          value={repoName}
          onChange={(e) => setRepoName(e.target.value)}
          placeholder="repo name"
          className="rounded-md border border-outline-variant bg-surface-container px-3 py-2 text-sm text-on-surface focus:border-primary focus:outline-none"
        />
        <input
          value={token}
          onChange={(e) => setToken(e.target.value)}
          type="password"
          placeholder="GitHub personal access token"
          className="flex-1 rounded-md border border-outline-variant bg-surface-container px-3 py-2 text-sm text-on-surface focus:border-primary focus:outline-none"
        />
        <button
          onClick={handleDeploy}
          disabled={loading || !token || !repoName}
          className="rounded-md bg-tertiary-container px-4 py-2 text-sm font-medium text-on-surface disabled:opacity-40"
        >
          {loading ? "Pushing..." : "Push & Deploy"}
        </button>
      </div>

      {error && <p className="mt-2 text-xs text-error">{error}</p>}

      {result && (
        <div className="mt-3 flex flex-col gap-1 text-sm">
          <a href={result.repo_url} target="_blank" rel="noreferrer" className="underline text-primary">
            View repo on GitHub
          </a>
          <a
            href={result.vercel_deploy_url}
            target="_blank"
            rel="noreferrer"
            className="underline text-tertiary"
          >
            Finish deploying on Vercel →
          </a>
        </div>
      )}
    </div>
  );
}
