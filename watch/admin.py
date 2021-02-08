from django.contrib import admin
from .models import Profile,Neighborhood,Business,Authority,Hospital,Alert
# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Authority)
admin.site.register(Hospital)
admin.site.register(Alert)