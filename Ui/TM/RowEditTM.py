from App.model import LogTablePart as Ltp, Product, Color, Base, Tare
from PyQt5.QtCore import *
from typing import Any


class RowEditTM(QAbstractTableModel):
    def __init__(self, parent=None, idx=0):
        super(RowEditTM, self).__init__(parent)
        self.column_names = ['id', 'Номер', 'Продукт', 'Тара', 'База', 'Цвет']
        self.table = None

        self.model_update(idx)

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

            if role == Qt.DisplayRole: # and column != 2:
                return QVariant(value)
            # elif role == Qt.CheckStateRole and column == 2:
            #     if value:
            #         return Qt.Checked
            #     else:
            #         return Qt.Unchecked

    def setData(self, index: QModelIndex, value: Any, role: int = ...):

        if role != Qt.EditRole: # and role == Qt.CheckStateRole:
            return False
        if index.isValid():
            row = index.row()
        return True

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.ItemIsEnabled
        flag = Qt.ItemFlags(QAbstractTableModel.flags(self, index))
        # if index.column() == 2:
        #         flag |= Qt.ItemIsUserCheckable
        # else:
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
        Ltp.delete_by_id(idx)
        self.model_update()
        self.endRemoveRows()

    def model_update(self, idx):
        self.table = Ltp.select(Ltp.id.alias(self.column_names[0]),
                                Ltp.row_number.alias(self.column_names[1]),
                                Product.name.alias(self.column_names[2]),
                                Tare.name.alias(self.column_names[3]),
                                Base.name.alias(self.column_names[4]),
                                Color.color_id.alias(self.column_names[5])) \
            .join(Product).switch(Ltp) \
            .join(Tare).switch(Ltp) \
            .join(Base).switch(Ltp) \
            .join(Color) \
            .where(Ltp.log_id == idx).dicts()
