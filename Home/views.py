from django.shortcuts import render
from django.views.generic import ListView
from Home.models import Specialties,Condition,Procedures,Doctor

# Create your views here.
# Bosh sahifa
def index(request):
    return render(request,'Home/home.html')







#mutaxasislar ro'yxati
class SpecialtiesList(ListView):
    model = Specialties
    context_object_name = 'specailties'
    template_name='Home/specailties.html'





#mutaxasis bo'yicha doctorlar ro'yxati
def specialties_doctor(request,doctor_id):
    specialties=Specialties.objects.get(id=doctor_id)
    doctor=specialties.doctor_set.order_by('name')
    context={
    'specialties':specialties,
    'doctor':doctor
    
    
    }
    return render(request,'Home/specialties_doctor.html',context)



#kassaliklar ro'yxati
class ConditionList(ListView):
    model = Condition
    context_object_name = 'condition'
    template_name='Home/condition.html'




#kassalik bo'yicha doctorlar
def condition_doctor(request,doctor_id):
    condition=Condition.objects.get(id=doctor_id)
    specialties=Specialties.objects.filter(name=condition.specialties_id).get()
    doctor=specialties.doctor_set.order_by('name')
    context={
        'condition':condition,
        'specialties':specialties,
        'doctor':doctor
    }
    return render(request,'Home/condition_doctor.html',context)




#operatsiyalar ro'yxati
class ProceduresList(ListView):
    model = Procedures
    context_object_name = 'procedures'
    template_name='Home/procedures.html'


#operatsiya bo'yicha doctorlar
def procedures_doctor(request,doctor_id):
    procedures=Procedures.objects.get(id=doctor_id)
    specialties=Specialties.objects.filter(name=procedures.specialties_id).get()
    doctor=specialties.doctor_set.order_by('name')
    context={
        'procedures':procedures,
        'specialties':specialties,
        'doctor':doctor
    }
    return render(request,'Home/procecdures_doctor.html',context)
