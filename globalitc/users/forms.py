# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
#
# from .models import *
#
#
# class StudentSignUpForm(forms.Form):
#     full_name = forms.CharField(max_length=100)
#
#     # def __init__(self, *args, **kwargs):
#     #     super(StudentSignUpForm, self).__init__(*args, **kwargs)
#     #
#     #     for fieldname in ['email', 'password1', 'password2']:
#     #         self.fields[fieldname].help_text = None
#
#     class Meta(UserCreationForm.Meta):
#         model = Student
#         fields = ['email', 'full_name', 'password1', 'password1']
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         Student.objects.create(user=user, full_name=self.cleaned_data.get('full_name'))
#         return user
#
#
# class TeacherSignUpForm(forms.Form):
#     full_name = forms.CharField(max_length=100)
#
#     # def __init__(self, *args, **kwargs):
#     #     super(TeacherSignUpForm, self).__init__(*args, **kwargs)
#     #
#     #     for fieldname in ['username', 'password1', 'password2']:
#     #         self.fields[fieldname].help_text = None
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_teacher = True
#         user.save()
#         Teacher.objects.create(user=user, full_name=self.cleaned_data.get('full_name'))
#         return user
#
#
# class FreelancerSignUpForm(forms.Form):
#     full_name = forms.CharField(max_length=100)
#
#     # def __init__(self, *args, **kwargs):
#     #     super(FreelancerSignUpForm, self).__init__(*args, **kwargs)
#     #
#     #     for fieldname in ['username', 'password1', 'password2']:
#     #         self.fields[fieldname].help_text = None
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_freelancer = True
#         user.save()
#         Freelancer.objects.create(user=user, full_name=self.cleaned_data.get('full_name'))
#         return user
#
#
# class GuestSignUpForm(forms.Form):
#     full_name = forms.CharField(max_length=100)
#
#     # def __init__(self, *args, **kwargs):
#     #     super(GuestSignUpForm, self).__init__(*args, **kwargs)
#     #
#     #     for fieldname in ['username', 'password1', 'password2']:
#     #         self.fields[fieldname].help_text = None
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_guest = True
#         user.save()
#         Guest.objects.create(user=user, full_name=self.cleaned_data.get('full_name'))
#         return user
#
#
# class EducationCenterSignUpForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     director = forms.CharField(max_length=100)
#     phone_number = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=100)
#     address = forms.CharField(max_length=100)
#     cooperation = forms.ModelChoiceField(queryset=Cooperation.objects.all(), empty_label='Համագործակցության նպատակը')
#     institution = forms.ModelChoiceField(queryset=Institution.objects.all(), empty_label='Ուս․ Հաստատության տեսակը')
#
#     # def __init__(self, *args, **kwargs):
#     #     super(EducationCenterSignUpForm, self).__init__(*args, **kwargs)
#     #
#     #     for fieldname in ['username', 'password1', 'password2']:
#     #         self.fields[fieldname].help_text = None
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_edcenter = True
#         user.save()
#         EducationCenter.objects.create(user=user, name=self.cleaned_data.get('name'),
#                                        director=self.cleaned_data.get('director'),
#                                        phone_number=self.cleaned_data.get('phone_number'),
#                                        email=self.cleaned_data.get('email'),
#                                        address=self.cleaned_data.get('address'),
#                                        cooperation=self.cleaned_data.get('cooperation'),
#                                        institution=self.cleaned_data.get('institution'),
#                                        )
#         return user
#
#
# class PartnerSignUpForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     director = forms.CharField(max_length=100)
#     phone_number = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=100)
#     address = forms.CharField(max_length=100)
#     cooperation = forms.ModelChoiceField(queryset=Cooperation.objects.all(), empty_label='Համագործակցության նպատակը')
#     activity = forms.ModelChoiceField(queryset=Activity.objects.all(), empty_label='Գործունեության ոլորտը')
#
#     # def __init__(self, *args, **kwargs):
#     #     super(PartnerSignUpForm, self).__init__(*args, **kwargs)
#     #
#     #     for fieldname in ['username', 'password1', 'password2']:
#     #         self.fields[fieldname].help_text = None
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_partner = True
#         user.save()
#         Partner.objects.create(user=user, name=self.cleaned_data.get('name'),
#                                director=self.cleaned_data.get('director'),
#                                phone_number=self.cleaned_data.get('phone_number'),
#                                email=self.cleaned_data.get('email'),
#                                address=self.cleaned_data.get('address'),
#                                cooperation=self.cleaned_data.get('cooperation'),
#                                activity=self.cleaned_data.get('activity'))
#
#         return user
