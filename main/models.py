from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=1000)

    class Meta:
        label = "name"

class Carousel(models.Model):
    name = models.CharField(max_length=50, default='ineedaname')
    images = models.ManyToManyField(Image)

    class Meta:
        label = "name"

class NewsItem(models.Model):
    markdown = models.CharField(max_length=20000)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
        label = "published_at"

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50000)
    releases = models.ManyToManyField('Release', blank=True)
    spotifylink = models.CharField(max_length=1000)
    soundcloudlink = models.CharField(max_length=1000)
    bandcamplink = models.CharField(max_length=1000)
    applemusiclink = models.CharField(max_length=1000)

    class Meta:
        label = "name"

class Release(models.Model):
    title = models.CharField(max_length=200)
    typevideotrack = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    releasedate = models.DateField()
    link = models.CharField(max_length=1000)

    class Meta:
        label = "title"
