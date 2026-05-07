# Changelog

All notable changes are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.3.0] — 2026-05-07 · Beta

### Added
- Broken-path detection: ⚠ marker flags missing source files in the scan log
- Replayable relocation log: `<project>.relocation_<TS>.py` written after each CONSOLIDATE — run `python <file>.py` from any terminal to reverse a transfer, even after TD is closed
- Scan log shows OP short name and family type (TOP / CHOP / SOP / COMP / DAT) per entry
- **COPY PATHS** button next to CLEAR — copies all found absolute paths to system clipboard, one per line
- Preset save/load with per-project smart defaults and auto-increment on filename collision
- Safety `.toe` backup toggle: saves `<project>.original.toe` once before any change
- Per-field reset buttons (`×`) for Types and COMPs; global `RESET` for all settings
- Hover tooltips on every UI control (shown in the status bar)

### Changed
- Panel UI redesigned and compacted
- Exclusion palette toggle relocated to Safety row
- Version scheme changed to 0.x.y (pre-1.0 beta)
- TD version requirement relaxed to TouchDesigner 2025 (any build)
- Network annotations refreshed to reflect current architecture

## [0.2.0]

- Reset buttons, preset save/load, `.toe` safety backup

## [0.1.0]

- Panel dispatch fix, tooltip system, editable inputs, demo fixture
