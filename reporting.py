# analytics/reporting.py
"""
Creates daily/weekly/monthly analytics reports for users.
"""

class Reporting:
    def __init__(self):
        self.reports = []

    def generate_summary(self, activity_log, load_summary, metrics):
        summary = {
            "activity_entries": len(activity_log),
            "avg_focus": load_summary.get("avg_focus", 0),
            "avg_stress": load_summary.get("avg_stress", 0),
            "metrics_logged": len(metrics)
        }
        self.reports.append(summary)
        return summary

    def get_reports(self):
        return self.reports

    def clear_reports(self):
        self.reports = []
