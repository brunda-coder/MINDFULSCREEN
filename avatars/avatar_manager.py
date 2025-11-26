class AvatarManager:
    """
    Handles creating, loading, and switching user avatars.
    """

    def __init__(self):
        self.current_avatar = None
        self.avatars = {}

    def add_avatar(self, name, data):
        self.avatars[name] = data

    def set_avatar(self, name):
        if name in self.avatars:
            self.current_avatar = name
            return f"Avatar switched to {name} vruuu 🌀"
        return "Avatar not found vruuu"

    def get_current_avatar(self):
        return self.avatars.get(self.current_avatar, {})
