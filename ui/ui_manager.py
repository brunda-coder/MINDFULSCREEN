class UIManager:
    """
    Controls switching screens, loading layouts, refreshing UI.
    """

    def __init__(self):
        self.current_screen = None
        self.screens = {}

    def add_screen(self, name, screen_object):
        self.screens[name] = screen_object

    def switch_to(self, name):
        if name in self.screens:
            self.current_screen = name
            return f"Switched to {name} screen vruuu ✨"
        return "Screen not found vruuu"

    def render(self):
        if not self.current_screen:
            return "No screen loaded vruuu"
        return self.screens[self.current_screen].render()
