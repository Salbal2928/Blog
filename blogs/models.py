from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(null=False, blank=False, max_length=50)
    content = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.title