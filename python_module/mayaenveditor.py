# -*- coding: utf-8 -*-

import os
import re
from functools import partial

import maya.cmds as cmds
import maya.OpenMayaUI as omui
# from maya.app.general.mayaMixin import MayaQDockWidget

try:
    from PySide import QtGui, QtCore
    import PySide.QtGui as QtWidgets
    from shiboken import wrapInstance

except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
    from shiboken2 import wrapInstance

except ImportError:
    from PyQt4 import QtGui
    from PyQt4 import QtCore
    import PyQt4.QtGui as QtWidgets
    from sip import wrapinstance as wrapInstance


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 568)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(560, 560))
        self.editorGroupBox = QtGui.QGroupBox(Form)
        self.editorGroupBox.setGeometry(QtCore.QRect(10, 10, 531, 535))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editorGroupBox.sizePolicy().hasHeightForWidth())
        self.editorGroupBox.setSizePolicy(sizePolicy)
        self.editorGroupBox.setObjectName("editorGroupBox")
        self.layoutWidget = QtGui.QWidget(self.editorGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 511, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.variable_verticalLayout_1 = QtGui.QVBoxLayout()
        self.variable_verticalLayout_1.setObjectName("variable_verticalLayout_1")
        self.listBox = QtGui.QListWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listBox.sizePolicy().hasHeightForWidth())
        self.listBox.setSizePolicy(sizePolicy)
        self.listBox.setDragEnabled(True)
        self.listBox.setDragDropOverwriteMode(False)
        self.listBox.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.listBox.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listBox.setAlternatingRowColors(True)
        self.listBox.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listBox.setMovement(QtGui.QListView.Snap)
        self.listBox.setResizeMode(QtGui.QListView.Fixed)
        self.listBox.setSelectionRectVisible(False)
        self.listBox.setObjectName("listBox")
        self.variable_verticalLayout_1.addWidget(self.listBox)
        self.gridLayout.addLayout(self.variable_verticalLayout_1, 0, 0, 1, 1)
        self.variable_verticalLayout_2 = QtGui.QVBoxLayout()
        self.variable_verticalLayout_2.setObjectName("variable_verticalLayout_2")
        self.addButton = QtGui.QPushButton(self.layoutWidget)
        self.addButton.setObjectName("addButton")
        self.variable_verticalLayout_2.addWidget(self.addButton)
        self.editButton = QtGui.QPushButton(self.layoutWidget)
        self.editButton.setObjectName("editButton")
        self.variable_verticalLayout_2.addWidget(self.editButton)
        self.removeButton = QtGui.QPushButton(self.layoutWidget)
        self.removeButton.setObjectName("removeButton")
        self.variable_verticalLayout_2.addWidget(self.removeButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.variable_verticalLayout_2.addItem(spacerItem)
        self.upButton = QtGui.QPushButton(self.layoutWidget)
        self.upButton.setObjectName("upButton")
        self.variable_verticalLayout_2.addWidget(self.upButton)
        self.downButton = QtGui.QPushButton(self.layoutWidget)
        self.downButton.setObjectName("downButton")
        self.variable_verticalLayout_2.addWidget(self.downButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.variable_verticalLayout_2.addItem(spacerItem1)
        self.variable_verticalLayout_2.setStretch(3, 1)
        self.variable_verticalLayout_2.setStretch(6, 1)
        self.gridLayout.addLayout(self.variable_verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.editorGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 444, 511, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ok_pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.horizontalLayout.addWidget(self.ok_pushButton)
        self.cancel_pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.editorGroupBox.setTitle(QtGui.QApplication.translate("Form", "Maya Module Path Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Form", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("Form", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("Form", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setText(QtGui.QApplication.translate("Form", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downButton.setText(QtGui.QApplication.translate("Form", "Move Down", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_pushButton.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_pushButton.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))


class StringListEditor(QtWidgets.QDialog, Ui_Form):

    def __init__(self, parent=None, list=[]):
        super(StringListEditor, self).__init__(parent)
        self.setupUi(self)
        self.setList(list)

        self.addCaption = "Add ..."
        self.addLabel = "Add ..."
        self.editCaption = "Edit ..."
        self.editLabel = "Edit ..."
        self.ask = True

    def setTexts(self, addCaption, addLabel, editCaption, editLabel):
        self.addCaption = addCaption
        self.addLabel = addLabel
        self.editCaption = editCaption
        if editLabel.isEmpty():
            self.editLabel = addLabel
        else:
            self.editLabel = editLabel

    def askBeforeRemoving(self):
        return self.ask

    def setAskBeforeRemoving(self, a):
        self.ask = a

    def allowDuplicates(self):
        return self.duplicatesOk

    def setAllowDuplicates(self, allow):
        self.duplicatesOk = allow

    def setList(self, list):
        self.listBox.clear()
        self.listBox.addItems(list)

        fm = self.listBox.fontMetrics()
        width = 0
        for item in list:
            w = fm.width(item)
            if w > width:
                width = w

        if self.listBox.verticalScrollBar():
            width += self.listBox.verticalScrollBar().width()

        # TODO: consider screen size
        # self.listBox.setMinimumWidth(width)
        # QtCore.qMin(width, qApp.desktop().screenGeometry().width() * 4 / 5))

        self.updateButtons()

    def refreshList(self):
        # TODO: fixme...
        item = self.listBox.currentItem()
        self.listBox.scrollToItem(item)

    def addString(self, *args):

        dlg = QtGui.QInputDialog()
        dlg.setInputMode(QtGui.QInputDialog.TextInput)
        txt, ok = dlg.getText(self, self.addCaption, self.addLabel)  # ,
        txt = txt.rstrip('\\')
        txt = txt.rstrip('/')
        # QtGui.QLineEdit.Normal, self.listBox.currentItem().text())

        if ok and (txt is not None):
            # if (not self.duplicatesOk and self.listBox.findItem(txt, CaseSensitive | ExactMatch)):
            #     return

            self.listBox.addItem(txt)
            self.listBox.setCurrentRow(self.listBox.count() - 1)
            self.listBox.clearSelection()
            self.refreshList()
            # self.updateButtons()

    def editString(self, *args):
        currentItem = self.listBox.currentItem()
        original = currentItem.text()

        if original is not None:
            txt, ok = QtGui.QInputDialog.getText(self, self.editCaption, self.editLabel,
                                                 QtGui.QLineEdit.Normal, original)

            if ok and (txt is not None):
                # if (not self.duplicatesOk and self.listBox.findItem(txt, CaseSensitive | ExactMatch)):
                #     return
                self.listBox.currentItem().setText(txt)
                self.refreshList()
                self.updateButtons()

            else:
                self.addString()

    def removeString(self, *args):
        currentItem = self.listBox.currentItem()
        original = currentItem.text()

        if original is not None and (self.ask and not self.confirmToRemove(original)):
            return

        item = self.listBox.currentItem()
        self.listBox.takeItem(self.listBox.row(item))
        self.refreshList()
        self.updateButtons()

    def confirmToRemove(self, txt):
        question = QtGui.QMessageBox.question(
            self, "Remove",
            "Remove '{0}'?".format(txt),
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.No)

        return question == QtGui.QMessageBox.Yes

    def moveUp(self, *args):
        currentItem = self.listBox.currentItem()
        currentIndex = self.listBox.row(currentItem)

        if (currentIndex > 0):

            prev = self.listBox.item(currentIndex - 1)
            prevIndex = self.listBox.row(prev)

            temp = self.listBox.takeItem(prevIndex)
            self.listBox.insertItem(currentIndex, temp)
            self.listBox.insertItem(prevIndex, currentItem)
            self.listBox.setCurrentRow(currentIndex - 1)
            self.refreshList()
            self.updateButtons()

    def moveDown(self, *args):
        currentItem = self.listBox.currentItem()
        currentIndex = self.listBox.row(currentItem)

        if (currentIndex < self.listBox.count() - 1):

            next = self.listBox.item(currentIndex + 1)
            nextIndex = self.listBox.row(next)

            temp = self.listBox.takeItem(nextIndex)
            self.listBox.insertItem(currentIndex, temp)
            self.listBox.insertItem(nextIndex, currentItem)
            self.listBox.setCurrentRow(currentIndex + 1)
            self.refreshList()
            self.updateButtons()

    def updateButtons(self):
        currentItem = self.listBox.currentItem()
        if currentItem:
            hasItems = self.listBox.count() > 0
            self.editButton.setEnabled(hasItems)
            self.removeButton.setEnabled(hasItems)
            index = self.listBox.row(self.listBox.currentItem())
            self.upButton.setEnabled(hasItems and index > 0)
            self.downButton.setEnabled(hasItems and index < int(self.listBox.count()) - 1)


class EnvironmentVariableEditorTab(StringListEditor):

    def __init__(self, parent=None, envvarpath="", envvarkey=""):
        self.envvarkey = envvarkey
        self.envvarpath = envvarpath

        list = self.load_variable_value()
        super(EnvironmentVariableEditorTab, self).__init__(parent, list=list)
        self.editorGroupBox.setTitle(
            QtGui.QApplication.translate(
                "Form", "Edit environment variable '{0}'".format(envvarkey), None, QtGui.QApplication.UnicodeUTF8))

    def load_variable_value(self):

        with open(self.envvarpath, 'r') as f:
            x = f.read()
            m = re.search(r"{0} *= *(.*)".format(self.envvarkey), x)

            if m:
                list = m.group(1).split(os.pathsep)
                list = map(lambda x: x.strip('"'), list)
            else:
                list = []

        return list

    def create_connections(self, parent):
        self.cancel_pushButton.clicked.connect(parent.cancel)
        self.ok_pushButton.clicked.connect(self.save)

        self.addButton.clicked.connect(partial(self.addString, self.listBox))
        self.removeButton.clicked.connect(partial(self.removeString, self.listBox))
        self.editButton.clicked.connect(partial(self.editString, self.listBox))
        self.upButton.clicked.connect(partial(self.moveUp, self.listBox))
        self.downButton.clicked.connect(partial(self.moveDown, self.listBox))
        self.listBox.itemDoubleClicked.connect(self.editString)
        self.listBox.itemSelectionChanged.connect(self.updateButtons)

        # TODO:
        # fix selection after draganddrop fired

    def save(self):
        items = []
        for i in range(self.listBox.count()):
            item = self.listBox.item(i).text()
            item = '"{0}"'.format(item) if " " in item and '"' not in item else item
            # item = re.escape(item)
            item = item.replace("\\", "\\\\")
            items.append(item)
        var = os.pathsep.join(items)

        with open(self.envvarpath, 'r') as f:
            body = f.read()

        with open(self.envvarpath, 'w+') as f:
            try:
                pat = "{0}\s*=\s*.*".format(self.envvarkey)
                repl = "{0}={1}".format(self.envvarkey, var)
                res = re.sub(pat, repl, body)
                f.write(res)

                QtGui.QMessageBox.question(
                    self, "Save succece",
                    "save file at '{0}'.".format(self.envvarpath),
                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default)

            except Exception as e:
                f.write(body)
                import traceback
                traceback.print_exc()
                raise e

        os.environ[self.envvarkey] = var
        if "MAYA_MODULE_PATH" in self.envvarkey:
            # CAUTION: this does not mean that environment variables in the
            #   module definition file are not re-evaluated
            cmds.loadModule(allModules=True)


class MayaEnvEditor(QtWidgets.QDialog):
    valueChanged = QtCore.Signal(int)
    TITLE = "Edit environment variable"

    def __init__(self, parent=None):
        self.mayaMainWindow = parent
        self.toolName = self.TITLE
        # Delete old instances of the componet settings window.
        self.deleteInstances()

        super(MayaEnvEditor, self).__init__(parent)
        self.envvarpath = self.search_mayaenv_path()

        self.create_tabs()
        self.setup_window()

    def search_mayaenv_path(self):
        usd = cmds.internalVar(usd=True)
        ud = '/'.join(usd.split('/')[0:-2])
        p = os.path.join(ud, 'Maya.env')

        if not os.path.exists(p):
            # searching path for environments other than English UI
            ud = '/'.join(usd.split('/')[0:-3])
            p = os.path.join(ud, 'Maya.env')
            if not os.path.exists(p):
                QtGui.QMessageBox.question(
                    self, "Error",
                    "Maya.env is not detected (at: {0}), check your installation or call your system administrator.".format(p),
                    QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default)
                raise "Maya.env is not detected"

        return p

    def search_env_vars(self):
        with open(self.envvarpath, 'r') as f:
            x = f.read()
            m = re.findall(r"(\w+) *= *(.*)", x)

        return m

    def generate_tab_label(self, full):
        x = " ".join(full.split("_")).lower()
        return x

    def create_tabs(self):
        self.tabWidgets = []

        def __inner(index, key):
            tab = EnvironmentVariableEditorTab(envvarpath=self.envvarpath, envvarkey=key)
            self.tabWidgets.append(tab)
            self.tabs.insertTab(index, tab, self.generate_tab_label(key))
            self.tabWidgets.append(tab)
            tab.create_connections(self)

            return tab

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setObjectName("tabs")

        self.mainSettingsTab = __inner(0, "MAYA_MODULE_PATH")

        envvars = self.search_env_vars()
        for i, entry in enumerate(envvars):
            k, v = entry[0], entry[1]
            if "MAYA_MODULE_PATH" not in k:
                __inner(i + 1, k)

    def setup_window(self):
        self.setObjectName(self.toolName)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle(self.TITLE)

        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.addWidget(self.tabs)
        self.settings_layout.setStretch(1, 1)

        self.setLayout(self.settings_layout)

        self.resize(self.width(), self.height())

    def eventFilter(self, sender, event):
        return True

    def dockCloseEventTriggered(self):
        self.deleteInstances()

    def cancel(self):
        # TODO: set dirty and notify on close
        self.close()
        self.deleteInstances()

    def closeWindow(self):
        self.close()
        self.deleteInstances()

    def deleteInstances(self):
        for obj in self.mayaMainWindow.children():
            # if type(obj) == MayaQDockWidget or type(obj) == MayaEnvEditor:
            if type(obj) == QtWidgets.QDialog or "MayaEnvEditor" in str(type(obj)):
                if obj.objectName() == self.toolName:
                    try:
                        self.mayaMainWindow.removeDockWidget(obj)
                    except TypeError:
                        pass
                    obj.setParent(None)
                    obj.deleteLater()


def run(*args, **kwargs):
    try:
        main_window_ptr = omui.MQtUtil.mainWindow()
        main_window = wrapInstance(long(main_window_ptr), QtWidgets.QMainWindow)
        dialog = MayaEnvEditor(main_window)
        dialog.show()

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e


if __name__ == '__main__':
    run()
