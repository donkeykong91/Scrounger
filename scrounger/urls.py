from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^selectfood/', include('selectfood.urls')),
    url(r'^admin/', admin.site.urls),
]
