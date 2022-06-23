from django.urls import path, include

from greenCalendar.views import HomeView

app_name = 'greenCalendar'

urlpatterns = [
    path('greenCalendar/', HomeView.as_view(), name='home'),
    ]