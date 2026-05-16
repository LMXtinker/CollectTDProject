# Changelog

All notable changes are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.5.0-beta] — 2026-05-16

First public beta release of `tdCollectProject` (formerly `CollectTDProject`). Consolidates all prior internal development into a single shipped artifact. Earlier internal `v1.x` and `v0.3.x` tags have been retired.

### Scanning

- Recursive scan of the project network or a defined subtree from a configurable Scan Root
- Detects file references across all operator types by evaluating string parameters
- Smart skip rule — already-local relative references that resolve inside `project.folder` are filtered automatically; everything else (absolute, external, broken) is recorded
- Configurable `Max Depth` (`0` = unlimited)
- Exclusion lists: skip specific COMP paths or file extensions
- Palette / system exclusion — skips components from the TD palette and internal system paths
- **Broken-path detection** — missing source files are flagged with `⚠` in the scan log, never silently dropped. The `Files_Table` `Exists` column records `'1'` (on disk) or `'0'` (missing).

### Transfer

- **Copy** or **Move** modes
- Three conflict strategies: **Skip**, **Overwrite**, **Auto-Rename** (e.g. `clip_1.mp4`)
- Rewrites originating OP parameters to relative paths after transfer (toggle: `Modify Params`)
- Output organised into category folders: `Image/`, `Movie/`, `Audio/`, `Geo/`, `Data/`, `Font/`, `Component/`
- File size calculator — total dependency size reported before commit

### Safety

- **Undo** — in-panel single-step reversal of the last consolidation
- **Replayable relocation log** — every successful CONSOLIDATE writes `<project>.relocation_<TS>.py` next to the `.toe`. Run `python <file>.py` from any terminal to reverse a transfer, even after TD is closed
- **Safety `.toe` backup** toggle — saves `<project>.original.toe` once before any change

### Panel UI

- Three-row layout: FIND / CONSOLIDATE / UNDO action row · SAVE / LOAD / RESET preset+reset row · config grid (Scan, Mode, Conflict, Safety, Exclusions)
- Exclusion presets — one-click toggles for Images, Video, Audio, 3D/Geo, Data, TOX
- Per-field reset buttons (`×`) next to *Exclude Types* and *Exclude COMPs*; global `RESET` for all settings
- **COPY PATHS** button — copies all found absolute paths to clipboard, one per line
- Hover tooltips on every control (shown in the status bar)
- Live status bar — conflict mode, file count, last action timestamp
- Structured log output — marker legend (`+` on disk, `⚠` missing), column header (`name.filetype  [Node]  node name  path to file`), aligned divider
- Filename middle-truncation past 30 chars; OP short-name middle-truncation past 20 chars

### Presets

- Save / load all operational parameters to JSON
- Per-project smart defaults: preset name auto-resolves to `preset_<project_stem>` and folder to `~/Documents/Derivative/tdCollectProject`
- Auto-increment on filename collision — `preset_X.json` becomes `preset_X_1.json`, `_2`, etc.
- Forward-compatible loader — unknown keys are skipped with a log warning
- JSON also captures the current log content under a `log` key

### Project rename

- Project + component renamed from `CollectTDProject` to `tdCollectProject`. Release asset is now `tdCollectProject.tox`; root COMP path is `/project1/tdCollectProject`.
- GitHub repository renamed to `LMXtinker/tdCollectProject`. The old URL auto-redirects; update local clones with `git remote set-url origin https://github.com/LMXtinker/tdCollectProject.git`.

### Internals

- Single `.tox`, no external Python packages or dependencies
- Self-contained `ConsolidateExt` extension class (promoted as `parent.tool`)
- TouchDesigner 2025 (any build)
- Network annotations describe each functional block

### Acknowledgments

Built on top of [TD-File-Collector](https://github.com/mourendxu/TD-File-Collector) by mourendxu (GPL-3.0). The core file-scanning and parameter-rewriting approach originates from that project.
