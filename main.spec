# -*- mode: python ; coding: utf-8 -*-

# Añade tus archivos aquí

a = Analysis(
    ['main.py'],
    pathex=['D:\Master_AnaliticaDatos\SegundoCutri\Estadistica Analitica\Proba_analitica\GUI_python'],
    binaries=[],
    datas=[('./images/logo.png', './images'), 
           ('./images/utp_color.png', './images'), 
           ('./images/bayes_icon_w.png', './images'), 
           ('./images/bin_icon_w.png', './images'), 
           ('./images/expo_icon_w.png', './images'), 
           ('./images/graphic_icon_w.png', './images'), 
           ('./images/menu.png', './images'), 

           ('./images/normal_icon_w.png', './images'), 
           ('./images/poison_icon_w.png', './images'), 
           ('./images/poison_range_icon_w.png', './images'), 
           ('./images/icon.ico', './images'), 

           ('./images/bin_icon_w.png', './images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app_icon.ico'],
)
