# Utility functions for AI Attendance processing

def calculate_attendance_rate(present_count, total_classes):
    """Calculates the overall attendance percentage"""
    if total_classes == 0:
        return 0
    return round((present_count / total_classes) * 100, 2)

def format_supabase_timestamp(ts):
    """Parses ISO timestamps from the database"""
    from datetime import datetime
    try:
        return datetime.fromisoformat(ts).strftime('%Y-%m-%d %I:%M %p')
    except:
        return 'Invalid Date'

def is_valid_match(score, threshold=0.65):
    """Validates if the facial/voice match meets the confidence threshold"""
    return score >= threshold

