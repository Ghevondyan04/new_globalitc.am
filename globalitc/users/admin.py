from django.contrib import admin
from .models import *

admin.site.site_header = 'Global IT admin panel'
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Freelancer)
admin.site.register(Guest)
admin.site.register(EducationCenter)
admin.site.register(Partner)
admin.site.register(Institution)
admin.site.register(Activity)
admin.site.register(Cooperation)
