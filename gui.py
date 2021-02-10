from appJar import gui 
import settings
    
def menuPress(a):
    print("Menu clicked:", a)

with gui("mednboy & chum chum", "400x250") as app:
    # Toolbar
    # > File
    app.createMenu("File")
    
    app.addMenuItem("File", "Open...", menuPress)
    app.addMenuItem("File", "Save...", menuPress)

    app.addMenuSeparator("File")

    app.addSubMenu("File", "Recent Files")
    for game in settings.recentROMs:
        app.addMenuItem("Recent Files",
                        game['rom'],
                        menuPress
                        )

    app.addMenuSeparator("File")

    app.addMenuItem("File", "Close", app.stop)
    
    # > Help
    app.addMenuList("Help", ["About..."], menuPress)
    
    app.label("TengokuSoundTool")
    
    # for SOME FUCKING REASON, the spinbox's controls are inverted https://github.com/jarvisteach/appJar/issues/582
    # this is a workaround, since a release hasn't been made since this was "fixed"
    app.addLabelSpinBox("Entry", list(reversed(range(0,962)))) # 962 = 0x5A30 / 0x18
    
    app.addLabelSpinBox("Length", list(reversed(range(0,962))))
    app.addLabelSpinBox("Sample Rate", list(reversed(range(0,962))))
    app.addLabelSpinBox("Pitch", list(reversed(range(0,962))))
    app.addLabelSpinBox("Loop Start", list(reversed(range(0,962))))
    app.addLabelSpinBox("Loop End", list(reversed(range(0,962))))
    app.addLabelSpinBox("Start Pointer", list(reversed(range(0,962))))
    
