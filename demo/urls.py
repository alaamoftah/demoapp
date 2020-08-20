from django.conf.urls import url
from django.contrib import admin

from demoapp.views import index, about, contact_us, clear

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index, name='index'),
    url(r'^about/$',about, name='about'),
    url(r'^contact/$',contact_us, name='contact'),
    url(r'^clear/$',clear, name='clear'),
]
