# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atm_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AtmUI(object):
    def __init__(self, form) -> None:
        self.setupUi(Form=form)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.atm_screen_label = QtWidgets.QLabel(Form)
        self.atm_screen_label.setGeometry(QtCore.QRect(20, 20, 421, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.atm_screen_label.setFont(font)
        self.atm_screen_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.atm_screen_label.setAlignment(QtCore.Qt.AlignCenter)
        self.atm_screen_label.setObjectName("atm_screen_label")
        self.balance_button = QtWidgets.QPushButton(Form)
        self.balance_button.setGeometry(QtCore.QRect(470, 220, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.balance_button.setFont(font)
        self.balance_button.setStyleSheet("background-color: rgb(71, 184, 255);")
        self.balance_button.setObjectName("balance_button")
        self.withdraw_button = QtWidgets.QPushButton(Form)
        self.withdraw_button.setGeometry(QtCore.QRect(640, 220, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.withdraw_button.setFont(font)
        self.withdraw_button.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.withdraw_button.setObjectName("withdraw_button")
        self.payment_button = QtWidgets.QPushButton(Form)
        self.payment_button.setGeometry(QtCore.QRect(470, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.payment_button.setFont(font)
        self.payment_button.setStyleSheet("background-color: rgb(255, 150, 64);")
        self.payment_button.setObjectName("payment_button")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(640, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.exit_button.setObjectName("exit_button")
        self.about_user_label = QtWidgets.QLabel(Form)
        self.about_user_label.setGeometry(QtCore.QRect(470, 30, 301, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.about_user_label.setFont(font)
        self.about_user_label.setStyleSheet("background-color: rgb(255, 255, 157);")
        self.about_user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.about_user_label.setObjectName("about_user_label")
        self.phone_edit = QtWidgets.QPlainTextEdit(Form)
        self.phone_edit.setGeometry(QtCore.QRect(470, 380, 301, 51))
        self.phone_edit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.phone_edit.setObjectName("phone_edit")
        self.cash_edit = QtWidgets.QPlainTextEdit(Form)
        self.cash_edit.setGeometry(QtCore.QRect(470, 450, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cash_edit.setFont(font)
        self.cash_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cash_edit.setObjectName("cash_edit")
        self.save_session_button = QtWidgets.QPushButton(Form)
        self.save_session_button.setGeometry(QtCore.QRect(470, 520, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_session_button.setFont(font)
        self.save_session_button.setStyleSheet("background-color: rgb(224, 110, 255);")
        self.save_session_button.setObjectName("save_session_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.atm_screen_label.setText(_translate("Form", "Screen..."))
        self.balance_button.setText(_translate("Form", "BALANCE"))
        self.withdraw_button.setText(_translate("Form", "WITHDRAW"))
        self.payment_button.setText(_translate("Form", "PAYMENT"))
        self.exit_button.setText(_translate("Form", "EXIT"))
        self.about_user_label.setText(_translate("Form", "About User..."))
        self.phone_edit.setPlaceholderText("Enter phone number: ")
        self.cash_edit.setPlaceholderText("Enter cash: ")
        self.save_session_button.setText(_translate("Form", "SAVE SESSION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
