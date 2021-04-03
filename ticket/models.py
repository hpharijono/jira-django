from django.contrib.auth.models import User
from django.db import models

from jira.base_model import JiraBaseModel, optional
from project.models import Project


class Ticket(JiraBaseModel):
    TODO = "To Do"
    INPROGRESS = "In Progress"
    TOREVIEW = "To Review"
    DONE = "Done"
    STATUS_CHOICES = [TODO, INPROGRESS, TOREVIEW, DONE]

    title = models.CharField(max_length=255)
    description = models.TextField(**optional)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tickets"
    )
    assignee = models.ForeignKey(
        User, **optional, on_delete=models.CASCADE, related_name="tickets"
    )
    status = models.CharField(
        max_length=20, choices=[(x, x) for x in STATUS_CHOICES], default=TODO
    )
