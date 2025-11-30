# camera/face_detection.py
"""
Detects faces from camera input for recognition and emotion analysis.
"""

class FaceDetector:
    def __init__(self):
        self.faces_detected = []

    def detect_faces(self, image):
        print("Detecting faces in image...")
        # Placeholder: return dummy face coordinates
        self.faces_detected = [{"x": 100, "y": 150, "w": 50, "h": 50}]
        return self.faces_detected

    def clear_faces(self):
        self.faces_detected = []
