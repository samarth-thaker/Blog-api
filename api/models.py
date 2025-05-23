from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.CharField(max_length=50, blank=True)
    published_date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title