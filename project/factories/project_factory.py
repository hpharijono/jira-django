import factory

from project.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: f"Test Project {n}")
    code = factory.Sequence(lambda n: f"TP{n}")
