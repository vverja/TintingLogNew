import sys
from PyQt5 import QtWidgets
from Ui import MainForm as mf
from Ui import UserLogon as UserAuto
from Ui import RowEdit
from Ui.TM import MainWindowTModel
from App.utility import *
from App.user_edit_ctrl import *

from datetime import datetime, time

class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)

        self.ui = mf.Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_user = None

        # Подключаем модель к таблице
        self.ui.twTinting.setModel(MainWindowTModel.TableModel())
        # Привязка формы к редактированию по двойному клику
        self.row_edit_window = QtWidgets.QDialog(self)
        self.row_ui = RowEdit.Ui_Dialog()
        self.ui.twTinting.doubleClicked.connect(self.dblclicked_table)

        self.ui.actionImportProduct.triggered.connect(self.import_data)
        self.ui.actionUserEdit.triggered.connect(self.show_user_edit)

    def show(self):
        ulogin = UserLogin(self)
        # while not ulogin.current_user:
        result = ulogin.exec_()

        self.current_user = ulogin.current_user
        self.set_date_period()

        QtWidgets.QWidget.show(self)

    def set_date_period(self):
        begin = MainWindowTModel.TableModel.get_begin_date()
        end = MainWindowTModel.TableModel.get_begin_date()
        self.ui.dtBegin.setDate(begin)
        self.ui.dtEnd.setDate(end)

    def add_log(self):
        # todo: открыть форму добаления колеровки
        pass

    def del_log(self):
        # todo: удалить запись колеровки из базы данных
        pass

    def import_data(self):
        # todo: функция импорта продукции и ?? вееров
        caption = 'Выберите файл с данными'
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption=caption,
                                                            filter="Data file (*.csv *.xls *.xlsx)")
        if import_data_from_file(filename):
            QtWidgets.QMessageBox.information(self, 'Информация', 'Данные загружены')
        else:
            QtWidgets.QMessageBox.critical(self, 'Информация', 'Данные не загружены')

    def export_data(self):
        # todo: функция эскспорта журнала колеровок
        pass

    def dblclicked_table(self, index):
        id = index.sibling(index.row(), 0).data()
        if id:
            self.row_ui.setupUi(self.row_edit_window, id, operation=0)
            self.row_edit_window.show()

    def show_user_edit(self):
        uedit = UserEditCtrl(self)
        uedit.show()


class UserLogin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.current_user = None
        self.ui = UserAuto.Ui_DialogUserLogon()
        self.ui.setupUi(self)
        self.ui.cbUser.addItems([rec.username for rec in Users.select(Users.username)])
        self.accepted.connect(self.accept)
        self.rejected.connect(self.close)

    def accept(self):
        if self.user_authenticate():
             QtWidgets.QDialog.done(self, 0)
        else:
            self.ui.lbWarning.setText("Пароль не верный!!!")

    def user_authenticate(self):
        user = self.ui.cbUser.currentText()
        passwrd = self.ui.lineEdit.text()

        user_cursor = Users.select().where(Users.username == user,
                                           Users.password == passwrd)

        if len(user_cursor):
            self.current_user = user_cursor[0].username
            return True
        else:
            return False


if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_form = MainWin()
    main_form.show()

    sys.exit(app.exec_())

