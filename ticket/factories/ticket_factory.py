import factory

from project.factories.project_factory import ProjectFactory
from ticket.models import Ticket


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    title = factory.Sequence(lambda n: f"Ticket #{n}")
    description = factory.LazyAttribute(lambda obj: f"Description for {obj.title}")
    project = factory.SubFactory(ProjectFactory)
