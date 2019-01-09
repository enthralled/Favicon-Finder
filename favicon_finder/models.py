from django.db import models

class Favicon(models.Model):
    website_name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    fav_url = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website_name