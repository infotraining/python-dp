import PySide6.QtWidgets as Qw
import PySide6.QtGui as Qg
from PySide6.QtCore import Qt
import PySide6.QtCore as Qc

import sys


class CustomListWidget(Qw.QListWidget):

    returnPressed = Qc.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def selectedIndex(self):
        return self.selectedIndexes

    def keyPressEvent(self, event: Qg.QKeyEvent) -> None:
        if event.key() == Qc.Qt.Key_Enter or event.key() == Qc.Qt.Key_Return:            
            self.returnPressed.emit()
        
        return super().keyPressEvent(event)


class QuickEntryMediator(Qc.QObject):
    def __init__(self, line_edit: Qw.QLineEdit, list_widget: CustomListWidget):
        super().__init__()
        self._line_edit = line_edit
        self._list_widget = list_widget
        self._line_edit.textChanged.connect(self.on_line_edit_text_changed)
        self._line_edit.returnPressed.connect(self.on_return_pressed)
        self._list_widget.returnPressed.connect(self.on_return_pressed)        

    @Qc.Slot(str)
    def on_line_edit_text_changed(self, text):
        if (not text):
            self._list_widget.clearSelection()
            return

        is_found = False
        for index in range(self._list_widget.count()):
            item = self._list_widget.item(index)
            item_text: str = item.text()
            if item_text.startswith(text):
                item.setSelected(True)
                self._item_selected = item
                is_found = True
                break

        if not is_found:
            self._list_widget.clearSelection()

    @Qc.Slot()
    def on_return_pressed(self):
        selected_items = self._list_widget.selectedItems()
        if len(selected_items) == 1:
            self._line_edit.setText(selected_items[0].text())



class MyDialog(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickEntryMediator")

        grid = Qw.QVBoxLayout()
        line_edit = Qw.QLineEdit(self)
        grid.addWidget(line_edit)
        list_widget = CustomListWidget(self)        
        Qw.QListWidgetItem("Metallica", list_widget)
        Qw.QListWidgetItem("Tool", list_widget)
        Qw.QListWidgetItem("Alice in Chains", list_widget)
        Qw.QListWidgetItem("Soundgarden", list_widget)
        Qw.QListWidgetItem("Pearl Jam", list_widget)
        grid.addWidget(list_widget)
        self.setLayout(grid)

        self._quick_entry_mediator = QuickEntryMediator(line_edit, list_widget)


app = Qw.QApplication(sys.argv)
window = MyDialog()
window.show()

app.exec()
