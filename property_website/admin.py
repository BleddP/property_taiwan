from django.contrib import admin
from .models import Agent, User, Property, Station, School, City, Area, PropertyType

# Register your models here.
admin.site.register(Agent)
admin.site.register(User)
admin.site.register(Property)
admin.site.register(Station)
admin.site.register(School)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(PropertyType)
