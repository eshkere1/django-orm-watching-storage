from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.storage_information_view import get_duration, format_duration



def is_visit_long(duration, minutes=60):
    minutes = minutes * 60
    minutes_on = duration.total_seconds()
    if minutes_on > minutes:
        return True
    return False

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        visit_time = format_duration(duration)
        entered_local_time = localtime(visit.entered_at)
        is_strange = is_visit_long(duration)


        this_passcard_visits.append(
            {
                'entered_at': entered_local_time,
                'duration': visit_time,
                'is_strange':  is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
