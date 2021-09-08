from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import HeaderModels, Faculties, FacultyCourse, Services, Partners
from blog_and_contact.models import Offer, News
from blog_and_contact.forms import ContactWithUsForm, SubscribeForm
from .models import Services


# class HomePageView(TemplateView):
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["header_data"] = HeaderModels.objects.all()
#         context["faculties_data"] = Faculties.objects.all()
#         context["faculties_course_data"] = FacultyCourse.objects.all()
#         context["services_data"] = Services.objects.all()
#         context["partners_data"] = Partners.objects.all()
#         context["offers_data"] = Offer.objects.all()
#         context["news_data"] = News.objects.all()
#         return context


def home_view(request):
    header_data = HeaderModels.objects.all()
    faculties_data = Faculties.objects.all()
    faculties_course_data = FacultyCourse.objects.all()
    services_data = Services.objects.all()
    partners_data = Partners.objects.all()
    offers_data = Offer.objects.all()
    news_data = News.objects.all()

    if request.method == 'POST':
        contact_form = ContactWithUsForm(request.POST)
        subscribe_form = SubscribeForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
        if subscribe_form.is_valid():
            subscribe_form.save()

    contact_form = ContactWithUsForm()
    subscribe_form = SubscribeForm()

    context = {
        "header_data": header_data,
        "faculties_data": faculties_data,
        "faculties_course_data": faculties_course_data,
        "services_data": services_data,
        "partners_data": partners_data,
        "offers_data": offers_data,
        "news_data": news_data,
        "contact_form": contact_form,
        "subscribe_form": subscribe_form,
    }

    return render(request, 'index.html', context)


def services_list_view(request):
    services_list = Services.objects.all()

    context = {
        "services_data": services_list,
    }

    return render(request, 'services_list.html', context)
