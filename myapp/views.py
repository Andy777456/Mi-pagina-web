from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = " El Poder de la Perseverancia!!"
    return render(request, "index.html", {
        "title": title
    })


def about(request):
    username = "Andy"
    return render(request, "about.html", {
        "username": username
    })


def hello(request, username):
    return HttpResponse("<h1/>reto de las flexiones %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })


def tasks(request):
    # task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })

def task_delete(request, task_id):
    # get_object_or_404 busca la tarea o devuelve un error 404 si no la encuentra.
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        # Redirigimos al usuario de vuelta a la lista de tareas.
        return redirect('tasks')
    # Si el método no es POST, simplemente redirigimos.
    return redirect('tasks')

def task_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.done = True
        task.save()
        return redirect('tasks')
    return redirect('tasks')


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {
            "form": CreateNewTask()
        })
    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                project=form.cleaned_data["project"],
            )
            return redirect("tasks")
    else:
        Task.objects.create(
            title=request.POST["title"], description=request.POST["description"], project_id=2)
        return redirect("tasks")
        form = CreateNewTask()
    return render(request, "tasks/create_task.html", {"form": form})


def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            "form": CreateNewProject()
        })
    else:
     Project.objects.create(name=request.POST["name"])
    return redirect("projects")


def project_detail(request, id):
   project = get_object_or_404(Project, id=id)
   tasks = Task.objects.all()
   return render(request, "projects/detail.html", {
       'project': project,
       "tasks": tasks
   })

       
