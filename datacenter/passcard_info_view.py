from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404
import datetime


def get_duration(visit):
    if visit.leaved_at is None:
        return localtime() - visit.entered_at
    else:
        return visit.leaved_at - visit.entered_at


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is None:
        return False
    duration = get_duration(visit)
    if duration.total_seconds() < minutes * 60:
        return False
    else:
        return True


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    time = datetime.time(hour=int(hours), minute=int(minutes))
    return time.strftime('%H:%M')


def filter_passcard_visits(visits):
    passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        visit_info = {
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': is_visit_long(visit)
            }
        passcard_visits.append(visit_info)
    return passcard_visits


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = filter_passcard_visits(visits)
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
