---
name: AI Operating System
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c2c6d6'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#8c909f'
  outline-variant: '#424754'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e6a'
  primary-container: '#4d8eff'
  on-primary-container: '#00285d'
  inverse-primary: '#005ac2'
  secondary: '#d0bcff'
  on-secondary: '#3c0091'
  secondary-container: '#571bc1'
  on-secondary-container: '#c4abff'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#00a572'
  on-tertiary-container: '#00311f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  mono-label:
    fontFamily: Geist Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for a high-performance virtual organization platform. It draws inspiration from modern technical tools like Linear and Vercel, prioritizing speed, clarity, and structural integrity. The brand personality is "The Intelligent Engine"—authoritative yet invisible, sophisticated yet accessible.

The aesthetic follows a **Modern Corporate** style with **Glassmorphic** accents. It utilizes ultra-thin borders and expansive white space to create a "canvas" feel where data and AI agents are the primary actors. The UI should evoke an emotional response of total control and effortless scale, mimicking a futuristic operating system dedicated to organizational logic.

## Colors

The system defaults to a "Deep Obsidian" dark mode to emphasize the "AI OS" aesthetic, though it fully supports a crisp light mode. 

- **Primary & Secondary:** A vibrant gradient of Indigo and Purple is used for high-intent actions, active AI processing states, and primary navigation highlights.
- **Semantic Accents:** Emerald is reserved for "System Health" and "Success" states. Rose is used sparingly for "Critical Errors" or "Halted Processes."
- **Neutrals:** In dark mode, use a scale of cool grays starting from #020617 (Background) to #1E293B (Borders). In light mode, use #FFFFFF for surfaces and #F1F5F9 for background fills.

## Typography

The typography leverages **Geist** for its technical precision and optimal legibility in data-dense environments. 

- **Headlines:** Use tight letter-spacing on larger sizes to maintain a sleek, modern appearance.
- **Data Display:** For AI logs, timestamps, or system IDs, use a monospaced variant of the font to reinforce the "Operating System" feel.
- **Hierarchy:** Maintain a clear distinction between "System Labels" (all-caps, small size, slightly tracked out) and "Content Body" (standard sentence case).

## Layout & Spacing

The design system utilizes a **12-column fluid grid** for the main workspace, transitioning to a single-column layout on mobile.

- **The Sidebar:** A fixed-width sidebar (280px) houses the organizational hierarchy. It uses a glassmorphic background blur to distinguish it from the main canvas.
- **Spacing Rhythm:** Based on a 4px baseline. Most components should use 16px (4 units) or 24px (6 units) for internal padding to maintain a spacious, premium feel.
- **Density:** Provide a "Compact" mode for data-heavy executive reports where spacing is reduced to 8px between list items.

## Elevation & Depth

Depth is achieved through **Tonal Layering** supplemented by ultra-soft ambient shadows. 

1. **Floor (Level 0):** The base background (#020617).
2. **Card/Canvas (Level 1):** Slightly elevated surface (#0F172A) with a 1px border (#1E293B). 
3. **Overlays/Modals (Level 2):** Use a backdrop-filter (blur: 12px) with a semi-transparent surface (alpha: 0.7).
4. **Shadows:** Use a single, very large blur radius (32px) with low opacity (15%) for floating elements to avoid a "muddy" appearance. Shadows should inherit a slight indigo tint in dark mode.

## Shapes

The shape language is consistently "Soft-Geometric." 

- **Standard Elements:** Use 12px (`rounded-lg`) for standard cards and containers.
- **Buttons & Inputs:** Use 8px (`rounded-md`) to maintain a slightly more functional and precise appearance.
- **Status Badges:** Use fully pill-shaped (999px) containers for status indicators to differentiate them from interactive buttons.

## Components

- **Executive Cards:** Use a subtle hover transition where the 1px border color shifts from gray to the primary Indigo. Background should subtly brighten by 2%.
- **AI Status Badges:** Include a small "pulse" animation dot next to active agent names. Use Emerald for "Idle" and Purple for "Processing."
- **Kanban Cards:** High-contrast title typography with a monospaced "Task ID" in the top right. Ghost borders for empty states.
- **Timeline Feed:** Use a vertical 2px line in #1E293B. Events are marked with 8px circular nodes. Primary events get a Purple glow.
- **Input Fields:** Minimalist design—no background fill, only a bottom border that expands to a full 1px outline on focus.
- **Progress Bars:** Ultra-thin (4px height) with a subtle outer glow when the AI is actively calculating/generating data.