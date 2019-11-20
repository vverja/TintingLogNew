from Ui import RowEdit
from Ui.TM.UserEditTM import TableModel
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(584, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tvUsersList = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tvUsersList.setObjectName("tvUsersList")
        self.tvUsersList.setModel(TableModel())
        self.verticalLayout.addWidget(self.tvUsersList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUserAdd = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Actions-user-group-new-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUserAdd.setIcon(icon)
        self.actionUserAdd.setObjectName("actionUserAdd")
        self.actionUserDelete = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Actions-user-group-delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUserDelete.setIcon(icon1)
        self.actionUserDelete.setObjectName("actionUserDelete")

        self.toolBar.addAction(self.actionUserAdd)
        self.toolBar.addAction(self.actionUserDelete)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список пользователей"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionUserAdd.setText(_translate("MainWindow", "UserAdd"))
        self.actionUserAdd.setToolTip(_translate("MainWindow", "Добавить пользователя"))
        self.actionUserDelete.setText(_translate("MainWindow", "UserDelete"))
        self.actionUserDelete.setToolTip(_translate("MainWindow", "Удалить пользователя"))
import Ui.resourse_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
