from django.db import models


class HeaderModels(models.Model):
    header_title = models.CharField(max_length=100)
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
    slug = models.SlugField(unique=True, max_length=15)

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


class FacultiesDescriptions(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    context = models.TextField()
    image = models.ImageField(upload_to="CourseDescription")

    def __str__(self):
        return f'{self.course} {self.name}'


class CourseCourses(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    context = models.TextField()
    period = models.CharField(max_length=30)
    vacation = models.CharField(max_length=30)
    image = models.ImageField(upload_to="CourseCourses")

    def __str__(self):
        return f'{self.course} {self.name}'


class CourseInclude(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="CourseCourses")

    def __str__(self):
        return f'{self.course} {self.name}'


class CourseLevels(models.Model):
    levels_list = [
        (1, "LevelOne"),
        (2, "LevelTwo"),
        (3, "LevelThree")
    ]

    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    level = models.IntegerField(choices=levels_list)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.course} {self.name}'


class CourseVideo(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    video = models.FileField()
    video_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f'{self.course}'


class CourseTeachers(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="CourseTeachers")
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()

    def __str__(self):
        return f'{self.course} {self.full_name}'


class CourseCertificate(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="CourseCertificate")
    full_name = models.CharField(max_length=30)
    context = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'{self.course} {self.full_name}'


class CourseComments(models.Model):
    course = models.ForeignKey(FacultyCourse, on_delete=models.CASCADE)


class Services(models.Model):
    service_title = models.CharField(max_length=30)
    service_image = models.ImageField(upload_to="ServicesImages")
    service_icon = models.ImageField(upload_to="ServicesIcons")
    in_home_page = models.BooleanField(default=True)
    where_in_menu = models.IntegerField(verbose_name="Մենույի ո՞ր սյունակում լինի(1,2,3)")

    def __str__(self):
        return f"{self.service_title}"


class OtherServices(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="OtherServicesImages")
    service_icon = models.ImageField(upload_to="OtherServicesIcons")
    in_home_page = models.BooleanField(default=True)
    where_in_menu = models.IntegerField(verbose_name="Մենույի ո՞ր սյունակում լինի(1,2)")

    def __str__(self):
        return f"{self.title}"


class Partners(models.Model):
    partner_logo = models.ImageField(upload_to="PartnersImages")
    partner_link = models.URLField(max_length=200)
