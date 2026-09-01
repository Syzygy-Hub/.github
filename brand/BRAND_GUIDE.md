<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="100%">
</picture>

# Syzygy Brand Guide

Usage guidelines for the Syzygy logo, icon, banners, color palette, and typography. See [README.md](README.md) for the asset file list.

## Logo & icon

### Clear space

Keep clear space around the icon/logo equal to at least the height of the icon's own inner ring on all sides. Don't let text, other logos, or UI chrome (nav bars, borders, adjacent badges) intrude into that space.

### Minimum size

- Icon: don't render smaller than 32×32px (`syzygy-icon-32.png` is the smallest pre-rendered size available; anything smaller and the rings lose definition).
- Banner: don't render narrower than 300px wide — below that, the wordmark becomes illegible.

### Do

- Use the icon/banner exactly as provided in `Assets/` — the pre-exported sizes (`-192`, `-512`, `-1024`, `-1200`, `-2400`) cover favicon through print/retina use cases.
- Use the dark-background variant (`syzygy-banner-dark-*`) on dark surfaces, and the light-background variant (`syzygy-banner-light-*`) on light surfaces — pick by actual background color, not by the app's overall theme.
- Maintain the icon/banner's original aspect ratio at all times — scale width and height together.
- Use the SVG (`syzygy-icon.svg`) wherever scalability matters (README headers, print) instead of a raster export.

### Don't

- Don't recolor the rings (purple/teal/coral) — these three colors are the fixed brand palette and shouldn't be substituted, tinted, or modified.
- Don't stretch or distort the icon/banner on one axis — always scale proportionally.
- Don't add drop shadows, glows, bevels, or other effects — the assets are designed to sit flat on their background.
- Don't rotate the icon/banner at any angle.
- Don't place the icon/banner on a background color close to its own ring colors — it needs contrast to stay legible (this is why both a light and dark banner variant exist).

## Color palette

| Color | Hex |
|---|---|
| Purple | ![7F77DD](https://img.shields.io/badge/-%237F77DD-7F77DD?style=flat-square) `#7F77DD` |
| Teal | ![1D9E75](https://img.shields.io/badge/-%231D9E75-1D9E75?style=flat-square) `#1D9E75` |
| Coral | ![D85A30](https://img.shields.io/badge/-%23D85A30-D85A30?style=flat-square) `#D85A30` |

## Typography

- **Wordmark & headings:** [Sora](https://fonts.google.com/specimen/Sora) — bold weight, geometric and technical, matches the icon's angular ring construction.
- **Body text / documentation:** pair Sora headings with [Inter](https://fonts.google.com/specimen/Inter) (or the platform's system font — San Francisco on iOS, Roboto on Android) for body copy. Sora is a display face; don't set long-form paragraphs in it.

## Correct vs. incorrect usage

**Correct:** The icon appears at its original proportions, rings in their original purple/teal/coral, sitting on a plain background with enough contrast to read clearly, with generous clear space around it before any other text or logo begins.

**Incorrect:** The icon has been squeezed narrower than its source aspect ratio, its rings recolored to match a single-brand accent color, a drop shadow added underneath, and it's rotated slightly and placed directly beside another logo with no clear space between them. Any one of these on its own is a misuse — combined, this is what to avoid entirely.

## Available Assets

All assets are hosted at `brand/assets/` in the `Syzygy-Hub/.github` repository.

### Banners

**Light banners**

| Filename | Format | URL |
|---|---|---|
| `syzygy-banner-light-1200.png` | PNG 1200px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png` |
| `syzygy-banner-light-2400.png` | PNG 2400px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-2400.png` |
| `syzygy-banner-light-1200.webp` | WebP 1200px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.webp` |
| `syzygy-banner-light-2400.webp` | WebP 2400px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-2400.webp` |
| `syzygy-banner-light.webp` | WebP (full-size) | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light.webp` |
| `syzygy-banner-light.svg` | SVG (scalable) | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light.svg` |

**Dark banners**

| Filename | Format | URL |
|---|---|---|
| `syzygy-banner-dark-1200.png` | PNG 1200px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png` |
| `syzygy-banner-dark-2400.png` | PNG 2400px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-2400.png` |
| `syzygy-banner-dark-1200.webp` | WebP 1200px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.webp` |
| `syzygy-banner-dark-2400.webp` | WebP 2400px | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-2400.webp` |
| `syzygy-banner-dark.webp` | WebP (full-size) | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark.webp` |
| `syzygy-banner-dark.svg` | SVG (scalable) | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark.svg` |

### Icons

| Filename | Format | Dimensions | URL |
|---|---|---|---|
| `syzygy-icon-32.png` | PNG | 32×32 | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon-32.png` |
| `syzygy-icon-192.png` | PNG | 192×192 | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon-192.png` |
| `syzygy-icon-512.png` | PNG | 512×512 | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon-512.png` |
| `syzygy-icon-1024.png` | PNG | 1024×1024 | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon-1024.png` |
| `syzygy-icon-512.webp` | WebP | 512×512 | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon-512.webp` |
| `syzygy-icon-1024.webp` | WebP | 1024×1024 | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon-1024.webp` |
| `syzygy-icon.svg` | SVG | Scalable | `https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/icons/syzygy-icon.svg` |
