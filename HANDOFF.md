# CollectTDProject — Handoff

> For the next Claude Code instance picking this up.

---

## Repo

https://github.com/LMXtinker/CollectTDProject  
Branch: `master` (direct commits, no PR workflow yet)  
Latest commit: `355616e` — Fix glsl consolidation + add panel tooltip system

---

## What Was Done This Session

### Bug fixes (committed ✅)

1. **`glsl` (and `py`, `yaml`, `yml`, `toml`, `frag`, `vert`, `hlsl`) were missing from the consolidator's `Dirs` map** in `chopexec1`. They were *found* by the scanner but logged as `unknown extension` and skipped during consolidation. Fixed by adding them to the `Dirs` dict → `Data/` folder.

2. **Config UI buttons were silently not dispatching.** `panel_callbacks` had `par.panels = 'actions'`, watching only the top action bar. All config buttons (exclusion presets, Copy/Move, Skip/Overwrite/Rename) were never firing. Fixed by changing `par.panels = '..'` (full `ui` subtree).

### New features (committed ✅)

3. **Hover tooltip system.** When the user hovers any interactive element in the panel UI, description text appears in the status bar:
   - `ui/tooltip` textDAT stores the active tooltip text (empty = no hover)
   - `ui/status.par.text.expr` = `me.parent().op('tooltip').text or parent.tool.Status_line()`
   - `panel_callbacks.par.valuechange = True` — `onValueChange` writes to `ui/tooltip` on `rolloveron`/`rolloveroff` events
   - `_TOOLTIP` dict in `panel_callbacks` covers all 18 interactive elements

### Screenshots updated (committed ✅)

- `screenshots/02_demo_network.jpg` — one node per supported file type (moviefileinTOP for .exr and .mp4, audiofileinCHOP for .wav, fileinSOP for .fbx, textTOP for .ttf, textDAT×2 for .json and .glsl, baseCOMP with externaltox for .tox), viewers enabled, errors/warnings visible
- `screenshots/03_find_results.png` — Find output showing 7 files found across all types

---

## What Still Needs Doing

### 1. `demo_broken_paths.tox` — NEEDS TD MCP CONNECTION

The demo network was created live in TD during this session but was NOT saved as a standalone `.tox`. The user wants it saved to the repo as a test fixture.

**What the demo COMP should contain:**
- 8 nodes, one per supported file type:
  - `img_hero` — `moviefileinTOP`, `par.file = 'assets/hero.exr'`
  - `vid_background` — `moviefileinTOP`, `par.file = 'assets/loop.mp4'`
  - `aud_soundtrack` — `audiofileinCHOP`, `par.file = 'assets/soundtrack.wav'`
  - `geo_scene` — `fileinSOP`, `par.file = 'assets/scene.fbx'`
  - `fnt_title` — `textTOP`, `par.fontfile = 'assets/custom.ttf'`
  - `dat_config` — `textDAT`, `par.file = 'assets/settings.json'`, `par.syncfile = True`
  - `dat_shader` — `textDAT`, `par.file = 'assets/noise.glsl'`, `par.syncfile = True`
  - `tox_module` — `baseCOMP`, `par.externaltox = 'assets/module.tox'`, `par.enableexternaltox = True`
- All with `op.viewer = True`
- Custom page "Demo" with a pulse par `Forcecook` (label "Force Cook Children")
- `force_cook_callbacks` `parameterexecuteDAT` inside the COMP watching `..` for `Forcecook` pulse, force-cooks all children on pulse

**Use relative paths** (e.g. `assets/hero.exr`) instead of absolute paths so the broken-path state is self-contained and portable.

**Save location:** `tests/demo_broken_paths.tox` in the repo.

**To create:** Reconnect the TD MCP server (`mcp__twozero_td__*` tools), navigate to `/project1`, run the creation script, then `op('/project1/demo_broken_paths').save('C:/Users/.../CONSOLIDATE_FILES/tests/demo_broken_paths.tox')`.

### 2. Screenshots retake after `demo_broken_paths.tox` is created

After saving the demo TOX, retake:
- `02_demo_network.jpg` — using the proper TOX-based demo loaded fresh (to show clean state)

### 3. Version bump + new GitHub release

Changes since v1.0.0 are significant enough for a v1.1.0:
- glsl/data extension fix
- tooltip system
- config button dispatch fix

Steps:
1. In TD: set `CollectTDProject.par.Version = '1.1.0'` and `par.Toxsavebuild = app.build`
2. Save TOX: `op('/project1/CollectTDProject').save('...CollectTDProject.tox')`
3. Commit: `git add CollectTDProject.tox && git commit -m "release: v1.1.0 - ..."`
4. Tag + push: `git tag v1.1.0 && git push && git push --tags`
5. Create GitHub Release: `gh release create v1.1.0 CollectTDProject.tox --title "v1.1.0" --notes "..."`

### 4. `tests/` folder scaffold (optional)

Add a `tests/` folder with:
- `demo_broken_paths.tox` (see above)
- A `README.md` explaining how to use it for manual testing

---

## Current Repo State

| File | Status |
|------|--------|
| `CollectTDProject.tox` | Current, includes glsl fix + tooltip system |
| `CollectTDProject_dev.toe` | Dev source (`.toe` files are gitignored from tracking) |
| `README.md` | Current |
| `CONTRIBUTING.md` | Updated this session — now matches actual structure |
| `screenshots/` | Current — 3 screenshots |
| `tests/` | Does not exist yet |

---

## TD MCP Connection

The `mcp__twozero_td__*` tools connect to a local MCP server running inside TouchDesigner (port ~61840). If they appear in the deferred tools list but `ToolSearch` returns "no match" or they throw errors, the MCP server has disconnected. Ask the user to restart TD or reconnect the MCP server from the TD palette.

When connected, TD instance info is available via `mcp__twozero_td__td_list_instances`. The active project is `CollectTDProject_dev.toe`.

---

## Key Files to Read on Start

1. `CollectTDProject.tox` — binary, don't edit directly
2. `CONTRIBUTING.md` — architecture, dispatch system, extension map
3. `README.md` — user-facing docs, screenshots
4. Inside TD (via MCP): `op('/project1/CollectTDProject/chopexec1').text` — consolidator with Dirs map  
5. Inside TD: `op('/project1/CollectTDProject/ui/panel_callbacks').text` — full dispatch + tooltip logic  
6. Inside TD: `op('/project1/CollectTDProject/scanning_chopExec').text` — scanner logic
