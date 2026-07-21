"use client";

import { useState } from "react";

export function ChatComposer({
  onSubmit,
  disabled,
}: {
  onSubmit: (message: string) => void;
  disabled: boolean;
}) {
  const [value, setValue] = useState("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!value.trim() || disabled) return;
    onSubmit(value.trim());
    setValue("");
  }

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        disabled={disabled}
        placeholder="I want to launch an AI fitness app..."
        className="flex-1 rounded-md border border-outline-variant bg-surface-container px-4 py-3 text-sm text-on-surface placeholder:text-outline focus:border-primary focus:outline-none disabled:opacity-50"
      />
      <button
        type="submit"
        disabled={disabled || !value.trim()}
        className="rounded-md bg-primary-container px-5 py-3 text-sm font-medium text-on-primary disabled:opacity-40"
      >
        {disabled ? "Working..." : "Send to team"}
      </button>
    </form>
  );
}
