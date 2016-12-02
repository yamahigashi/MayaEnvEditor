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
    from PySide.QtGui import QSizePolicy
    from PySide.QtGui import QGroupBox
    from PySide.QtGui import QWidget
    from PySide.QtGui import QVBoxLayout
    from PySide.QtGui import QGridLayout
    from PySide.QtGui import QListWidget
    from PySide.QtGui import QAbstractItemView
    from PySide.QtGui import QListView
    from PySide.QtGui import QPushButton
    from PySide.QtGui import QHBoxLayout
    from PySide.QtGui import QSpacerItem
    from PySide.QtGui import QApplication
    from PySide.QtGui import QMessageBox
    from PySide.QtGui import QInputDialog
    from PySide.QtGui import QLineEdit
    from shiboken import wrapInstance

except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
    from PySide2.QtWidgets import QSizePolicy
    from PySide2.QtWidgets import QGroupBox
    from PySide2.QtWidgets import QWidget

    from PySide2.QtWidgets import QVBoxLayout
    from PySide2.QtWidgets import QGridLayout
    from PySide2.QtWidgets import QListWidget
    from PySide2.QtWidgets import QAbstractItemView
    from PySide2.QtWidgets import QListView
    from PySide2.QtWidgets import QPushButton
    from PySide2.QtWidgets import QHBoxLayout
    from PySide2.QtWidgets import QSpacerItem
    from PySide2.QtWidgets import QApplication
    from PySide2.QtWidgets import QMessageBox
    from PySide2.QtWidgets import QInputDialog
    from PySide2.QtWidgets import QLineEdit

    QApplication.UnicodeUTF8 = 0

    from shiboken2 import wrapInstance

except ImportError:
    from PyQt4 import QtCore
    import PyQt4.QtGui as QtWidgets
    from PyQt4.QtGui import QSizePolicy
    from PyQt4.QtGui import QGroupBox
    from PyQt4.QtGui import QWidget
    from PyQt4.QtGui import QVBoxLayout
    from PyQt4.QtGui import QGridLayout
    from PyQt4.QtGui import QListWidget
    from PyQt4.QtGui import QAbstractItemView
    from PyQt4.QtGui import QListView
    from PyQt4.QtGui import QPushButton
    from PyQt4.QtGui import QHBoxLayout
    from PyQt4.QtGui import QSpacerItem
    from PyQt4.QtGui import QApplication
    from PyQt4.QtGui import QMessageBox
    from PyQt4.QtGui import QInputDialog
    from PyQt4.QtGui import QLineEdit
    from sip import wrapinstance as wrapInstance


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.editorGroupBox = QGroupBox(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editorGroupBox.sizePolicy().hasHeightForWidth())
        self.editorGroupBox.setSizePolicy(sizePolicy)
        self.editorGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.editorGroupBox.setObjectName("editorGroupBox")
        self.gridLayout_3 = QGridLayout(self.editorGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.variable_verticalLayout_1 = QVBoxLayout()
        self.variable_verticalLayout_1.setObjectName("variable_verticalLayout_1")
        self.listBox = QListWidget(self.editorGroupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listBox.sizePolicy().hasHeightForWidth())
        self.listBox.setSizePolicy(sizePolicy)
        self.listBox.setDragEnabled(True)
        self.listBox.setDragDropOverwriteMode(False)
        self.listBox.setDragDropMode(QAbstractItemView.InternalMove)
        self.listBox.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listBox.setAlternatingRowColors(True)
        self.listBox.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listBox.setMovement(QListView.Snap)
        self.listBox.setResizeMode(QListView.Fixed)
        self.listBox.setSelectionRectVisible(False)
        self.listBox.setObjectName("listBox")
        self.variable_verticalLayout_1.addWidget(self.listBox)
        self.gridLayout.addLayout(self.variable_verticalLayout_1, 0, 0, 1, 1)
        self.variable_verticalLayout_2 = QVBoxLayout()
        self.variable_verticalLayout_2.setObjectName("variable_verticalLayout_2")
        self.addButton = QPushButton(self.editorGroupBox)
        self.addButton.setObjectName("addButton")
        self.variable_verticalLayout_2.addWidget(self.addButton)
        self.editButton = QPushButton(self.editorGroupBox)
        self.editButton.setObjectName("editButton")
        self.variable_verticalLayout_2.addWidget(self.editButton)
        self.removeButton = QPushButton(self.editorGroupBox)
        self.removeButton.setObjectName("removeButton")
        self.variable_verticalLayout_2.addWidget(self.removeButton)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.variable_verticalLayout_2.addItem(spacerItem)
        self.upButton = QPushButton(self.editorGroupBox)
        self.upButton.setObjectName("upButton")
        self.variable_verticalLayout_2.addWidget(self.upButton)
        self.downButton = QPushButton(self.editorGroupBox)
        self.downButton.setObjectName("downButton")
        self.variable_verticalLayout_2.addWidget(self.downButton)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.variable_verticalLayout_2.addItem(spacerItem1)
        self.variable_verticalLayout_2.setStretch(3, 1)
        self.variable_verticalLayout_2.setStretch(6, 1)
        self.gridLayout.addLayout(self.variable_verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ok_pushButton = QPushButton(self.editorGroupBox)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.horizontalLayout.addWidget(self.ok_pushButton)
        self.cancel_pushButton = QPushButton(self.editorGroupBox)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.editorGroupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form", None, QApplication.UnicodeUTF8))
        self.editorGroupBox.setTitle(QApplication.translate("Form", "Maya Module Path Editor", None, QApplication.UnicodeUTF8))
        self.addButton.setText(QApplication.translate("Form", "<<", None, QApplication.UnicodeUTF8))
        self.editButton.setText(QApplication.translate("Form", "Edit", None, QApplication.UnicodeUTF8))
        self.removeButton.setText(QApplication.translate("Form", ">>", None, QApplication.UnicodeUTF8))
        self.upButton.setText(QApplication.translate("Form", "Move Up", None, QApplication.UnicodeUTF8))
        self.downButton.setText(QApplication.translate("Form", "Move Down", None, QApplication.UnicodeUTF8))
        self.ok_pushButton.setText(QApplication.translate("Form", "Save", None, QApplication.UnicodeUTF8))
        self.cancel_pushButton.setText(QApplication.translate("Form", "Close", None, QApplication.UnicodeUTF8))


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

        dlg = QInputDialog()
        dlg.setInputMode(QInputDialog.TextInput)
        txt, ok = dlg.getText(self, self.addCaption, self.addLabel)  # ,
        txt = txt.rstrip('\\')
        txt = txt.rstrip('/')
        # QLineEdit.Normal, self.listBox.currentItem().text())

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
            txt, ok = QInputDialog.getText(self, self.editCaption, self.editLabel,
                                                 QLineEdit.Normal, original)

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
        question = QMessageBox.question(
            self, "Remove",
            "Remove '{0}'?".format(txt),
            QMessageBox.Yes | QMessageBox.Default,
            QMessageBox.No)

        return question == QMessageBox.Yes

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
            QApplication.translate(
                "Form", "Edit environment variable '{0}'".format(envvarkey), None, QApplication.UnicodeUTF8))

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

                QMessageBox.question(
                    self, "Save succece",
                    "save file at '{0}'.".format(self.envvarpath),
                    QMessageBox.Ok | QMessageBox.Default)

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
                QMessageBox.question(
                    self, "Error",
                    "Maya.env is not detected (at: {0}), check your installation or call your system administrator.".format(p),
                    QMessageBox.Ok | QMessageBox.Default)
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

        self.settings_layout = QtWidgets.QHBoxLayout()
        self.settings_layout.addWidget(self.tabs, 1)
        self.setLayout(self.settings_layout)

        # self.resize(self.width(), self.height())
        self.resize(560, 560)

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
