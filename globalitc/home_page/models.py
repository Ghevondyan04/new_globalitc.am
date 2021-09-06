from django.db import models


class HeaderModels(models.Model):
    header_title = models.CharField()
    header_context = models.CharField(max_length=500)
    header_image = models.ImageField(upload_to="HeaderImages")
    in_page = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.header_title}"


class Faculties(models.Model):
    fac_title = models.CharField(max_length=30)
    fac_image = models.ImageField(upload_to="FacultiesImages")
    fac_icon = models.ImageField(upload_to="FacultiesIcons")
    large_icon = models.ImageField(upload_to="FacultiesLargeIcons")

    def __str__(self):
        return f"{self.fac_title}"


class FacultyCourse(models.Model):
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=30)
    course_time = models.CharField(max_length=15)
    course_pay = models.CharField(max_length=30)
    course_image = models.ImageField(upload_to="FacultyCourseImages")
    course_icon = models.ImageField(upload_to="CourseIcons")

    def __str__(self):
        return f"{self.course_title}"


class Services(models.Model):
    service_title = models.CharField(max_length=30)
    service_image = models.ImageField(upload_to="ServicesImages")
    other_service = models.BooleanField(default=False)
    in_home_page = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.service_title}"


class Partners(models.Model):
    partner_logo = models.ImageField(upload_to="PartnersImages")
    partner_link = models.URLField(max_length=200)
