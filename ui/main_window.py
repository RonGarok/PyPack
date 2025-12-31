import sys
import os
from PySide6.QtWidgets import QMainWindow, QTabWidget, QMessageBox
from PySide6.QtGui import QIcon

from ui.tabs.installed_tab import InstalledTab
from ui.tabs.explore_tab import ExploreTab
from ui.tabs.settings_tab import SettingsTab

from core.lang_manager import load_config
from core.translator import translate


def resource_path(relative_path):
    """Retourne le chemin correct, même dans un EXE PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        config = load_config()
        self.lang_code = config.get("language", "fr")

        self.setWindowTitle(translate("PyPack - Gestionnaire de paquets Python", self.lang_code))

        # Logo
        self.setWindowIcon(QIcon(resource_path("assets/pypack.ico")))

        self.resize(1000, 650)

        self._build_ui()
        self._build_menu()

    def _build_ui(self):
        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        self.installed_tab = InstalledTab(self.lang_code)
        tabs.addTab(self.installed_tab, translate("Installés", self.lang_code))

        self.explore_tab = ExploreTab(self.lang_code)
        tabs.addTab(self.explore_tab, translate("Explorer PyPI", self.lang_code))

        self.settings_tab = SettingsTab(self)
        tabs.addTab(self.settings_tab, translate("Paramètres", self.lang_code))

    def _build_menu(self):
        menu = self.menuBar()
        help_menu = menu.addMenu(translate("Aide", self.lang_code))

        feedback_action = help_menu.addAction(translate("Envoyer un feedback", self.lang_code))
        feedback_action.triggered.connect(self._show_feedback_message)

    def _show_feedback_message(self):
        QMessageBox.information(
            self,
            translate("Feedback", self.lang_code),
            translate("Pour envoyer un feedback, écrivez à : Aaronsdsm@gmail.com", self.lang_code)
        )