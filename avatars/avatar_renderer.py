class AvatarRenderer:
    """
    Renders avatar visuals for UI.
    """

    def render(self, avatar_data):
        if not avatar_data:
            return "No avatar loaded vruuu"
        return f"Rendering avatar: {avatar_data.get('name')} ✨"
