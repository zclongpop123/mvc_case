#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Tue Nov 06 10:54:12 2018
#========================================
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import mvc_qt, mvc_model, mvc_delegate
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class MVCWindow(mvc_qt.Ui_MainWindow, QtWidgets.QMainWindow):
    '''
    '''
    def __init__(self, parent=None):
        '''
        '''
        super(MVCWindow, self).__init__(parent)
        self.setupUi(self)

        #- 
        self.__list_model = mvc_model.MVC_List_Model(self.listView, list('ABCDE'))
        self.listView.setModel(self.__list_model)
        self.listView_2.setModel(self.__list_model)

        self.__table_model = mvc_model.MVC_table_model(self.tableView, [['A2', 'B2', 'A3', 'B4'], ['B1', 'B2', 'B3', 'B4']])
        self.tableView.setModel(self.__table_model)
        self.tableView_2.setModel(self.__table_model)

        self.__delegate = mvc_delegate.ComboDelegate()
        self.listView.setItemDelegate(self.__delegate)



    @QtCore.pyqtSlot(bool)
    def on_btn_lsv_insert_clicked(self, args):
        '''
        '''
        text = QtWidgets.QInputDialog.getText(self, 'Input', 'strings:')
        if text[-1]:
            self.__list_model.insertRow(text[0])



    @QtCore.pyqtSlot(bool)
    def on_btn_lsv_remove_clicked(self, args):
        '''
        '''
        row = self.listView.currentIndex().row()
        self.__list_model.removeRow(row)



    @QtCore.pyqtSlot(bool)
    def on_btn_lsv_clear_clicked(self, args):
        '''
        '''
        self.__list_model.clear()




def main():
    '''
    '''
    application = QtWidgets.QApplication(sys.argv)

    window = MVCWindow()
    window.show()    

    application.exec_()




if __name__ == '__main__':
    main()
