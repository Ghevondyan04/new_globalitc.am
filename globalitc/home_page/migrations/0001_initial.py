# Generated by Django 3.2.7 on 2021-09-14 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_title', models.CharField(max_length=30)),
                ('fac_image', models.ImageField(upload_to='FacultiesImages')),
                ('fac_icon', models.ImageField(upload_to='FacultiesIcons')),
                ('large_icon', models.ImageField(upload_to='FacultiesLargeIcons')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(max_length=100)),
                ('header_context', models.CharField(max_length=500)),
                ('header_image', models.ImageField(upload_to='HeaderImages')),
                ('in_page', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OtherServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='OtherServicesImages')),
                ('service_icon', models.ImageField(upload_to='OtherServicesIcons')),
                ('in_home_page', models.BooleanField(default=True)),
                ('where_in_menu', models.IntegerField(verbose_name='Մենույի ո՞ր սյունակում լինի(1,2)')),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_logo', models.ImageField(upload_to='PartnersImages')),
                ('partner_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=30)),
                ('service_image', models.ImageField(upload_to='ServicesImages')),
                ('service_icon', models.ImageField(upload_to='ServicesIcons')),
                ('in_home_page', models.BooleanField(default=True)),
                ('where_in_menu', models.IntegerField(verbose_name='Մենույի ո՞ր սյունակում լինի(1,2,3)')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=30)),
                ('course_time', models.CharField(max_length=15)),
                ('course_pay', models.CharField(max_length=30)),
                ('course_image', models.ImageField(upload_to='FacultyCourseImages')),
                ('course_icon', models.ImageField(upload_to='CourseIcons')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.faculties')),
            ],
        ),
    ]
