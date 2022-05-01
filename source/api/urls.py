from django.urls import path, include
from api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("todo", views.TaskViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls))
]
