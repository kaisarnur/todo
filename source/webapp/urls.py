from django.urls import path
from webapp import views as task_views

app_name = "webapp"

urlpatterns = [
    path("", task_views.IndexView.as_view(), name="index"),
    path("task/create/", task_views.TaskCreateView.as_view(), name="task_create"),
    path("task/<int:task_pk>/", task_views.TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/edit/", task_views.TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", task_views.TaskDeleteView.as_view(), name="task_delete"),
]
