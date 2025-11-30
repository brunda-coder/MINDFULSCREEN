# analytics/utils.py
"""
Helper functions for analytics calculations and formatting.
"""

def format_timestamp(ts):
    return ts.strftime("%Y-%m-%d %H:%M:%S")

def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)
