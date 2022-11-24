import datetime

from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at is None:
        return (localtime() - visit.entered_at).total_seconds()
    else:
        return (visit.leaved_at - visit.entered_at).total_seconds()


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    time = datetime.time(hour=int(hours), minute=int(minutes))
    return time.strftime('%H:%M')


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > minutes * 60
