from django.db import models

from server.apps.core.fields import CreatedField, ModifiedField


class BaseModel(models.Model):
    """Base model."""

    created = CreatedField()
    modified = ModifiedField()

    class Meta:
        abstract = True
