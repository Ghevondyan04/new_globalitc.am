from django.contrib import admin
from .models import HeaderModels, Faculties, FacultyCourse, Services, OtherServices, Partners, FacultiesDescriptions, \
    CourseCourses, CourseInclude, CourseLevels, CourseVideo, CourseTeachers, CourseCertificate, CourseComments

admin.site.site_header = 'Global IT admin panel'
admin.site.register(HeaderModels)
admin.site.register(Faculties)
admin.site.register(FacultyCourse)
admin.site.register(Services)
admin.site.register(OtherServices)
admin.site.register(Partners)
admin.site.register(FacultiesDescriptions)
admin.site.register(CourseCourses)
admin.site.register(CourseInclude)
admin.site.register(CourseLevels)
admin.site.register(CourseVideo)
admin.site.register(CourseTeachers)
admin.site.register(CourseCertificate)
admin.site.register(CourseComments)

# Register your models here.
