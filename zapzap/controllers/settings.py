from multiprocessing.spawn import import_main_path
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from zapzap.service.portal_config import write_json


class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('zapzap/view/settings.ui', self)

        self.parent = parent

        self.closeButton.clicked.connect(parent.onToggled)

        # Sistema
        self.start_system.stateChanged.connect(self.state_start_system)
        self.start_hide.stateChanged.connect(
            lambda: write_json('start_hide', self.start_hide.isChecked()))
        self.night_mode.stateChanged.connect(self.state_night_mode)

        # Notificações
        self.notify_desktop.stateChanged.connect(self.state_notify_desktop)
        self.show_photo.stateChanged.connect(
            lambda: write_json('show_photo', self.show_photo.isChecked()))
        self.show_name.stateChanged.connect(
            lambda: write_json('show_name', self.show_name.isChecked()))
        self.show_msg.stateChanged.connect(
            lambda: write_json('show_msg', self.show_msg.isChecked()))

    def state_night_mode(self, s):
        self.parent.parent.toggle_stylesheet()

        write_json('night_mode', bool(s))

    def state_start_system(self, s):
        self.start_hide.setEnabled(s)

        write_json('start_system', bool(s))

    def state_notify_desktop(self, s):
        self.show_photo.setEnabled(s)
        self.show_name.setEnabled(s)
        self.show_msg.setEnabled(s)

        write_json('notify_desktop', bool(s))
