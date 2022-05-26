# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pin_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class PinUI(object):
    def __init__(self, form) -> None:
        self.setupUi(Form=form)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.pin_label = QtWidgets.QLabel(Form)
        self.pin_label.setGeometry(QtCore.QRect(300, 110, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pin_label.setFont(font)
        self.pin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pin_label.setObjectName("pin_label")
        self.pin_edit = QtWidgets.QPlainTextEdit(Form)
        self.pin_edit.setGeometry(QtCore.QRect(270, 210, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pin_edit.setFont(font)
        self.pin_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pin_edit.setPlainText("")
        self.pin_edit.setObjectName("pin_edit")
        self.confirm_button = QtWidgets.QPushButton(Form)
        self.confirm_button.setGeometry(QtCore.QRect(330, 490, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.confirm_button.setObjectName("confirm_button")
        self.enter_card_button = QtWidgets.QPushButton(Form)
        self.enter_card_button.setGeometry(QtCore.QRect(240, 270, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_card_button.setFont(font)
        self.enter_card_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.enter_card_button.setObjectName("enter_card_button")
        self._enter_text_label = QtWidgets.QLabel(Form)
        self._enter_text_label.setGeometry(QtCore.QRect(180, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self._enter_text_label.setFont(font)
        self._enter_text_label.setObjectName("_enter_text_label")
        self.load_session_button = QtWidgets.QPushButton(Form)
        self.load_session_button.setGeometry(QtCore.QRect(420, 270, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.load_session_button.setFont(font)
        self.load_session_button.setStyleSheet("background-color: rgb(255, 175, 16);")
        self.load_session_button.setObjectName("load_session_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pin_label.setText(_translate("Form", "PIN"))
        self.confirm_button.setText(_translate("Form", "CONFIRM"))
        self.enter_card_button.setText(_translate("Form", "ENTER A CARD"))
        self._enter_text_label.setText(_translate("Form", "Enter:"))
        self.load_session_button.setText(_translate("Form", "LOAD SESSION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
