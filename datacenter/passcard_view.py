import datetime

from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at is None:
        return localtime() - visit.entered_at
    else:
        return visit.leaved_at - visit.entered_at


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    time = datetime.time(hour=int(hours), minute=int(minutes))
    return time.strftime('%H:%M')
