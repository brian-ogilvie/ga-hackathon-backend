from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:report_id>/', views.individual, name='individual'),
    path('location', views.location, name='location'),
]