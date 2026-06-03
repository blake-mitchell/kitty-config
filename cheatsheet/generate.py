#!/usr/bin/env python3
"""Generate kitty cheat sheet style variants + a comparison index page."""
import pathlib

OUT = pathlib.Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- shared DOM
BODY = """
<header>
  <svg width="30" height="30" viewBox="0 0 32 32">
    <path d="M5 13 L5 4 L12 9 Z" fill="var(--cat)"/>
    <path d="M27 13 L27 4 L20 9 Z" fill="var(--cat)"/>
    <circle cx="16" cy="17" r="11" fill="var(--cat)"/>
    <circle cx="11.5" cy="15.5" r="1.8" fill="#34d399"/>
    <circle cx="20.5" cy="15.5" r="1.8" fill="#34d399"/>
    <path d="M16 19.5 L14.6 21 L17.4 21 Z" fill="#f59e0b"/>
    <g stroke="var(--whisker)" stroke-width=".8">
      <line x1="2" y1="17" x2="9" y2="18"/><line x1="2" y1="21" x2="9" y2="20"/>
      <line x1="30" y1="17" x2="23" y2="18"/><line x1="30" y1="21" x2="23" y2="20"/>
    </g>
  </svg>
  <svg class="wordmark" width="200" height="27" viewBox="0 0 200 27">
    <defs>
      <linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="var(--t1)"/>
        <stop offset="100%" stop-color="var(--t2)"/>
      </linearGradient>
    </defs>
    <text x="0" y="21" font-size="21" font-weight="700"
          font-family="Helvetica Neue, Arial, sans-serif" letter-spacing="-0.4"
          fill="url(#tg)">kitty shortcuts</text>
  </svg>
  <div class="legend">
    <span class="pill">plain key = <kbd>Ctrl+Shift</kbd> + key</span>
    <span class="pill"><kbd class="lit">blue</kbd> = literal combo</span>
    <span class="pill"><kbd>A</kbd><span class="arr">&rarr;</span><kbd class="p2">B</kbd> = chord: <kbd>Ctrl+Shift+A</kbd>, release, then just <kbd class="p2">B</kbd></span>
    <span class="pill">kitty 0.45 defaults</span>
  </div>
</header>
<div class="rule"></div>

<div class="cols">

<section class="s-clip">
<h2>Clipboard</h2>
<table>
<tr><td class="k"><kbd>C</kbd> / <kbd>V</kbd></td><td>Copy / paste clipboard</td></tr>
<tr><td class="k"><kbd>S</kbd> <span class="lit">/ <kbd>Shift+Ins</kbd></span></td><td>Paste from selection</td></tr>
<tr><td class="k"><kbd>O</kbd></td><td>Pass selection to program</td></tr>
</table>
</section>

<section class="s-scroll">
<h2>Scrolling</h2>
<table>
<tr><td class="k"><kbd>K</kbd> / <kbd>J</kbd></td><td>Line up / down (also <kbd>&uarr;</kbd>/<kbd>&darr;</kbd>)</td></tr>
<tr><td class="k"><kbd>PgUp</kbd> / <kbd>PgDn</kbd></td><td>Page up / down</td></tr>
<tr><td class="k"><kbd>Home</kbd> / <kbd>End</kbd></td><td>Top / bottom</td></tr>
<tr><td class="k"><kbd>Z</kbd> / <kbd>X</kbd></td><td>Previous / next shell prompt</td></tr>
<tr><td class="k"><kbd>H</kbd></td><td>Scrollback in pager</td></tr>
<tr><td class="k"><kbd>G</kbd></td><td>Last command output</td></tr>
<tr><td class="k"><kbd>/</kbd></td><td>Search scrollback</td></tr>
</table>
</section>

<section class="s-win">
<h2>Windows (splits)</h2>
<table>
<tr><td class="k"><kbd>Enter</kbd></td><td>New window</td></tr>
<tr><td class="k"><kbd>N</kbd></td><td>New OS window</td></tr>
<tr><td class="k"><kbd>W</kbd></td><td>Close window</td></tr>
<tr><td class="k"><kbd>]</kbd> / <kbd>[</kbd></td><td>Next / previous window</td></tr>
<tr><td class="k"><kbd>F</kbd> / <kbd>B</kbd></td><td>Move forward / backward</td></tr>
<tr><td class="k"><kbd>`</kbd></td><td>Move window to primary</td></tr>
<tr><td class="k"><kbd>R</kbd></td><td>Resize window</td></tr>
<tr><td class="k"><kbd>1</kbd>&hellip;<kbd>0</kbd></td><td>Focus window 1&ndash;10</td></tr>
<tr><td class="k"><kbd>F7</kbd> / <kbd>F8</kbd></td><td>Focus / swap by letter</td></tr>
</table>
</section>

<section class="s-tabs">
<h2>Tabs</h2>
<table>
<tr><td class="k"><kbd>T</kbd> / <kbd>Q</kbd></td><td>New / close tab</td></tr>
<tr><td class="k"><kbd>&rarr;</kbd> <span class="lit">/ <kbd>Ctrl+Tab</kbd></span></td><td>Next tab</td></tr>
<tr><td class="k"><kbd>&larr;</kbd> / <kbd>Tab</kbd></td><td>Previous tab</td></tr>
<tr><td class="k"><kbd>.</kbd> / <kbd>,</kbd></td><td>Move tab forward / backward</td></tr>
<tr><td class="k"><kbd>Alt+T</kbd></td><td>Set tab title</td></tr>
</table>
</section>

<section class="s-layout">
<h2>Layout &amp; Font</h2>
<table>
<tr><td class="k"><kbd>L</kbd></td><td>Next layout</td></tr>
<tr><td class="k"><kbd>=</kbd> / <kbd>-</kbd></td><td>Font size +2 / &minus;2</td></tr>
<tr><td class="k"><kbd>Bksp</kbd></td><td>Reset font size</td></tr>
</table>
</section>

<section class="s-hints">
<h2>Hints &mdash; screen text</h2>
<table>
<tr><td class="k"><kbd>E</kbd></td><td>Open URL</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">F</kbd></td><td>Insert path</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">Shift+F</kbd></td><td>Open path</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">C</kbd> / <kbd class="p2">D</kbd></td><td>Choose files / directory</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">L</kbd> / <kbd class="p2">W</kbd></td><td>Insert line / word</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">H</kbd></td><td>Insert hash (git SHA)</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">N</kbd></td><td>Open file:line in editor</td></tr>
<tr><td class="k"><kbd>P</kbd><span class="arr">&rarr;</span><kbd class="p2">Y</kbd></td><td>Open hyperlink</td></tr>
</table>
</section>

<section class="s-opacity">
<h2>Opacity <small>(needs dynamic_background_opacity yes)</small></h2>
<table>
<tr><td class="k"><kbd>A</kbd><span class="arr">&rarr;</span><kbd class="p2">M</kbd> / <kbd class="p2">L</kbd></td><td>Opacity +0.1 / &minus;0.1</td></tr>
<tr><td class="k"><kbd>A</kbd><span class="arr">&rarr;</span><kbd class="p2">1</kbd> / <kbd class="p2">D</kbd></td><td>Opacity 100% / default</td></tr>
</table>
</section>

<section class="s-misc">
<h2>Misc</h2>
<table>
<tr><td class="k"><kbd>F1</kbd></td><td>kitty docs</td></tr>
<tr><td class="k"><kbd>F2</kbd> / <kbd>F5</kbd></td><td>Edit / reload kitty.conf</td></tr>
<tr><td class="k"><kbd>F6</kbd></td><td>Show effective config</td></tr>
<tr><td class="k"><kbd>F10</kbd> / <kbd>F11</kbd></td><td>Maximize / fullscreen</td></tr>
<tr><td class="k"><kbd>U</kbd></td><td>Unicode input</td></tr>
<tr><td class="k"><kbd>Esc</kbd></td><td>kitty shell</td></tr>
<tr><td class="k"><kbd>Del</kbd></td><td>Reset terminal</td></tr>
</table>
</section>

<section class="lit mouse s-mouse">
<h2>Mouse <small>(literal &mdash; no Ctrl+Shift implied)</small></h2>
<table>
<tr><td class="k">Click URL</td><td>Open in browser</td></tr>
<tr><td class="k">2&times; / 3&times; click</td><td>Select word / line</td></tr>
<tr><td class="k"><kbd>Ctrl+Alt</kbd>+3&times;click</td><td>Select to end of line</td></tr>
<tr><td class="k"><kbd>Ctrl+Alt</kbd>+drag</td><td>Column select</td></tr>
<tr><td class="k">Right-click</td><td>Extend selection</td></tr>
<tr><td class="k">Middle-click</td><td>Paste selection</td></tr>
<tr><td class="k"><kbd>Ctrl+Shift</kbd>+r-click</td><td>Cmd output in pager</td></tr>
<tr><td class="k"><kbd>Shift</kbd>+click/drag</td><td>Select despite mouse grab</td></tr>
</table>
</section>

</div>

<script>
  // live reload when served by serve.py; inert when opened as file:// or printed
  if (location.protocol.startsWith('http')) {
    new EventSource('/live').onmessage = () => location.reload();
  }
</script>
"""

# ------------------------------------------------------------- shared layout
LAYOUT = """
  @page { size: letter portrait; margin: 8mm; }
  * { margin: 0; padding: 0; box-sizing: border-box;
      -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font: 10pt/1.45 "Helvetica Neue", Arial, sans-serif; padding: 6px; }
  header { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
  header svg { flex: none; }
  .legend { margin-left: auto; display: flex; flex-wrap: wrap; gap: 5px 7px; justify-content: flex-end; }
  .pill { font-size: 8pt; border-radius: 99px; padding: 2px 9px; white-space: nowrap; }
  .rule { height: 3px; border-radius: 2px; margin-bottom: 13px; }
  .cols { column-count: 3; column-gap: 16px; }
  section { break-inside: avoid; margin-bottom: 12px; border-radius: 9px; overflow: hidden; }
  h2 { font-size: 9.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: .07em; padding: 5px 10px; }
  h2 small { font-size: 7.5pt; font-weight: 400; text-transform: none; letter-spacing: 0; opacity: .85; }
  table { width: 100%; border-collapse: collapse; }
  td { padding: 3px 8px; vertical-align: top; }
  td.k { white-space: nowrap; width: 1%; padding-right: 12px; }
  section.mouse td.k { white-space: normal; max-width: 42%; }
  kbd { display: inline-block; font: 9pt/1.3 "DejaVu Sans Mono", Menlo, monospace;
        border-radius: 4px; padding: 0.5px 4px; }
  .arr { font-size: 8.5pt; }
"""

# ------------------------------------------------------------------- themes
THEMES = {
    "b-terminal": {
        "label": "B · Terminal dark",
        "blurb": "Dark GitHub-dark palette, neon accents with a soft glow, monospace ❯ headers, dark keycaps. Looks amazing on screen; ink-hungry to print.",
        "css": """
  body { color: #c9d1d9; background: #0d1117;
         --cat: #e6edf3; --whisker: #8b949e; --t1: #3fb950; --t2: #58a6ff; }
  .pill { color: #8b949e; background: #161b22; border: 1px solid #30363d; }
  .rule { background: linear-gradient(90deg,
      #2dd4bf, #58a6ff, #bc8cff, #f0b72f, #ff7bc8, #3fb950, #8b949e, #818cf8, #ff7b72); }
  .s-clip   { --a: #2dd4bf; } .s-scroll { --a: #58a6ff; } .s-win  { --a: #bc8cff; }
  .s-tabs   { --a: #f0b72f; } .s-layout { --a: #ff7bc8; } .s-hints{ --a: #3fb950; }
  .s-opacity{ --a: #8b949e; } .s-misc   { --a: #818cf8; } .s-mouse{ --a: #ff7b72; }
  section { background: #161b22; border: 1px solid #30363d;
            border-color: color-mix(in srgb, var(--a) 55%, #30363d);
            box-shadow: 0 0 7px color-mix(in srgb, var(--a) 30%, transparent); }
  h2 { font-family: "DejaVu Sans Mono", Menlo, monospace; letter-spacing: .04em;
       color: var(--a); background: #10151c; border-bottom: 1px solid var(--a); }
  h2::before { content: "\\276F "; }
  tr:nth-child(even) td { background: #1b2028; background: color-mix(in srgb, var(--a) 8%, #161b22); }
  kbd { color: #e6edf3; background: linear-gradient(#21262d, #161b22);
        border: 1px solid #3a414b; border-bottom-width: 2.5px; }
  .lit kbd, kbd.lit { border-color: #58a6ff; color: #79c0ff; }
  kbd.p2 { background: transparent; border-style: dashed; border-bottom-width: 1px; }
  .arr { color: #6e7681; }
""",
    },
    "b-terminal-light": {
        "label": "B2 · Terminal light",
        "blurb": "Variant B translated to a GitHub-light palette for printing: same ❯ headers and accent identity, white cards, darker accents, soft tinted shadows. Easy on ink.",
        "css": """
  body { color: #1f2328; background: #fff;
         --cat: #1f2328; --whisker: #6b7280; --t1: #1a7f37; --t2: #0969da; }
  .pill { color: #57606a; background: #f6f8fa; border: 1px solid #d0d7de; }
  .rule { background: linear-gradient(90deg,
      #0d7d76, #0969da, #8250df, #b08800, #bf3989, #1a7f37, #57606a, #5b5bd6, #cf222e); }
  .s-clip   { --a: #0d7d76; } .s-scroll { --a: #0969da; } .s-win  { --a: #8250df; }
  .s-tabs   { --a: #b08800; } .s-layout { --a: #bf3989; } .s-hints{ --a: #1a7f37; }
  .s-opacity{ --a: #57606a; } .s-misc   { --a: #5b5bd6; } .s-mouse{ --a: #cf222e; }
  section { background: #fff; border: 1px solid #d0d7de;
            border-color: color-mix(in srgb, var(--a) 50%, #d0d7de);
            box-shadow: 0 1px 3px color-mix(in srgb, var(--a) 18%, transparent); }
  h2 { font-family: "DejaVu Sans Mono", Menlo, monospace; letter-spacing: .04em;
       color: var(--a); background: #eef1f5; border-bottom: 1px solid var(--a); }
  h2::before { content: "\\276F "; }
  tr:nth-child(even) td { background: #f6f8fa; background: color-mix(in srgb, var(--a) 6%, #fff); }
  kbd { color: #1f2328; background: linear-gradient(#fff, #e9ecf0);
        border: 1px solid #b7bec9; border-bottom-width: 2.5px;
        box-shadow: 0 1px 1px rgba(31,35,40,.08); }
  .lit kbd, kbd.lit { border-color: #0969da; color: #0550ae; background: #f0f7ff; }
  kbd.p2 { background: #fff; border-style: dashed; border-bottom-width: 1px; }
  .arr { color: #8b949e; }
""",
    },
}

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>kitty Shortcuts — {label}</title>
<style>{layout}{css}</style>
</head>
<body>
{body}
</body>
</html>
"""

for slug, t in THEMES.items():
    (OUT / f"{slug}.html").write_text(
        PAGE.format(label=t["label"], layout=LAYOUT, css=t["css"], body=BODY))

# ---------------- dark PDF variant: full-bleed background, no white frame --
dark_pdf_css = THEMES["b-terminal"]["css"] + """
  @page { margin: 0; }
  body { padding: 9mm; }
"""
(OUT / "b-terminal-pdf.html").write_text(
    PAGE.format(label="B · Terminal dark (full-bleed PDF)",
                layout=LAYOUT, css=dark_pdf_css, body=BODY))

# ---------------- adaptive main sheet: dark on screen, light in print ------
adaptive_css = (
    "\n  @media screen {" + THEMES["b-terminal"]["css"] + "  }\n"
    "\n  @media print {" + THEMES["b-terminal-light"]["css"] + "  }\n"
)
(OUT / "kitty-cheatsheet.html").write_text(
    PAGE.format(label="Terminal (adaptive: dark screen / light print)",
                layout=LAYOUT, css=adaptive_css, body=BODY))

# -------------------------------------------------------------------- index
cards = "\n".join(f"""
  <div class="card">
    <h2>{t["label"]}</h2>
    <p>{t["blurb"]}</p>
    <a href="{slug}.html" target="_blank">open full size &rarr;</a>
    <div class="frame"><iframe src="{slug}.html"></iframe></div>
  </div>""" for slug, t in THEMES.items())

(OUT / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>kitty cheat sheet — pick a style</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font: 14px/1.5 "Helvetica Neue", Arial, sans-serif; background: #1c2128; color: #e6edf3; padding: 24px; }}
  h1 {{ font-size: 22px; margin-bottom: 4px; }}
  .sub {{ color: #8b949e; margin-bottom: 20px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(460px, 1fr)); gap: 20px; }}
  .card {{ background: #22272e; border: 1px solid #444c56; border-radius: 10px; padding: 14px; }}
  .card h2 {{ font-size: 16px; margin-bottom: 2px; }}
  .card p {{ font-size: 12.5px; color: #8b949e; margin-bottom: 4px; min-height: 3em; }}
  .card a {{ font-size: 12.5px; color: #58a6ff; }}
  .frame {{ margin-top: 10px; width: 440px; height: 330px; overflow: hidden;
            border-radius: 6px; border: 1px solid #444c56; background: #fff; }}
  iframe {{ width: 880px; height: 660px; border: 0;
            transform: scale(.5); transform-origin: top left; pointer-events: none; }}
</style>
</head>
<body>
<h1>kitty cheat sheet — pick a style</h1>
<p class="sub">Click “open full size” to inspect any variant at 100%. Previews are scaled 50%.</p>
<div class="grid">{cards}</div>
<script>
  if (location.protocol.startsWith('http')) {{
    new EventSource('/live').onmessage = () => location.reload();
  }}
</script>
</body>
</html>
""")

print("wrote:", ", ".join(f"{s}.html" for s in THEMES), "+ index.html")
