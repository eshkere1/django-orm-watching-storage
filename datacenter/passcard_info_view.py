from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.security_info_helper import get_duration, format_duration, is_visit_long
from django.utils import timezone
from datetime import datetime

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        date_now = localtime(datetime.now(timezone.utc))
        duration = get_duration(visit, date_now)
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
