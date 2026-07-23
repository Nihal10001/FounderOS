"use client";

import { useState } from "react";

export function IdeaForm({
  onGenerate,
  loading,
}: {
  onGenerate: (idea: string) => void;
  loading: boolean;
}) {
  const [idea, setIdea] = useState("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!idea.trim() || loading) return;
    onGenerate(idea.trim());
  }

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <input
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
        disabled={loading}
        placeholder="A subscription box for rare houseplants..."
        className="flex-1 rounded-md border border-outline-variant bg-surface-container px-4 py-3 text-sm text-on-surface placeholder:text-outline focus:border-primary focus:outline-none disabled:opacity-50"
      />
      <button
        type="submit"
        disabled={loading || !idea.trim()}
        className="rounded-md bg-primary-container px-5 py-3 text-sm font-medium text-on-primary disabled:opacity-40"
      >
        {loading ? "Generating..." : "Build site"}
      </button>
    </form>
  );
}
