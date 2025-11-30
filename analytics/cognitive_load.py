# analytics/cognitive_load.py
"""
Analyzes user cognitive load and stress levels
based on activity patterns.
"""

class CognitiveLoadAnalyzer:
    def __init__(self):
        self.load_data = []

    def add_measurement(self, focus_level, stress_level, timestamp):
        entry = {"focus": focus_level, "stress": stress_level, "time": timestamp}
        self.load_data.append(entry)

    def get_load_summary(self):
        total_entries = len(self.load_data)
        if total_entries == 0:
            return {"avg_focus": 0, "avg_stress": 0}
        avg_focus = sum(d["focus"] for d in self.load_data) / total_entries
        avg_stress = sum(d["stress"] for d in self.load_data) / total_entries
        return {"avg_focus": avg_focus, "avg_stress": avg_stress}

    def clear_data(self):
        self.load_data = []
