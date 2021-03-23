from django.db import models
from django.contrib.auth.models import User




# Create your models here.


class Specialties(models.Model):
    name=models.CharField("mutaxasislik", max_length=100)

    def __str__(self):
        return self.name
    






class Province(models.Model):
    name=models.CharField('Viloyat', max_length=50)

    def __str__(self):
        return self.name





class District(models.Model):
    name=models.CharField('Tuman', max_length=50)
    district_id=models.ForeignKey(Province,on_delete=models.CASCADE)

    def __str__(self):
        return self.name






class Work_time(models.Model):
    name=models.CharField('ishlash kunlari', max_length=50)

    def __str__(self):
        return self.name




class Doctor(models.Model):
    name=models.CharField('Doctor ism familiya', max_length=50)
    img=models.ImageField(upload_to = 'images')
    province_id=models.ForeignKey(District, on_delete=models.CASCADE)
    address=models.CharField('address', max_length=100)

    GENDER_CHOICES=(
        ('Erkak','Erkak'),
        ('Ayol','Ayol'),
    )
    gender=models.CharField('Jinsi', max_length=5,choices=GENDER_CHOICES)
    Work_experience=(
        ('<<5','<<5'),
        ('5-10','5-10'),
        ('10-20','10-20'),
        ('20-30','20-30'),
        ('30<<','30<<')
    )
    work_experience=models.CharField('work experience', max_length=5,choices=Work_experience)
    body=models.TextField('Ummumiy malumot')
    age=models.IntegerField('Yoshi')
    specialties_id=models.ForeignKey(Specialties,on_delete=models.CASCADE)
    
    work_time_id=models.ForeignKey(Work_time, on_delete=models.CASCADE)
    phone_number=models.CharField('Raqami', max_length=9)
    date_add=models.DateField('qowilgan vaqt', auto_now=False, auto_now_add=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name




class Condition(models.Model):
    name=models.CharField('Kassalik', max_length=100)
    specialties_id=models.ForeignKey(Specialties, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name




class Procedures(models.Model):
    name=models.CharField('Operatsiya', max_length=100)
    
    specialties_id=models.ForeignKey(Specialties,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



    
    

     