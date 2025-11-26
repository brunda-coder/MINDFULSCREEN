from .voice_input import VoiceInput
from .speech_to_text import SpeechToText
from .text_to_speech import TextToSpeech

class VoiceCore:
    """
    Central voice pipeline:
    - Listen
    - Transcribe
    - Respond
    - Speak
    """

    def __init__(self):
        self.input = VoiceInput()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

    def handle_voice_interaction(self):
        self.input.start_listening()
        audio = self.input.capture_audio()
        text = self.stt.transcribe(audio)
        self.tts.speak(f"I heard: {text}")
        self.input.stop_listening()
