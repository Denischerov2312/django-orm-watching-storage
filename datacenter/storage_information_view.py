from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import datetime


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    time = datetime.time(hour=int(hours), minute=int(minutes))
    return time.strftime('%H:%M')


def get_duration(visit):
    if visit.leaved_at is None:
        return localtime() - visit.entered_at
    else:
        return visit.leaved_at - visit.entered_at


def get_non_closed_visits(visits):
    non_closed_visits = []
    for visit in visits:
        passcard = visit.passcard
        duration = get_duration(visit)
        visit_info = {
            'who_entered': passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(duration)
        }
        non_closed_visits.append(visit_info)
    return non_closed_visits


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = get_non_closed_visits(visits)
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
