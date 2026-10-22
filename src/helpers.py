# Utility functions for AI Attendance processing

def calculate_attendance_rate(present_count, total_classes):
    """Calculates the overall attendance percentage"""
    if total_classes == 0:
        return 0
    return round((present_count / total_classes) * 100, 2)

