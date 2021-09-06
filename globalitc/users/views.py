# from django.contrib.auth import login
# from django.shortcuts import redirect, render
# from django.views.generic import CreateView
#
# from .forms import StudentSignUpForm, TeacherSignUpForm, FreelancerSignUpForm, GuestSignUpForm, \
#     EducationCenterSignUpForm, PartnerSignUpForm
# from .models import User
#
#
# def RegisterView(request):
#     return render(request, "register.html")
#
#
# class StudentSignUpView(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'student_register.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return f"ok"
#
#
# class TeacherSignUpView(CreateView):
#     model = User
#     form_class = TeacherSignUpForm
#     template_name = 'teacher_register.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'teacher'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('register')
#
#
# class FreelancerSignUpView(CreateView):
#     model = User
#     form_class = FreelancerSignUpForm
#     template_name = 'freelancer_register.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'freelancer'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('register')
#
#
# class GuestSignUpView(CreateView):
#     model = User
#     form_class = GuestSignUpForm
#     template_name = 'guest_register.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'guest'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('register')
#
#
# class EducationCenterSignUpView(CreateView):
#     model = User
#     form_class = EducationCenterSignUpForm
#     template_name = 'educ_register.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'education_center'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('register')
#
#
# class PartnerSignUpView(CreateView):
#     model = User
#     form_class = PartnerSignUpForm
#     template_name = 'partner_register.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'partner'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('register')