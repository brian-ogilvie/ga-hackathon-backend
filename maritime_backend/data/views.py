from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from data.data_app import script

from django.db.models import Q

from .models import Report
# Create your views here.
def index(request):
    data = Report.objects.get(pk=1)
    vessel_record = data.vessel.captain

    print(vessel_record)
    return JsonResponse({'data': data}, safe=False)

def location(request):
    return JsonResponse({"lat": 25, "long": 13})

def individual(request, report_id):
    data = Report.objects.filter(id=report_id)
    data = list(data.values())
    return JsonResponse({'data':data}, safe=False)

def vessel_record(request, vessel_id):
    report = Report.objects.filter(vessel= vessel_id, speed_through_water__isnull=False, speed_over_ground__isnull=False, eta_local__isnull=False, eta_utc__isnull=False).order_by('id')[:20]
    data = Report.objects.filter(vessel= vessel_id).select_related('vessel')[:20]

    vessel_name = data[0].vessel.vessel_name

    report = list(report.values())


    return JsonResponse({'vessel_name': vessel_name, 'data': report }, safe=False)


def current_record(request):
    vessel1 = Report.objects.filter(vessel = 1, speed_through_water__isnull=False, speed_over_ground__isnull=False, eta_local__isnull=False, eta_utc__isnull=False)[:1]
    vessel1 = list(vessel1.values())
    vessel2 = Report.objects.filter(vessel = 2, speed_through_water__isnull=False, speed_over_ground__isnull=False, eta_local__isnull=False, eta_utc__isnull=False)[:1]
    vessel2 = list(vessel2.values())
    vessel3 = Report.objects.filter(vessel = 3, speed_through_water__isnull=False, speed_over_ground__isnull=False, eta_local__isnull=False, eta_utc__isnull=False)[:1]
    vessel3 = list(vessel3.values())
    vessel4 = Report.objects.filter(vessel = 4, speed_through_water__isnull=False, speed_over_ground__isnull=False, eta_local__isnull=False, eta_utc__isnull=False)[:1]
    vessel4 = list(vessel4.values())

    return JsonResponse({'Nina': vessel1, 'Santa Maria':vessel2, 'Pinta':vessel3, 'Mayflower':vessel4}, safe=False)