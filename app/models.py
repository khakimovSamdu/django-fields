from django.db import models

# Create your models here.
class IT_Markaz(models.Model):
    name = models.CharField(max_length=8, blank = True)
    ticher_count = models.IntegerField()
    talaba_count = models.IntegerField()
    date = models.DateField()
    bool_field = models.BooleanField()
    date_auto = models.DateField(auto_now_add=True)
    date_auto_now = models.DateField(auto_now = True)
    date_time = models.DateTimeField()

    def __str__(self) -> str:
        f = self.name + " " + str(self.ticher_count) + " " + str(self.talaba_count) + " " + str(self.date) + " " + str(self.bool_field) +" Auto now add " + str(self.date_auto) + " Auto now " + str(self.date_auto_now) + " Date time " + str(self.date_time)
        return f
class Samdu(models.Model):
    datetime_aut = models.DateTimeField(auto_now = True)
    