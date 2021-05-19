import uuid

from django.db import models
from django.utils import timezone


class Exchange(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    value = models.FloatField()
    provider = models.CharField(max_length=50)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.provider}: {str(self.value)}'
