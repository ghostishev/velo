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
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

from velo.views import *

from djangobb_forum import settings as forum_settings
from djangobb_forum.sitemap import SitemapForum, SitemapTopic

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

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

    # Apps
    # (r'^forum/', include('djangobb_forum.urls', namespace='djangobb'), name='forum'),
    # url(r'^$', home, name='forum')
    # url('', include('django.contrib.auth.urls')),
    url('', include('registration.urls')),

    # Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    # Apps
    url(r'^forum/account/', include('allauth.urls')),
    url(r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
]

# PM Extension
if forum_settings.PM_SUPPORT:
    urlpatterns += [
        url(r'^forum/pm/', include('django_messages.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
