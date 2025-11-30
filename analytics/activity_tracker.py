# analytics/activity_tracker.py
"""
Tracks user activity across apps, tasks, and workflows.
Generates logs and heatmaps for focus analysis.
"""

class ActivityTracker:
    def __init__(self):
        self.activity_log = []

    def log_action(self, app_name, action, timestamp):
        entry = {"app": app_name, "action": action, "time": timestamp}
        self.activity_log.append(entry)

    def get_activity_log(self):
        return self.activity_log

    def clear_log(self):
        self.activity_log = []
