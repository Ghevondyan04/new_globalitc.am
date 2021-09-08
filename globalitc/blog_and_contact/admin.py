from django.contrib import admin
from .models import NewsHeader, Offer, News, CallOrder, ContactWithUs, Subscribe

admin.site.site_header = 'Global IT admin panel'
admin.site.register(NewsHeader)
admin.site.register(Offer)
admin.site.register(News)
admin.site.register(CallOrder)
admin.site.register(ContactWithUs)
admin.site.register(Subscribe)
