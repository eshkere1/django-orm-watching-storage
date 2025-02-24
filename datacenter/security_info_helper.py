from django.utils.timezone import localtime
from django.utils import timezone
from datetime import datetime

def is_visit_long(duration, minutes=60):
    seconds_in_minute = 60
    minutes = minutes * seconds_in_minute
    minutes_on = duration.total_seconds() > minutes
    return minutes_on


def get_duration(visit, date_now):
    entered_local_time = localtime(visit.entered_at)
    if visit.leaved_at:
        leaved_local_time = localtime(visit.leaved_at)
        delta = leaved_local_time - entered_local_time
    else:
        delta = date_now - entered_local_time
    return delta


def format_duration(duration):
    seconds = duration.total_seconds()
    seconds_in_hour = 3600
    seconds_in_minute = 60
    hours = int(seconds // seconds_in_hour)
    minutes = int((seconds % seconds_in_hour) // seconds_in_minute)
    seconds = int(seconds % seconds_in_minute)
    return f"{hours:02}:{minutes:02}:{seconds:02}"
