# Contributing to CollectTDProject

## Development Setup

The development source is `CollectTDProject_dev.toe` (at repo root). Open this in TouchDesigner to work on the component. When ready to release, export the inner COMP as a `.tox` via right-click → **Save Component**, saving to `CollectTDProject.tox` at repo root.

### Actual Repository Structure

```
CollectTDProject/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── CollectTDProject.tox        # Distributable component — commit this
├── CollectTDProject_dev.toe    # Dev source — open this to make changes
├── screenshots/
│   ├── 01_panel_ui.png
│   ├── 02_demo_network.jpg     # Demo network with one node per file type
│   └── 03_find_results.png     # Find action output
├── scripts/
│   └── build_panel.py          # Panel layout helper
└── instagram_icon.png
```

> `Backup/`, `TDImportCache/`, runtime output folders (`Audio/`, `Data/`, etc.) are gitignored.

---

### Internal Architecture

The component is a single `containerCOMP` with a Python extension class (`Helpers` textDAT, promoted via `extension1`). Two CHOP Execute scripts drive the main logic:

| Script | Role |
|--------|------|
| `scanning_chopExec` | Recursive scan — evaluates all string pars, writes results to `Files_Table`, reports total file size |
| `chopexec1` | Reads `Files_Table`, runs file transfer into categorised subfolders, rewrites OP parameters to relative paths |

The extension class (`CollectExt`) provides shared helpers: `Write_log()`, `Get_exclude_list()`, `Get_scan_root()`, `Record_undo_par()`, `Record_undo_file()`, `Undo_last_consolidate()`, `Refresh_status()`, etc.

Access from any script inside the component via `me.parent()` (resolves to the root COMP with the promoted extension).

### Extension Categories Map (`chopexec1` → `Dirs` dict)

The consolidator maps file extensions to output subfolder names. If a scanned extension is not in `Dirs`, it is logged as `unknown extension` and skipped. Currently mapped:

| Folder | Extensions |
|--------|-----------|
| `Image/` | jpg jpeg png gif bmp tif tiff exr hdr tga dds svg pic |
| `Movie/` | mp4 mov avi wmv mpeg mpg mkv |
| `Audio/` | mp3 wav aiff aif ogg flac |
| `Font/` | ttc ttf otf |
| `Geo/` | fbx obj abc dae usd usda usdc usdz ply stl dxf |
| `Data/` | txt json xml csv dat py yaml yml toml glsl frag vert hlsl |
| `Component/` | tox |

**When adding a new extension**: add it to `Dirs` in `chopexec1` AND to the relevant preset list in `panel_callbacks` (`_PRESETS`).

### Panel Dispatch System

All button interactions are handled by a single `panelexecuteDAT` at `ui/panel_callbacks`. It watches the entire `ui` subtree (`par.panels = '..'`). Dispatch is name-based via `panelValue.owner.name`:

- `_TOGGLES` — binary toggles (Modifyparams, Ignorepalettecomps)
- `_INDEXED` — segmented buttons with numeric suffix (seg_mode_0/1, seg_conflict_0/1/2)
- `_PRESETS` — exclusion preset toggles (preset_img, preset_vid, etc.)
- Direct name match — main action buttons (btn_find, btn_consolidate, btn_undo, btn_clear, btn_instagram)

Rollover events (`rolloveron` / `rolloveroff`) are handled in `onValueChange`. Tooltip text per element is defined in the `_TOOLTIP` dict in the same DAT. Active tooltip is written to `ui/tooltip` textDAT; the status bar reads it via expression.

---

### Code Rules

1. **No `print()` for user feedback.** Use `tool.Write_log(message)` — `tool` is `me.parent()`.
2. **No `os.rename()` for cross-drive moves.** Use `shutil.move()` or `os.replace()` as already implemented.
3. **Wrap all parameter evaluation in `try/except`.** TD parameters frequently contain broken expressions.
4. **Log message format:** use the standard prefixes already in use: `✓` success, `✗` error/skip, `·` neutral, `+` created, `→` transferred.
5. **Do not break the `me.parent().op('Log')` reference.** The `Write_log()` function depends on the relative path to the `Log` DAT.
6. **Extensions must be added to both `Dirs` AND `_PRESETS`** to be fully supported (see above).

---

## Versioning Strategy

`.tox` files are binary — Git diffs are not meaningful. Use this workflow:

### Tagging Releases

Use [Semantic Versioning](https://semver.org/): `vMAJOR.MINOR.PATCH`

- **PATCH** (`v1.0.1`): Bug fixes, no behaviour change.
- **MINOR** (`v1.1.0`): New features, backwards-compatible.
- **MAJOR** (`v2.0.0`): Breaking changes (parameter renames, removed functionality).

### Release Workflow

1. Make changes in `CollectTDProject_dev.toe`, test thoroughly.
2. Update `par.Version` on the component's About page to the new version string.
3. Update `par.Toxsavebuild` to the current TD build (`app.build`).
4. Export the component: right-click COMP → **Save Component** → `CollectTDProject.tox`.
5. Commit: `git add CollectTDProject.tox && git commit -m "release: vX.Y.Z - description"`
6. Tag: `git tag vX.Y.Z`
7. Push: `git push && git push --tags`
8. Create a GitHub Release from the tag, attach `CollectTDProject.tox` as a release asset.

---

## Reporting Bugs

Open a GitHub Issue. Include:

- TouchDesigner version (`Help → About`)
- Operating system
- A description of the project structure (rough network layout, file types referenced)
- The full log output from the component after the failure

---

## License & Attribution

This project is licensed under **GPL-3.0**. It is a derivative of [TD-File-Collector](https://github.com/mourendxu/TD-File-Collector) by mourendxu (GPL-3.0). All contributions must be compatible with GPL-3.0.
