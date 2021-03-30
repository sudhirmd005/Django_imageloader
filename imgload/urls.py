from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView 
urlpatterns = [
    # path('', TemplateView.as_view(template_name="img/signupp.html")),
    path('admin/', admin.site.urls),
    path('', include('img.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
