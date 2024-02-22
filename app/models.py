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
    decimal_field = models.DecimalField( max_digits = 5, decimal_places = 2)
    duration_field = models.DurationField()
    email_field = models.EmailField(max_length=16)
    float_field = models.FloatField(max_length=5)
    file_field = models.FileField(upload_to="%Y/%m/%d/", blank = True,verbose_name="File yuklash ")
    
    def __str__(self) -> str:
        return str(self.datetime_aut) + " " + str(self.decimal_field) + " " + str(self.duration_field) +" Email: "+ str(self.email_field) + " Float field: " + str(self.float_field)
    
class RoboContest(models.Model):
    ism = models.CharField(verbose_name = "Ism ", max_length = 10)
    familya = models.CharField(verbose_name = "Familya ", max_length = 12)
    email_faild = models.EmailField(verbose_name = "Elektron poshta manzili", max_length=20)
    phone_field = models.IntegerField(verbose_name = "Telefon raqam ", max_length = 10)
    taxallus_field = models.CharField(verbose_name="Taxallus ", max_length = 10)
    viloyat = models.CharField(verbose_name="Viloyat ", max_length = 12)
    Tuman = models.CharField(verbose_name="Tuman ", max_length = 10)
    talim = models.TextField(verbose_name="O'qish joy ")
    kurs = models.IntegerField(verbose_name="Kursi yoki sinifi ", max_length = 2)
    bool_field = models.BooleanField(verbose_name="Agar o'qish jpyingiz yuqorida qayd etilmagan bo'lsa yoki biror joyda ishlasangiz buni tanlang va quyidagilarni to'ldiring")
    now_date = models.DateField(verbose_name = "Ro'yxatdan o'tilgan kun")
    now_time = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.ism + " " + self.familya + " " + str(self.email_faild) + " " + str(self.phone_field)  + " "+ str(self.kurs) + " "+str(self.bool_field) + " " + str(self.now_date)
    