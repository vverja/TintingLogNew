from PyQt5 import QtWidgets
from Ui import UserEdit, UserEditRow


class UserEditCtrl(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.ui = UserEdit.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tvUsersList.doubleClicked.connect(self.dblclicked_table)
        self.ui.actionUserAdd.triggered.connect(self.user_add)
        self.ui.actionUserDelete.triggered.connect(self.user_del)

        self.row_edit_window = QtWidgets.QDialog(self)
        self.row_ui = UserEditRow.Ui_Dialog()

    def dblclicked_table(self, index):
        id = index.sibling(index.row(), 0).data()
        if id:
            self.row_ui.setupUi(self.row_edit_window, id, operation=0)
            self.row_edit_window.show()

    def user_add(self):
        self.row_ui.setupUi(self.row_edit_window, None, operation=1)
        self.row_edit_window.show()

    def user_del(self):
        model = self.ui.tvUsersList.model()
        selectionIndexes =self.ui.tvUsersList.selectionModel().selectedIndexes()
        for index in selectionIndexes:
            model.removeRows(index.row(), 1, index)
        # self.ui.tvUsersList.repaint()
