# create_demo.py
# Run this in TD's textport: exec(open('C:/Users/dikan/OneDrive/Touchdesigner/___TOX___/CONSOLIDATE_FILES/tests/create_demo.py').read())
# Or paste directly into a textport window.
# Creates /project1/demo_broken_paths and saves it as tests/demo_broken_paths.tox

SAVE_PATH = 'C:/Users/dikan/OneDrive/Touchdesigner/___TOX___/CONSOLIDATE_FILES/tests/demo_broken_paths.tox'

# ── 1. Create or clear the container ─────────────────────────────────────────
root = op('/project1')
existing = root.op('demo_broken_paths')
if existing:
    existing.destroy()

demo = root.create(containerCOMP, 'demo_broken_paths')
demo.nodeX = 0
demo.nodeY = 0

# ── 2. Create the 8 asset-reference nodes ────────────────────────────────────
nodes = [
    ('img_hero',       'moviefileinTOP',  'file',        'assets/hero.exr'),
    ('vid_background', 'moviefileinTOP',  'file',        'assets/loop.mp4'),
    ('aud_soundtrack', 'audiofileinCHOP', 'file',        'assets/soundtrack.wav'),
    ('geo_scene',      'fileinSOP',       'file',        'assets/scene.fbx'),
    ('fnt_title',      'textTOP',         'fontfile',    'assets/custom.ttf'),
    ('dat_config',     'textDAT',         'file',        'assets/settings.json'),
    ('dat_shader',     'textDAT',         'file',        'assets/noise.glsl'),
    ('tox_module',     'baseCOMP',        'externaltox', 'assets/module.tox'),
]

for i, (name, optype, param, path) in enumerate(nodes):
    n = demo.create(eval(optype), name)
    n.nodeX = (i % 4) * 200 - 300
    n.nodeY = -(i // 4) * 150
    n.viewer = True
    try:
        getattr(n.par, param).val = path
    except Exception as e:
        print(f'  Warning: could not set {name}.par.{param}: {e}')

# Extra settings for specific node types
demo.op('dat_config').par.syncfile = True
demo.op('dat_shader').par.syncfile = True
tox_node = demo.op('tox_module')
tox_node.par.enableexternaltox = True

# ── 3. Add custom "Demo" page with Forcecook pulse ───────────────────────────
page = demo.appendCustomPage('Demo')
p = page.appendPulse('Forcecook', label='Force Cook Children')

# ── 4. Add force_cook_callbacks parameterexecuteDAT ──────────────────────────
cb = demo.create(parameterexecuteDAT, 'force_cook_callbacks')
cb.par.op = '..'
cb.par.pars = 'Forcecook'
cb.par.onpulse = True
cb.nodeX = 0
cb.nodeY = -350

cb.text = """\
# force_cook_callbacks
def onPulse(par, prev):
    for child in me.parent().children:
        try:
            child.cook(force=True)
        except Exception:
            pass
"""

# ── 5. Save ──────────────────────────────────────────────────────────────────
demo.save(SAVE_PATH)
print(f'Saved: {SAVE_PATH}')
print('demo_broken_paths.tox created successfully.')
