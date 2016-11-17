"""velokrua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from velo.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?:page/)?(\d+)?$', home, name='home'),
    url(r'^calendar', calendar, name='calendar'),
    url(r'^about', about, name='about'),
    # #    url(r'^forum', 'velo.content.views.forum', name='forum'),
    url(r'^contacts', contacts, name='contacts'),
    url(r'^shops', shops, name='shops'),
    url(r'^map', online_map, name='online_map'),
    url(r'^nav', nav, name='navigation'),
    url(r'^download/(.+)$', download, name='download'),
    url(r'^trips/(.+)?', trip, name='trip'),
    url(r'^signin$', signin, name='signin'),

    # Apps
    # (r'^forum/', include('djangobb_forum.urls', namespace='djangobb'), name='forum'),
    # url(r'^$', home, name='forum')
    url('', include('django.contrib.auth.urls')),
]
