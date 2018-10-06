from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    photo = models.FileField(upload_to='media/')
    text = models.TextField()
    author =models.ForeignKey('auth.User', on_delete=models.CASCADE) #odnośnik do innego modelu
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

