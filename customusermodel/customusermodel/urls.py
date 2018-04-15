from django.conf.urls import url
from django.contrib import admin

from accounts.views import register, login_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view)
]
