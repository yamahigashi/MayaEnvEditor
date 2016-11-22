# -*- coding: utf-8 -*-
from functools import partial

import maya.utils as utils
import maya.mel as mel
import maya.cmds as cmds


import mayaenveditor as editor


def create_menu():
    cmd = '''
    global string $gMainFileMenu; // Retrieve the menu name
    buildViewMenu("MayaWindow|mainWindowMenu");
    buildPreferenceMenu mainOptionsMenu;
    buildSettingsMenu MayaWindow|mainWindowMenu;

    '''

    mel.eval(cmd)
    cmds.menuItem(divider=True)
    cmds.menuItem(label="Edit Maya.env", command=partial(editor.run))


def later():
    """
    Creates mGear menu
    """
    try:
        print "create_menu"
        create_menu()
        print "finish create_menu"

    except Exception as e:
        import traceback
        traceback.print_exc()
        print e


utils.executeDeferred('later()')
