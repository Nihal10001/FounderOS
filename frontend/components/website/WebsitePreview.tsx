"use client";

import { Sandpack } from "@codesandbox/sandpack-react";
import type { WebsiteFiles } from "@/lib/website-api";

export function WebsitePreview({ files }: { files: WebsiteFiles }) {
  const sandpackFiles: Record<string, { code: string }> = {};
  for (const [path, content] of Object.entries(files)) {
    sandpackFiles[path] = { code: content };
  }

  return (
    <Sandpack
      template="react"
      theme="dark"
      files={sandpackFiles}
      options={{
        showConsole: true,
        showTabs: true,
        editorHeight: 520,
      }}
    />
  );
}
