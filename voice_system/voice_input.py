class VoiceInput:
    """
    Handles recording, capturing, and processing raw voice input.
    """

    def __init__(self):
        self.is_listening = False

    def start_listening(self):
        self.is_listening = True
        print("Voice system is listening... vruuu 🎧")

    def stop_listening(self):
        self.is_listening = False
        print("Voice system stopped listening.")

    def capture_audio(self):
        if not self.is_listening:
            return None
        return "raw_audio_data"
