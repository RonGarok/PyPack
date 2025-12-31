from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QPushButton,
    QHBoxLayout, QMessageBox, QTextEdit, QLabel, QSizePolicy
)
from PySide6.QtCore import Qt, QThread, Signal

from core.pip_interface import list_installed_packages, uninstall_package
from core.pypi_api import get_package_info
from core.translator import translate


class LoadInstalledThread(QThread):
    packages_loaded = Signal(list)

    def run(self):
        packages = list_installed_packages()
        self.packages_loaded.emit(packages)


class InstalledTab(QWidget):
    def __init__(self, lang_code):
        super().__init__()
        self.lang = lang_code

        self._build_ui()
        self._connect_signals()
        self._load_packages()

    def _build_ui(self):
        main_layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()
        self.package_list = QListWidget()
        left_layout.addWidget(self.package_list)

        btn_layout = QHBoxLayout()
        self.refresh_btn = QPushButton(translate("Rafraîchir", self.lang))
        self.uninstall_btn = QPushButton(translate("Désinstaller", self.lang))
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addWidget(self.uninstall_btn)

        left_layout.addLayout(btn_layout)

        right_layout = QVBoxLayout()
        self.details_label = QLabel(translate("Détails du paquet sélectionné", self.lang))
        self.details_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        right_layout.addWidget(self.details_label)
        right_layout.addWidget(self.details_text)

        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 1)

    def _connect_signals(self):
        self.refresh_btn.clicked.connect(self._load_packages)
        self.uninstall_btn.clicked.connect(self._uninstall_selected)
        self.package_list.currentTextChanged.connect(self._on_package_selected)

    def _load_packages(self):
        self.package_list.clear()
        self.details_text.setPlainText(translate("Chargement des paquets installés...", self.lang))
        self.thread = LoadInstalledThread()
        self.thread.packages_loaded.connect(self._on_packages_loaded)
        self.thread.start()

    def _on_packages_loaded(self, packages):
        self.package_list.clear()
        for pkg in packages:
            self.package_list.addItem(f"{pkg['name']} ({pkg['version']})")
        self.details_text.setPlainText(f"{len(packages)} {translate('paquets installés.', self.lang)}")

    def _get_selected_name(self):
        item = self.package_list.currentItem()
        if not item:
            return None
        return item.text().split(" (")[0]

    def _uninstall_selected(self):
        name = self._get_selected_name()
        if not name:
            QMessageBox.warning(self, translate("Erreur", self.lang), translate("Veuillez sélectionner un paquet.", self.lang))
            return

        if QMessageBox.question(
            self,
            translate("Confirmation", self.lang),
            translate(f"Voulez-vous vraiment désinstaller {name} ?", self.lang)
        ) != QMessageBox.Yes:
            return

        try:
            uninstall_package(name)
            QMessageBox.information(self, translate("Terminé", self.lang), translate(f"{name} a été désinstallé.", self.lang))
            self._load_packages()
        except Exception as e:
            QMessageBox.critical(self, translate("Erreur", self.lang), str(e))

    def _on_package_selected(self, text):
        if not text:
            self.details_text.clear()
            return

        name = text.split(" (")[0]
        info = get_package_info(name)

        if not info:
            self.details_text.setPlainText(translate("Aucune information trouvée.", self.lang))
            return

        lines = [
            f"{translate('Nom', self.lang)}: {info.get('name')}",
            f"{translate('Version PyPI', self.lang)}: {info.get('version')}",
            f"{translate('Auteur', self.lang)}: {info.get('author')}",
            f"{translate('Site', self.lang)}: {info.get('home_page')}",
            "",
            translate("Résumé", self.lang) + ":",
            info.get("summary") or translate("(aucun résumé)", self.lang),
        ]
        self.details_text.setPlainText("\n".join(lines))