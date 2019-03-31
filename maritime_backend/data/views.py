from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Report
# Create your views here.
def index(request):
    data = Report.objects.filter(id=1)
    data = list(data.values())
    return JsonResponse({'data':data}, safe=False)

def location(request):
    return JsonResponse({"lat": 25, "long": 13})

def individual(request, report_id):
    data = Report.objects.filter(id=report_id)
    data = list(data.values())
    return JsonResponse({'data':data}, safe=False)