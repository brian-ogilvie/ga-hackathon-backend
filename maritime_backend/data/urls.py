from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:report_id>/', views.individual, name='individual'),
    path('location', views.location, name='location'),
    path('vessel/<int:vessel_id>', views.vessel_record),#20 most recent rows | Name |speed through water| speed over ground | ETA | Port Linup (screenshot) Anomalies |
    path('current', views.current_record)
]