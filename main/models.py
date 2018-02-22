from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

class Carousel(models.Model):
    name = models.CharField(max_length=50, default='ineedaname')
    images = models.ManyToManyField(Image)

    def __unicode__(self):
        return self.name

class News_item(models.Model):
    name = models.CharField(max_length=50, default='ineedaname')
    published_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name + self.published_at

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50000)
    releases = models.ManyToManyField('Release', blank=True)
    spotifylink = models.CharField(max_length=1000)
    soundcloudlink = models.CharField(max_length=1000)
    bandcamplink = models.CharField(max_length=1000)
    applemusiclink = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

class Release(models.Model):
    title = models.CharField(max_length=200)
    typevideotrack = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    releasedate = models.DateField()
    link = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title
