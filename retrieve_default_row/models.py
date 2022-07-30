from django.db import models


class Setting(models.Model):
    name = models.CharField()
    value = models.CharField()
    is_default = models.BooleanField(db_default=True)

    class Meta:
        ordering = ["pk"]
