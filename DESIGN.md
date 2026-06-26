---
version: v1.0.5
name: Super SP v1.0.5 - 亚马逊广告全景分析系统
description: >-
  Vercel Geist Light theme adapted for Super SP advertising analytics dashboard.
  Minimal, high-contrast, developer-focused interface for Amazon seller data.
colors:
  primary: "#171717"
  secondary: "#4d4d4d"
  tertiary: "#006bff"
  neutral: "#fafafa"
  background-100: "#ffffff"
  background-200: "#fafafa"
  on-primary: "#ffffff"
  on-tertiary: "#ffffff"
  gray-100: "#f2f2f2"
  gray-200: "#ebebeb"
  gray-300: "#e6e6e6"
  gray-400: "#eaeaea"
  gray-500: "#c9c9c9"
  gray-600: "#a8a8a8"
  gray-700: "#8f8f8f"
  gray-800: "#7d7d7d"
  gray-900: "#4d4d4d"
  gray-1000: "#171717"
  gray-alpha-100: "#0000000d"
  gray-alpha-200: "#00000015"
  gray-alpha-300: "#0000001a"
  gray-alpha-400: "#00000014"
  gray-alpha-500: "#00000036"
  gray-alpha-600: "#0000003d"
  gray-alpha-700: "#00000070"
  gray-alpha-800: "#00000082"
  gray-alpha-900: "#000000b3"
  gray-alpha-1000: "#000000e8"
  blue-100: "#f0f7ff"
  blue-200: "#e9f4ff"
  blue-300: "#dfefff"
  blue-400: "#cae7ff"
  blue-500: "#94ccff"
  blue-600: "#48aeff"
  blue-700: "#006bff"
  blue-800: "#0059ec"
  blue-900: "#005ff2"
  blue-1000: "#002359"
  red-100: "#ffeeef"
  red-200: "#ffe8ea"
  red-300: "#ffe3e4"
  red-400: "#ffd7d6"
  red-500: "#ffb1b3"
  red-600: "#ff676d"
  red-700: "#fc0035"
  red-800: "#ea001d"
  red-900: "#d8001b"
  red-1000: "#47000c"
  amber-100: "#fff6de"
  amber-200: "#fff4cf"
  amber-300: "#fff1c1"
  amber-400: "#ffdc73"
  amber-500: "#ffc543"
  amber-600: "#ffa600"
  amber-700: "#ffae00"
  amber-800: "#ff9300"
  amber-900: "#aa4d00"
  amber-1000: "#561900"
  green-100: "#ecfdec"
  green-200: "#e5fce7"
  green-300: "#d3fad1"
  green-400: "#b9f5bc"
  green-500: "#82eb8d"
  green-600: "#4ce15e"
  green-700: "#28a948"
  green-800: "#279141"
  green-900: "#107d32"
  green-1000: "#003a00"
typography:
  heading-24:
    fontFamily: Geist Sans
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: "-0.96px"
  heading-20:
    fontFamily: Geist Sans
    fontSize: 20px
    fontWeight: 600
    lineHeight: 26px
    letterSpacing: "-0.4px"
  heading-16:
    fontFamily: Geist Sans
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
    letterSpacing: "-0.32px"
  heading-14:
    fontFamily: Geist Sans
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
    letterSpacing: "-0.28px"
  button-14:
    fontFamily: Geist Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  button-12:
    fontFamily: Geist Sans
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
  label-13:
    fontFamily: Geist Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 16px
  label-12:
    fontFamily: Geist Sans
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  label-12-mono:
    fontFamily: Geist Mono
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  copy-14:
    fontFamily: Geist Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  copy-13:
    fontFamily: Geist Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 18px
  copy-13-mono:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 18px
spacing:
  1: 4px
  2: 8px
  3: 12px
  4: 16px
  6: 24px
  8: 32px
  10: 40px
  16: 64px
  base: 4px
rounded:
  sm: 6px
  md: 12px
  lg: 16px
  full: 9999px
components:
  button-primary:
    backgroundColor: "{colors.gray-1000}"
    textColor: "{colors.background-100}"
    typography: "{typography.button-14}"
    rounded: "{rounded.sm}"
    height: 40px
  button-primary-hover:
    backgroundColor: "#2a2a2a"
  button-secondary:
    backgroundColor: "{colors.background-100}"
    textColor: "{colors.primary}"
    typography: "{typography.button-14}"
    rounded: "{rounded.sm}"
    height: 40px
  button-tertiary:
    textColor: "{colors.primary}"
    backgroundColor: transparent
    typography: "{typography.button-14}"
    rounded: "{rounded.sm}"
    height: 40px
  button-error:
    backgroundColor: "{colors.red-800}"
    textColor: "#ffffff"
    typography: "{typography.button-14}"
    rounded: "{rounded.sm}"
    height: 40px
  button-small:
    typography: "{typography.button-12}"
    rounded: "{rounded.sm}"
    height: 32px
  input:
    backgroundColor: "{colors.background-100}"
    textColor: "{colors.primary}"
    typography: "{typography.copy-14}"
    rounded: "{rounded.sm}"
    height: 40px
  input-small:
    typography: "{typography.copy-14}"
    rounded: "{rounded.sm}"
    height: 32px
  card:
    backgroundColor: "{colors.background-100}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
  card-raised:
    backgroundColor: "{colors.background-100}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
  table-header:
    backgroundColor: "{colors.background-200}"
    textColor: "{colors.gray-900}"
    typography: "{typography.label-12}"
  chip-super:
    backgroundColor: "{colors.green-100}"
    textColor: "{colors.green-700}"
    rounded: "{rounded.full}"
    typography: "{typography.label-12}"
  chip-potential:
    backgroundColor: "{colors.blue-100}"
    textColor: "{colors.blue-700}"
    rounded: "{rounded.full}"
    typography: "{typography.label-12}"
  chip-warning:
    backgroundColor: "{colors.amber-100}"
    textColor: "{colors.amber-900}"
    rounded: "{rounded.full}"
    typography: "{typography.label-12}"
  chip-invalid:
    backgroundColor: "{colors.red-100}"
    textColor: "{colors.red-700}"
    rounded: "{rounded.full}"
    typography: "{typography.label-12}"
  filter-stats:
    backgroundColor: "{colors.background-200}"
    textColor: "{colors.primary}"
    typography: "{typography.heading-16}"
  metric-card:
    backgroundColor: "{colors.background-200}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
---

# Super SP Geist

## Overview

Super SP Geist applies Vercel's Geist design system to the Super SP advertising analytics dashboard. The interface is minimal and high-contrast: restrained grey-scale surfaces, Geist Sans typography, and color reserved for state signalling and the most important actions. The aesthetic prioritises readability, data density, and speed over decoration — every pixel serves the seller's decision-making workflow.

Target audience: Amazon SP advertising sellers who need to scan thousands of search terms and identify high-value keywords versus wasted spend in seconds.

## Colors

Each non-background scale runs 10 steps (100–1000) where the step encodes intent, not just lightness:

- **100** default background
- **200** hover background
- **300** active background
- **400** default border
- **500** hover border
- **600** active border
- **700** solid fill, high contrast
- **800** solid fill, hover
- **900** secondary text and icons
- **1000** primary text and icons

`background-100` is the primary page and card surface. `background-200` is a secondary surface for subtle separation. The `gray-alpha-*` tokens are translucent for borders, dividers, and overlays. Solid `gray-*` holds its contrast on any surface for text and opaque fills.

Accent scales carry meaning:
- **Blue** for primary interaction, links, focus rings, and potential-type classifications.
- **Green** for super-type classifications and positive metrics.
- **Amber** for warnings, high-competition classifications.
- **Red** for errors, invalid classifications, negative spend signals.

## Typography

Geist Sans sets all UI text. Geist Mono sets data values in table cells and metric numbers where tabular alignment matters. The `typography` tokens carry concrete values — use them instead of hand-setting font-size or weight.

- **Headings (heading-24 through heading-14):** Section titles, panel headers.
- **Buttons (button-14, button-12):** Medium-weight labels for interactive controls.
- **Labels (label-13, label-12):** Table headers, metadata, form labels, filter labels.
- **Copy (copy-14, copy-13):** Body text, table data cells, helper text.
- **Mono variants:** Use `copy-13-mono` for dollar amounts and order counts in tables; `label-12-mono` for pill-badge counts.

## Layout

Spacing follows a 4px scale: 4, 8, 12, 16, 24, 32, 40, 64, 96px. Keep a consistent three-step rhythm: `spacing.2` (8px) inside a group, `spacing.4` (16px) between groups, `spacing.6`–`spacing.8` (24–32px) between sections. Cards use `spacing.6` (24px) padding; `spacing.4` (16px) when compact.

The dashboard uses a two-column layout: a 260px sidebar for category navigation on the left, and a fluid content area on the right. Maximum content width is 1400px. Breakpoints: `sm` 401px, `md` 601px, `lg` 961px, `xl` 1200px.

## Elevation & Depth

Hierarchy comes from tonal surfaces and borders first; shadows stay subtle.

- **Raised cards:** `0 2px 2px rgba(0, 0, 0, 0.04)`
- **Popovers and menus:** `0 1px 1px rgba(0, 0, 0, 0.02), 0 4px 8px -4px rgba(0, 0, 0, 0.04), 0 16px 24px -8px rgba(0, 0, 0, 0.06)`
- **Modals and dialogs:** `0 1px 1px rgba(0, 0, 0, 0.02), 0 8px 16px -4px rgba(0, 0, 0, 0.04), 0 24px 32px -8px rgba(0, 0, 0, 0.06)`

## Shapes

Radii stay tight: `sm` (6px) for everyday surfaces and controls, `md` (12px) for cards, `lg` (16px) for fullscreen surfaces. Reserve `full` (9999px) for chips, pill badges, and circular controls. Keep one radius family per view.

## Motion

Use motion only when it clarifies a change. Most interactions should feel instant (0ms). When motion helps, use `cubic-bezier(0.175, 0.885, 0.32, 1.1)`: roughly 150ms for state changes, 200ms for tooltips, 300ms for overlays. Honour `prefers-reduced-motion`.

## Components

- **`button-primary`:** Solid `gray-1000` fill, white text. Single most important action per view (e.g., "Export CSV").
- **`button-secondary`:** White fill, `gray-alpha-400` border. Standard action (e.g., "Reset Filters").
- **`button-tertiary`:** Transparent fill, `gray-1000` text. Low-emphasis action.
- **`button-error`:** Solid `red-800` fill, white text. Destructive action.
- **`input`:** White fill, `gray-alpha-400` border, 6px radius. Search and filter inputs.
- **`card`:** White surface, `gray-alpha-400` border, 12px radius. Dashboard panels.
- **`chip-super/potential/warning/invalid`:** Coloured pill badges for 14-dimension classification labels.
- **`metric-card`:** Tinted `background-200` surface for KPI numbers in the campaign-metrics and spend-structure sections.

Hover states step up the scale: a `100` fill becomes `200` on hover, borders move from `400` to `500`. Focus shows a two-layer ring (`box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px #006bff`).

## Voice & Content

- Use Title Case for filter labels, button labels, section titles, and table headers.
- Use sentence case for helper text, metric labels, and tooltip descriptions.
- Name actions with a verb and a noun: "Export CSV", "Reset Filters", never "OK" or "Confirm".
- Use numerals in data: "3 campaigns", "12,847 search terms", not "three campaigns".
- Chip labels drop the word "type": "Super Keywords" not "Super Keyword Type".
- Empty states point to the first action: "No data yet. Place ad reports in the data/ folder and run the analysis."

## Do's and Don'ts

- **Do** use `gray-1000` for primary text, `gray-900` for secondary, `gray-700` for disabled.
- **Do** keep solid accent color (`blue-700`) for the primary action and link interactions only.
- **Do** hold WCAG AA contrast (4.5:1 for `copy-14` body text).
- **Do** show the focus ring on every interactive element at `:focus-visible`.
- **Do** apply the typography tokens instead of hand-setting font size, line weight, or height.
- **Don't** signal state with color alone — pair with text or shape (e.g., chip badge label).
- **Don't** use `background-200` as a general fill; it is for subtle separation only.
- **Don't** mix rounded and sharp corners in one view.
- **Don't** swap `gray-*` for `background-*` — they are separate scales.
- **Don't** use more than two font weights in one view (600 for headings, 400/500 for everything else).
