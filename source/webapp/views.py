from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.models import Task
from webapp.forms import TaskForm, TaskCreateForm


class IndexView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "index.html"
    paginate_by = 9


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "create.html"

    def get_success_url(self):
        return reverse("webapp:task_detail", kwargs={"task_pk": self.object.pk})


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "detail.html"
    pk_url_kwarg = "task_pk"


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "update.html"
    form_class = TaskForm
    context_object_name = "task"

    def get_success_url(self):
        return reverse("webapp:task_detail", kwargs={"task_pk": self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy("webapp:index")
    context_object_name = "task"

