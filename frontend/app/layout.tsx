import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "AI Org Chart",
  description: "Your virtual startup team — Research, Marketing, Finance & Manager agents",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-background text-on-background font-sans">
        {children}
      </body>
    </html>
  );
}
