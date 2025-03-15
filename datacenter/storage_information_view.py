from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.utils import timezone
from datacenter.security_info_helper import get_duration, format_duration


def storage_information_view(request):
    leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits =[]
    for visit in leaved_visits:
        date_now = localtime(timezone.now())
        duration = get_duration(visit, date_now)
        visit_time = format_duration(duration)
        entered_local_time = localtime(visit.entered_at)
        person = visit.passcard
        non_closed_visits.append (
            {
                'who_entered': person,
                'entered_at': entered_local_time,
                'duration': visit_time,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

