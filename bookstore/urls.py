from django.contrib import admin
from django.urls import path , include

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import handler404
from bstore.views import custom_404_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',include('bstore.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_404_view