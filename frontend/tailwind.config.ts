import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class",
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        background: "#0b1326",
        "on-background": "#dae2fd",
        surface: "#0b1326",
        "surface-container-lowest": "#060e20",
        "surface-container-low": "#131b2e",
        "surface-container": "#171f33",
        "surface-container-high": "#222a3d",
        "surface-container-highest": "#2d3449",
        "surface-bright": "#31394d",
        "on-surface": "#dae2fd",
        "on-surface-variant": "#c2c6d6",
        outline: "#8c909f",
        "outline-variant": "#424754",
        primary: "#adc6ff",
        "on-primary": "#002e6a",
        "primary-container": "#4d8eff",
        secondary: "#d0bcff",
        "secondary-container": "#571bc1",
        tertiary: "#4edea3",
        "tertiary-container": "#00a572",
        error: "#ffb4ab",
        "error-container": "#93000a",
      },
      fontFamily: {
        sans: ["Geist", "sans-serif"],
        mono: ["Geist Mono", "monospace"],
      },
      borderRadius: {
        sm: "0.25rem",
        DEFAULT: "0.5rem",
        md: "0.75rem",
        lg: "1rem",
        xl: "1.5rem",
      },
    },
  },
  plugins: [],
};
export default config;
