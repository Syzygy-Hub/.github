<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-dark-1200.png">
  <img src="https://raw.githubusercontent.com/Syzygy-Hub/.github/main/brand/assets/banners/syzygy-banner-light-1200.png" alt="Syzygy" width="100%">
</picture>

# Syzygy Ecosystem

**Engineering Ecosystem for Intelligent Applications**

Syzygy is an AI-enabled cross-platform engineering framework. Every layer above Foundation is independently usable. No peer layer depends on another peer. Base is the only composer.

## Architecture

```
                                     syzygy-foundation-*
                                              |
      +-------------------+-------------------+-------------------+-------------------+
      |                   |                                       |                   |
      v                   v                                       v                   v
 syzygy-ui-*        syzygy-core-*                         syzygy-services-*      syzygy-ai-*
      |                   |                                       |                   |
      +-------------------+-------------------+-------------------+-------------------+
                                              |
                                              v
                              syzygy-base-* (composer/scaffold)
                                              |
                                              v
                                    Syzygy Example App
```

## Design principle

Every layer above Foundation is independently usable. No peer layer depends on another peer. Base is the only composer.

## Full architecture

Full architecture documentation: [engineering/architecture/syzygy-ecosystem.md](https://github.com/Syzygy-Hub/.github/blob/main/engineering/architecture/syzygy-ecosystem.md)
