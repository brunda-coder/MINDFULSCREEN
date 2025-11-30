# analytics/performance.py
"""
Monitors system and application performance metrics.
"""

class PerformanceMonitor:
    def __init__(self):
        self.metrics = []

    def log_metric(self, resource, usage_percent, timestamp):
        entry = {"resource": resource, "usage": usage_percent, "time": timestamp}
        self.metrics.append(entry)

    def get_metrics(self):
        return self.metrics

    def clear_metrics(self):
        self.metrics = []
