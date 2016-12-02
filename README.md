Environment variable editor for maya.env
========================================

This is an editor for editing maya.env from Maya. It is mainly for editing `MAYA_MODULE_PATH`.
It is similar to the environment variable editor of Windows 10.
When activated, a tab is created according to the key name described in maya.env,
and the value of the environment variable corresponding to the key name is edited
in that tab.

![sample image](https://github.com/yamahigashi/MayaEnvEditor/blob/master/sample.png)

Usage:
======

1. Puts [MayaEnvEditor/python_module/mayaenveditor.py](https://raw.githubusercontent.com/yamahigashi/MayaEnvEditor/master/python_module/mayaenveditor.py) into shelf or Script Editor
2. execute it.

or


1. git clone or Download this repo
2. add its folder to `MAYA_MODULE_PATH` in the `maya.env`

 ```maya.env
 MAYA_MODULE_PATH=C:\maya\maya_modules\MayaEnvEditor
 ```
 
3. Menu item appers in Main menu Windows > Settings/Preferences > Edit Maya.env
