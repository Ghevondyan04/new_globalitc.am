from django.shortcuts import render
from .models import NewsHeader, Offer, News


def home_view(request):
    header_data = NewsHeader.objects.all()
    offer_data = Offer.objects.all()
    news_data = News.objects.all()

    context = {
        "header_data": header_data,
        "offer_data": offer_data,
        "news_data": news_data,

    }

    return render(request, 'news.html', context)
# Create your views here.
