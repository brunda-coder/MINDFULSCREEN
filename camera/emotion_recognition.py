# camera/emotion_recognition.py
"""
Recognizes emotions from detected faces in images.
"""

class EmotionRecognizer:
    def __init__(self):
        self.emotions = []

    def analyze(self, faces, image):
        print("Analyzing emotions from detected faces...")
        self.emotions = [{"face": face, "emotion": "neutral"} for face in faces]
        return self.emotions

    def clear_emotions(self):
        self.emotions = []
