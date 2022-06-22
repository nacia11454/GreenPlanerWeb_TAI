from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('plant/', views.plant_list, name="plant_list"),
    path('add_plant/',views.add_plant, name = "add_plant"),
    path('add_task/',views.add_task, name = "add_task"),
    path('plant/<plant_id>/', views.plant, name="plant"),

]
