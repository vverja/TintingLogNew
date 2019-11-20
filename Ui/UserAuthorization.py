
from PyQt5 import QtCore, QtWidgets
from App.model import Users


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(331, 163)
        Form.setWindowTitle("Авторизация")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cbUsers = QtWidgets.QComboBox(Form)
        self.cbUsers.setObjectName("cbUsers")

        # Adding user names to combobox
        users = Users.select()
        for user in users:
            self.cbUsers.addItem(user.username)


        self.verticalLayout.addWidget(self.cbUsers)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lePasswrd = QtWidgets.QLineEdit(Form)
        self.lePasswrd.setObjectName("lePasswrd")
        self.verticalLayout.addWidget(self.lePasswrd)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Пользователь"))
        self.label_2.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "ОК"))


#if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # Form = QtWidgets.QWidget()
    # ui = Ui_Form()
    # ui.setupUi(Form)
    # Form.show()
    # sys.exit(app.exec_())
