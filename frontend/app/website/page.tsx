"use client";

import { useState } from "react";
import Link from "next/link";
import { generateWebsite, WebsiteFiles } from "@/lib/website-api";
import { IdeaForm } from "@/components/website/IdeaForm";
import { WebsitePreview } from "@/components/website/WebsitePreview";
import { DeployPanel } from "@/components/website/DeployPanel";

export default function WebsiteBuilderPage() {
  const [files, setFiles] = useState<WebsiteFiles | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleGenerate(idea: string) {
    setError(null);
    setLoading(true);
    setFiles(null);
    try {
      const result = await generateWebsite(idea);
      setFiles(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Generation failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="mx-auto flex min-h-screen max-w-5xl flex-col gap-6 px-6 py-10">
      <header>
        <Link href="/" className="text-xs text-outline underline">
          ← Back to virtual team
        </Link>
        <h1 className="mt-2 text-2xl font-semibold text-on-surface">FounderOS — Idea → Website</h1>
        <p className="mt-1 text-sm text-on-surface-variant">
          Describe your idea, get a live editable React landing page, and deploy it in one hop.
        </p>
      </header>

      <IdeaForm onGenerate={handleGenerate} loading={loading} />

      {error && (
        <div className="rounded-md border border-error/40 bg-error-container/10 p-3 text-sm text-error">
          {error}
        </div>
      )}

      {files && (
        <div className="flex flex-col gap-4">
          <WebsitePreview files={files} />
          <DeployPanel files={files} />
        </div>
      )}

      {!files && !loading && !error && (
        <div className="rounded-md border border-dashed border-outline-variant p-8 text-center text-sm text-outline">
          Describe an idea above to generate a live, editable site.
        </div>
      )}
    </main>
  );
}
