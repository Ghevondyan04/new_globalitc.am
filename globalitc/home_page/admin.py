from django.contrib import admin
from .models import HeaderModels, Faculties, FacultyCourse, Services,OtherServices,Partners

admin.site.site_header = 'Global IT admin panel'
admin.site.register(HeaderModels)
admin.site.register(Faculties)
admin.site.register(FacultyCourse)
admin.site.register(Services)
admin.site.register(OtherServices)

# Register your models here.
