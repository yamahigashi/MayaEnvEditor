# -*- coding: utf-8 -*-
from functools import partial

import maya.utils as utils
import maya.mel as mel
import maya.cmds as cmds


import mayaenveditor


def create_menu():
    cmd = '''
    buildViewMenu MayaWindow|mainWindowMenu;
    buildPreferenceMenu mainOptionsMenu;

    string $parentName = "MayaWindow|mainWindowMenu";
    string $menuItems[] = `menu -q -ia $parentName`;

    for ($i = 0; $i < size($menuItems); $i += 1) {
        string $label = `menuItem -q -label $menuItems[$i]`;
        string $match = `match "Settings" $label`;
        if (0 < size($match)){
            $parentName = $parentName + "|" + $menuItems[$i];
            break;
        }
    }

    buildSettingsMenu $parentName;
    setParent -menu $parentName;
    '''

    mel.eval(cmd)

    cmds.menuItem(divider=True)
    cmds.menuItem(label="Edit Maya.env", command=partial(mayaenveditor.run))


def later():
    """
    Creates mGear menu
    """
    try:
        print "create_menu for mayaenveditor"
        create_menu()
        print "finish create_menu"

    except Exception as e:
        import traceback
        traceback.print_exc()
        print e


utils.executeDeferred('later()')
