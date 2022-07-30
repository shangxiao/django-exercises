from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    class Meta:
        ordering = ["pk"]
