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

