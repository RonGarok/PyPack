from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QMessageBox
from core.lang_manager import load_config, save_config

LANGUAGES = {
    "Français": "fr",
    "English": "en",
    "Deutsch": "de",
    "Español": "es",
    "Italiano": "it",
    "Português": "pt",
    "Nederlands": "nl",
    "Polski": "pl",
    "Svenska": "sv"
}

class SettingsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout(self)

        self.label = QLabel("Langue :")
        self.combo = QComboBox()

        for name in LANGUAGES:
            self.combo.addItem(name)

        config = load_config()
        current_lang = config.get("language", "fr")

        for name, code in LANGUAGES.items():
            if code == current_lang:
                self.combo.setCurrentText(name)

        layout.addWidget(self.label)
        layout.addWidget(self.combo)

        self.combo.currentTextChanged.connect(self.change_language)

    def change_language(self, lang_name):
        lang_code = LANGUAGES[lang_name]

        config = load_config()
        config["language"] = lang_code
        save_config(config)

        QMessageBox.information(
            self,
            "Langue changée",
            "La langue a été modifiée.\nRedémarrez PyPack pour appliquer les changements."
        )