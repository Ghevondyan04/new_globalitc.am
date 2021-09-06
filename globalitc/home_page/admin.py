from django.contrib import admin
from .models import HeaderModels, Faculties, FacultyCourse, Services, ServicesSections, Partners

admin.site.site_header = 'Global IT admin panel'
admin.site.register(HeaderModels)
admin.site.register(Faculties)
admin.site.register(FacultyCourse)
admin.site.register(Services)
admin.site.register(ServicesSections)
admin.site.register(Partners)

# Register your models here.
