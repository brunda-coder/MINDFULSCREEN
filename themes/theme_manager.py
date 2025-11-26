class ThemeManager:
    """
    Handles loading + switching visual themes.
    """

    def __init__(self):
        self.current_theme = "light"
        self.themes = {
            "light": {"bg": "#FFFFFF", "text": "#000000"},
            "dark": {"bg": "#000000", "text": "#FFFFFF"}
        }

    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name
            return f"Theme changed to {theme_name} vruuu ✨"
        return "Theme not found vruuu"

    def get_theme(self):
        return self.themes.get(self.current_theme, {})
