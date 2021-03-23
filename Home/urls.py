from django.contrib import admin
from django.urls import path,include
from Home import views

from .views import(
    SpecialtiesList,
    ProceduresList,
    ConditionList,
)
app_name='Home'
urlpatterns = [
    path('',views.index,name='index'),


    #Specialties
    path('specialties/',SpecialtiesList.as_view(),name='specialties'),
    path('specialties/doctor/<int:doctor_id>/',views.specialties_doctor,name='specialties_doctor'),
    #Procedures
    path('procedures/',ProceduresList.as_view(),name='procedures'),
    path('procedures/doctor/<int:doctor_id>/',views.procedures_doctor,name='procedures_doctor'),
    #Condition
    path('condition/',ConditionList.as_view(),name='condition'),
    path('condition/doctor/<int:doctor_id>/',views.condition_doctor,name='condition_doctor'),
    
]
