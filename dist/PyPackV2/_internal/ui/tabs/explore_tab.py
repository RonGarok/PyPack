from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QListWidget, QMessageBox, QTextEdit, QLabel
)
from PySide6.QtCore import Qt, QThread, Signal

from core.pypi_api import search_pypi, get_package_info
from core.pip_interface import install_package
from core.translator import translate


class SearchThread(QThread):
    results_ready = Signal(list)

    def __init__(self, query: str):
        super().__init__()
        self.query = query

    def run(self):
        results = search_pypi(self.query)
        self.results_ready.emit(results)


class ExploreTab(QWidget):
    def __init__(self, lang_code):
        super().__init__()
        self.lang = lang_code

        self._build_ui()
        self._connect_signals()

    def _build_ui(self):
        main_layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(translate("Rechercher un paquet sur PyPI...", self.lang))
        self.search_button = QPushButton(translate("Rechercher", self.lang))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        self.results_list = QListWidget()
        self.install_button = QPushButton(translate("Installer le paquet sélectionné", self.lang))

        left_layout.addLayout(search_layout)
        left_layout.addWidget(self.results_list)
        left_layout.addWidget(self.install_button)

        right_layout = QVBoxLayout()
        self.details_label = QLabel(translate("Détails du paquet", self.lang))
        self.details_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)

        right_layout.addWidget(self.details_label)
        right_layout.addWidget(self.details_text)

        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 1)

    def _connect_signals(self):
        self.search_button.clicked.connect(self._on_search_clicked)
        self.install_button.clicked.connect(self._on_install_clicked)
        self.results_list.currentTextChanged.connect(self._on_result_selected)

    def _on_search_clicked(self):
        query = self.search_input.text().strip()
        if not query:
            QMessageBox.warning(self, translate("Erreur", self.lang), translate("Veuillez entrer un terme de recherche.", self.lang))
            return

        self.results_list.clear()
        self.details_text.setPlainText(translate("Recherche en cours...", self.lang))

        self.search_thread = SearchThread(query)
        self.search_thread.results_ready.connect(self._on_results_ready)
        self.search_thread.start()

    def _on_results_ready(self, results):
        self.results_list.clear()

        if not results:
            self.results_list.addItem(translate("Aucun résultat.", self.lang))
            self.details_text.setPlainText(translate("Aucun paquet trouvé.", self.lang))
            return

        for name in results:
            self.results_list.addItem(name)

        self.details_text.setPlainText(f"{len(results)} {translate('paquets trouvés.', self.lang)}")

    def _get_selected_name(self):
        item = self.results_list.currentItem()
        if not item:
            return None
        text = item.text()
        if text == translate("Aucun résultat.", self.lang):
            return None
        return text

    def _on_install_clicked(self):
        name = self._get_selected_name()
        if not name:
            QMessageBox.warning(self, translate("Erreur", self.lang), translate("Veuillez sélectionner un paquet.", self.lang))
            return

        try:
            install_package(name)
            QMessageBox.information(self, translate("Installation terminée", self.lang), translate(f"{name} a été installé.", self.lang))
        except Exception as e:
            QMessageBox.critical(self, translate("Erreur", self.lang), str(e))

    def _on_result_selected(self, text):
        if not text or text == translate("Aucun résultat.", self.lang):
            self.details_text.clear()
            return

        name = text
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