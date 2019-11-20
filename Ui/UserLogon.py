
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogUserLogon(object):
    def setupUi(self, DialogUserLogon):
        DialogUserLogon.setObjectName("DialogUserLogon")
        DialogUserLogon.resize(401, 137)
        DialogUserLogon.setModal(True)
        self.widget = QtWidgets.QWidget(DialogUserLogon)
        self.widget.setGeometry(QtCore.QRect(0, 10, 401, 122))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cbUser = QtWidgets.QComboBox(self.widget)

        self.cbUser.setObjectName("cbUser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbUser)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lbWarning = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 147, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbWarning.setPalette(palette)
        self.lbWarning.setText("")
        self.lbWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWarning.setObjectName("lbWarning")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lbWarning)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogUserLogon)
        self.buttonBox.accepted.connect(DialogUserLogon.accept)
        self.buttonBox.rejected.connect(DialogUserLogon.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogUserLogon)

    def retranslateUi(self, DialogUserLogon):
        _translate = QtCore.QCoreApplication.translate
        DialogUserLogon.setWindowTitle(_translate("DialogUserLogon", "Авторизация"))
        self.label.setText(_translate("DialogUserLogon", "Пользователь"))
        self.label_2.setText(_translate("DialogUserLogon", "Пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogUserLogon = QtWidgets.QDialog()
    ui = Ui_DialogUserLogon()
    ui.setupUi(DialogUserLogon)
    DialogUserLogon.show()
    sys.exit(app.exec_())
