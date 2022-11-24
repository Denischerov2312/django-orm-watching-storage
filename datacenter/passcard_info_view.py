from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.passcard_view import get_duration
from datacenter.passcard_view import format_duration


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return not duration < minutes * 60


def get_passcard_visits(visits):
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
    this_passcard_visits = get_passcard_visits(visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
