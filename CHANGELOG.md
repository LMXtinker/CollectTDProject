# Changelog

All notable changes are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.3.1] — 2026-05-16 · Beta

### Fixed
- Per-field reset buttons (`×` next to Exclude Types / Exclude COMPs) now fire — the `ui/panel_callbacks` glob pattern was missing `ui/config/*/btn_reset_*`, so the dispatcher never received the click events. Global `RESET` and all other buttons were unaffected.
- `CONTRIBUTING.md` bug-report instructions corrected: `COPY PATHS` copies the found absolute file paths, **not** the log content (right-click → Copy on the `Log` DAT for the log).

### Removed
- Internal `text1` debug DAT (`print(parent.par.Movefiles)`, unreferenced).
- Internal `build_panel` rebuild script (~324 lines). Its embedded `PANEL_CALLBACKS_SOURCE` was stuck at the 0.1.x dispatcher and would have silently downgraded the panel if run. Component is now authored live per `CONTRIBUTING.md` — no build step.

## [0.3.0] — 2026-05-08 · Beta

### Added
- Broken-path detection: ⚠ marker flags missing source files in the scan log
- Replayable relocation log: `<project>.relocation_<TS>.py` written after each CONSOLIDATE — run `python <file>.py` from any terminal to reverse a transfer, even after TD is closed
- Scan log shows OP short name and family type (TOP / CHOP / SOP / COMP / DAT) per entry, plus full path
- **COPY PATHS** button next to CLEAR — copies all found absolute paths to system clipboard, one per line
- Structured log output: marker legend, column header (`name.filetype  [Node]  node name  path to file`), aligned divider
- Filename middle-truncation past 30 chars (`Gemini_Generat...06zlo506z.png`)
- OP short-name middle-truncation past 20 chars
- Preset save/load with per-project smart defaults and auto-increment on filename collision
- Preset JSON now also captures the current log content under a `log` key
- Safety `.toe` backup toggle: saves `<project>.original.toe` once before any change
- Per-field reset buttons (`×`) for Types and COMPs; global `RESET` for all settings
- Hover tooltips on every UI control (shown in the status bar)

### Changed
- Panel UI redesigned and compacted
- Exclusion palette toggle relocated to Safety row
- Instagram icon moved to `assets/` with relative path reference (was absolute, leaked username)
- Version scheme changed to 0.x.y (pre-1.0 beta)
- TD version requirement relaxed to TouchDesigner 2025 (any build)
- Network annotations refreshed to reflect current architecture
- `scripts/` and `tests/` now gitignored (kept local, not in public repo)
- `CONTRIBUTING.md` slimmed to essentials

## [0.2.0]

- Reset buttons, preset save/load, `.toe` safety backup

## [0.1.0]

- Panel dispatch fix, tooltip system, editable inputs, demo fixture
