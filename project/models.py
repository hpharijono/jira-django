from django.db import models

from jira.base_model import JiraBaseModel


class Project(JiraBaseModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
