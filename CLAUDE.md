# CLAUDE.md

Guidance for working in this repo. See `README.md` for layout and commands.

## Purpose

**This repo exists to manage the user's kitty terminal configuration.** That is
the point of the repo and where work normally happens: `kitty.conf` (and
`local.conf`, which holds host-specific overrides and is git-ignored).

The `cheatsheet/` directory is a secondary, self-contained add-on that
generates a reference cheat sheet — a nice-to-have, not the focus of the repo.
Don't treat cheat sheet upkeep as a standing responsibility; only touch it when
explicitly asked.

## kitty config

- Edit `kitty.conf` for configuration changes. Keep host-specific or secret
  values in `local.conf` (git-ignored), not in the tracked config.
- kitty 0.45. After config edits, the user reloads with `ctrl+shift+f5`
  (`ctrl+shift+f6` shows the effective config for verification).

## Cheat sheet (secondary)

Only relevant when the user is working on the cheat sheet itself.

- **`cheatsheet/generate.py` is the single source of truth.** Content (rows in
  `BODY`), palettes (`THEMES`), and spacing (`LAYOUT`) live there. Never
  hand-edit files in `cheatsheet/out/` — they're generated and overwritten.
- **Rebuild through `make`, run from inside `cheatsheet/`** (`make` for
  HTML+PDFs, `make html` for HTML only). The build tooling is scoped to that
  directory — there is no root-level Makefile, by design.
- Two looks from one source: dark (screen) and light (print, ink-friendly);
  `out/kitty-cheatsheet.html` is adaptive (`@media print`). Keep both palettes
  in sync when editing colors. Keep the sheet to **one page**.
- Notation: a plain key = `Ctrl+Shift` + key; blue = literal combo; `A → B` =
  chord (press `Ctrl+Shift+A`, release, then just `B`).
- Preview is on-demand only: `make serve` (foreground, Ctrl+C to stop). Do
  **not** reintroduce a systemd service or auto-start daemon — that was tried
  and removed as over-engineering.

## Git

- Tracked: `kitty.conf`, `CLAUDE.md`, `README.md`, and the cheat sheet sources
  (`cheatsheet/{generate.py,serve.py,Makefile}`).
- Git-ignored and never committed: `local.conf` and `cheatsheet/out/`
  (generated HTML + PDFs).
- Follow the user's global git rules: single-line commit messages, never push
  (the user pushes after reviewing), don't stage/commit unless asked.
