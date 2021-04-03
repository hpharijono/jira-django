from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ticket.views import TicketViewSet

router = DefaultRouter()
router.register("", TicketViewSet)

urlpatterns = [path("", include(router.urls))]
