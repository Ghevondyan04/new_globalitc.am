from django.contrib import admin
from django.urls import path, include
from home_page.views import home_view, services_list_view, fac_program_view, fac_web_program_view, fac_multimedia_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('users.urls')),
    path('', home_view, name="home"),
    path('services', services_list_view, name="services_list"),
    path('faculties/web', fac_web_program_view, name="faculties_web"),
    path('faculties/programming', fac_program_view, name="faculties_programming"),
    path('faculties/multimedia', fac_multimedia_view, name="faculties_multimedia")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
