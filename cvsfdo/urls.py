from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView, CreateView
from noticias.urls import noticias_patterns
from temporada.urls import temporada_patterns
from posts.urls import post_patterns
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('contacta/', views.contacta, name='contacta'),
    path('temporada/', include(temporada_patterns)),
    path('noticias/', include(noticias_patterns)),
    path('posts/', include(post_patterns)),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)