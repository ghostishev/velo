from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    title = models.CharField(_('title'), max_length=128)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    announce_text = models.TextField(_('announce'), max_length=512, blank=True)
    text = models.TextField(_('text'), max_length=4096)

    def __str__(self):
        return self.title

    @property
    def announce(self):
        return self.announce_text or self.text[:512].rsplit(' ', 1)[0]

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('article')
        verbose_name_plural = _('articles')


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, related_name="user")
    date = models.DateTimeField(True)
    name = models.CharField(max_length=128)
    content = models.TextField()

    class Meta:
        ordering = ["-date"]

    def __unicode__(self):
        return self.name


class About(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_us = models.TextField()

    def __unicode__(self):
        return self.about_us


class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    tel = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    about_shop = models.TextField()

    def __unicode__(self):
        return self.name


class Navfiles(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.TextField()
    count = models.IntegerField()
    last_download = models.DateTimeField(True)

    def __unicode__(self):
        return self.filename


class Trips(models.Model):
    trip_id = models.AutoField(primary_key=True)
    trip_name = models.CharField(max_length=255)
    gpsies_id = models.CharField(max_length=128)

    class Meta:
        ordering = ["-trip_name"]
