from django.contrib import admin
from Home.models import Doctor,Specialties,Condition,Province,District,Procedures,Work_time
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specialties)
admin.site.register(Condition)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Procedures)
admin.site.register(Work_time)
