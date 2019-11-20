

from PyQt5 import QtCore, QtGui, QtWidgets
from App.model import *
from datetime import datetime as dt
from Ui.TM.RowEditTM import *


import Ui.resourse_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog,idx, operation=0):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 323)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.dialog = Dialog
        self.operation = operation
        if self.operation == 0:
            self.record = self.get_record_from_db(idx)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 280, 471, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lb_date = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_date.setObjectName("lb_date")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_date)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lePhone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lePhone.setObjectName("lePhone")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lePhone)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 481, 198))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Button-Add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.button_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_delete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Button-Close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_delete.setIcon(icon1)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        if idx:
            date = dt.fromtimestamp(self.record['header']['date'] / 1000)
            self.dateEdit.setDate(date)
            self.lePhone.setText(self.record['header']['phone'])
            self.tableView.setModel(RowEditTM(self.dialog, idx))
            self.tableView.setColumnHidden(0, True)
            self.tableView.setColumnWidth(1, 5)
            self.tableView.setColumnWidth(2, 250)
            self.tableView.setColumnWidth(3, 5)
            self.tableView.setColumnWidth(4, 5)
            self.tableView.setColumnWidth(5, 50)



        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_date.setText(_translate("Dialog", "Дата"))
        self.label.setText(_translate("Dialog", "Телефон"))

    def get_record_from_db(self, idx):
        try:
            result = {}
            record = Log.get(id=idx)
            result['header'] = record.__dict__['__data__']
            query = LogTablePart.select().where(LogTablePart.log_id == idx).dicts()
            record = [row for row in query]
            result['table'] = record.copy()

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
