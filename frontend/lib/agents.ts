export const AGENT_META = {
  research: {
    label: "Research Agent",
    color: "#adc6ff", // primary — indigo
    border: "border-primary",
    dot: "bg-primary",
  },
  marketing: {
    label: "Marketing Agent",
    color: "#d0bcff", // secondary — purple
    border: "border-secondary",
    dot: "bg-secondary",
  },
  finance: {
    label: "Finance Agent",
    color: "#4edea3", // tertiary — emerald
    border: "border-tertiary",
    dot: "bg-tertiary",
  },
  manager: {
    label: "Manager Agent",
    color: "#4d8eff", // primary-container
    border: "border-primary-container",
    dot: "bg-primary-container",
  },
} as const;

export type AgentKey = keyof typeof AGENT_META;
