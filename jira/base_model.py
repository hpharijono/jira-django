from django.db import models

optional = {
    "null": True,
    "blank": True,
}


class JiraBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
