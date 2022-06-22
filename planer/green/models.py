from django.db import models

class Plant_species(models.Model):
    name_species = models.CharField('Species Name', max_length = 100)

    def __str__(self):
        return self.name_species

class Plant(models.Model):
    plant_name = models.CharField('Plant Name', max_length = 100)
    plant_species = models.ForeignKey(Plant_species, on_delete=models.CASCADE)
    plant_photo = models.URLField('Plant Photo')

    def __str__(self):
        return self.plant_name

class GreenUser(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Task(models.Model):
    task_title = models.CharField('Task Title', max_length = 100)
    task_date = models.DateTimeField('Task Date')
    task_note = models.TextField(blank=True)
    task_status = models.IntegerField(default=0)
    task_plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task_user = models.ForeignKey(GreenUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

