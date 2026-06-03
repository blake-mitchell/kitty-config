# kitty config

Personal [kitty](https://sw.kovidgoyal.net/kitty/) terminal configuration.

```
kitty/
├── kitty.conf       # the kitty configuration  ← the point of this repo
├── local.conf       # host-specific overrides (git-ignored)
├── README.md
├── CLAUDE.md
└── cheatsheet/      # secondary add-on — a generated reference sheet
```

`kitty.conf` is the main thing here. Keep host-specific or secret values in
`local.conf` (git-ignored), not in the tracked config. After edits, reload in
kitty with `ctrl+shift+f5` (`ctrl+shift+f6` shows the effective config).

## Cheat sheet (add-on)

A self-contained tool under `cheatsheet/` that generates a printable /
on-screen keyboard + mouse reference for kitty's default bindings. It's a
nice-to-have, not the focus of the repo — its build tooling lives entirely in
that directory.

```bash
cd cheatsheet
make            # generate HTML + render both PDFs (default target)
make html       # regenerate HTML only (live tabs reload themselves)
make pdf        # render PDFs into out/pdf/
make serve      # run the live-reload preview server (Ctrl+C to stop)
make open       # open the live preview in your browser (needs `make serve`)
make clean      # remove out/
make help       # list targets
```

One source of truth (`cheatsheet/generate.py`) drives two looks: **dark**
(screen) and **light** (ink-friendly, for print). `out/kitty-cheatsheet.html`
is adaptive — dark in a browser, light when printed (`@media print`).

- **Edit content** → the `BODY` table rows in `generate.py`, then `make`.
- **Edit colors** → the `b-terminal` (dark) / `b-terminal-light` (print)
  entries in `THEMES`; keep both in sync.
- **Edit spacing/sizing** → the shared `LAYOUT` block. Keep the sheet one page.
- Notation: a plain key = `Ctrl+Shift` + key; blue = literal combo; `A → B` =
  chord (press `Ctrl+Shift+A`, release, then just `B`).

Preview is on-demand: `make serve` (foreground) starts a live-reload server at
<http://127.0.0.1:7045/kitty-cheatsheet.html>; re-running `make html` refreshes
the open tab via SSE. `out/` (generated HTML + PDFs) is git-ignored and
regenerable, so it's never committed.

Requires `python3` (stdlib only), headless `google-chrome` (PDF rendering), and
optionally `poppler-utils` (`pdfinfo`, for the page-count check).
