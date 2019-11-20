from PyQt5 import QtCore, QtGui, QtWidgets
from App.model import *


class Ui_Dialog(object):
    def setupUi(self, Dialog, idx, operation=0):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.dialog = Dialog
        self.operation = operation

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout.addWidget(self.lblName)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblPassword = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblPassword.setObjectName("lblPassword")
        self.horizontalLayout_4.addWidget(self.lblPassword)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")

        
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblMarket = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblMarket.setObjectName("lblMarket")
        self.horizontalLayout_2.addWidget(self.lblMarket)
        self.cmbMarkets = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmbMarkets.setObjectName("cmbMarkets")


        self.horizontalLayout_2.addWidget(self.cmbMarkets)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")

        if idx:
            self.record = self.get_record_from_db(idx)
            self.lineEdit.setText(self.record['username'])
            self.lineEdit_2.setText(self.record['password'])
            self.get_markets(self.record['default_market'])
            if self.record ['admin']:
                self.checkBox.setCheckState(QtCore.Qt.Checked)
            else:
                self.checkBox.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.get_markets()

        self.horizontalLayout_6.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblName.setText(_translate("Dialog", "ФИО"))
        self.lblPassword.setText(_translate("Dialog", "Пароль"))
        self.lblMarket.setText(_translate("Dialog", "Маркет"))
        self.checkBox.setText(_translate("Dialog", "Админ"))

    def get_record_from_db(self, idx):
        try:
            record = Users.get(id=idx)
            result = record.__dict__['__data__']
        except IndexError:
            return None
        return result

    def set_record_in_db(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        admin = self.checkBox.checkState()
        default_market = self.cmbMarkets.currentData()
        table_view = self.dialog.parent().ui.tvUsersList
        model = table_view.model()
        if self.operation == 0:
            Users.update(username=name,
                         password=password,
                         admin=admin,
                         default_market=default_market) \
                .where(Users.id == self.record['id']).execute()
            model.model_update()
        else:
            model.insertRows(len(model.table), 1, QtCore.QModelIndex())
            Users.insert(username=name,
                         password=password,
                         admin=admin,
                         default_market=default_market).execute()
            model.model_update()

    def get_markets(self, current_id=None):
        self.cmbMarkets.clear()
        for row in Markets.select().execute():
            self.cmbMarkets.addItem(row.name, userData=row.id)
        if current_id:
            idx = self.cmbMarkets.findData(current_id)
            self.cmbMarkets.setCurrentIndex(idx)

    def accept(self):
        self.set_record_in_db()
        QtWidgets.QDialog.done(self.dialog, 0)
