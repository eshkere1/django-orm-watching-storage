from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.utils import timezone
from datetime import datetime


def get_duration(visit):
    entered_local_time = localtime(visit.entered_at)
    if visit.leaved_at:
        leaved_local_time = localtime(visit.leaved_at)
        delta = leaved_local_time - entered_local_time
    else:
        date_now = localtime(datetime.now(timezone.utc))
        delta = date_now - entered_local_time
    return delta


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours}:{minutes}:{seconds}"


def storage_information_view(request):
    leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits =[]
    for visit in leaved_visits:
        duration = get_duration(visit)
        print(duration)
        visit_time = format_duration(duration)
        print(visit_time)
        entered_local_time = localtime(visit.entered_at)
        persone = visit.passcard
        non_closed_visits.append (
            {
                'who_entered': persone,
                'entered_at': entered_local_time,
                'duration': visit_time,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

