from App.model import Log, LogTablePart, Product, Color
from PyQt5.QtCore import *
from typing import Any
import datetime as dt


class TableModel(QAbstractTableModel):
    def __init__(self, parent=None, date1=0, date2=0):
        super(TableModel, self).__init__(parent)
        # Инициализируем колонки и таблицу
        self.column_names = ['id', 'Дата', 'Телефон', 'Выгружен', 'Продукт', 'Цвет']
        self.table = None
        # Устанавливаем даты если они не были указаны в конструкторе
        if not date1:
            self.date1 = self.get_begin_date()
        if not date2:
            self.date2 = self.get_end_date()
        # Заполняем таблицу
        self.model_update()
        self.dataChanged.connect(self.model_update)

    def rowCount(self, parent):
        return len(self.table)

    def columnCount(self, parent):
        return len(self.column_names)

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            row = index.row()
            column = index.column()
            value = self.table[row].get(self.column_names[column])

            if role == Qt.DisplayRole and column == 1:
                value = dt.datetime.fromtimestamp(value/1000)
                return QVariant(value.strftime('%Y-%m-%d %H:%M:%S'))

            if role == Qt.DisplayRole and column != 3:
                return QVariant(value)

            elif role == Qt.CheckStateRole and column == 3:
                if value:
                    return Qt.Checked
                else:
                    return Qt.Unchecked

    def setData(self, index: QModelIndex, value: Any, role: int = ...):

        if role != Qt.EditRole and role == Qt.CheckStateRole:
            return False
        if index.isValid():
            row = index.row()
        return True

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.ItemIsEnabled
        flag = Qt.ItemFlags(QAbstractTableModel.flags(self, index))
        if index.column() == 2:
                flag |= Qt.ItemIsUserCheckable
        else:
            flag |= Qt.ItemIsEnabled
        return flag

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.column_names[section])

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...):
        self.beginInsertRows(QModelIndex(),row, row+count -1)
        self.model_update()
        self.endInsertRows()

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...):
        self.beginRemoveRows(QModelIndex(), row, row+count -1)
        idx = parent.sibling(parent.row(), 0).data()
        Log.delete_by_id(idx)
        LogTablePart.delete().where(LogTablePart.log_id == idx)
        self.model_update()
        self.endRemoveRows()

    def model_update(self):
        self.table = Log.select(Log.id.alias(self.column_names[0]),
                                Log.date.alias(self.column_names[1]),
                                Log.phone.alias(self.column_names[2]),
                                Log.exported.alias(self.column_names[3]),
                                Product.name.alias(self.column_names[4]),
                                Color.color_id.alias(self.column_names[5])) \
            .join(LogTablePart) \
            .join(Product).switch(LogTablePart) \
            .join(Color).where(LogTablePart.row_number == 1) \
            .where(Log.date >= self.date1 and Log.date <= self.date2).dicts()

    @staticmethod
    def get_begin_date():
        return dt.datetime.combine(dt.datetime.now(), dt.time(0, 0, 0, 0))

    @staticmethod
    def get_end_date():
        return dt.datetime.combine(dt.datetime.now(), dt.time(23, 59, 59))

