from django.contrib import admin
from .models import Plant_species, Plant, GreenUser, Task

admin.site.register(Plant_species)
admin.site.register(Plant)
admin.site.register(GreenUser)
admin.site.register(Task)