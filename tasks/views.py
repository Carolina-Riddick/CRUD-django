from django.shortcuts import render, redirect
from .models import Tasks
from .form import FormTasks


def get_tasks(request):
    tasks = Tasks.objects.all()  # Esto reemplaza a SELECT * FROM Tasks
    return render(request, 'getTasks.html', {'tasks': tasks})


def create_task(request):
    new_task = Tasks(title=request.POST['task'], description=request.POST['description'])
    new_task.save()
    return redirect('tasks')


def delete_task(request, task_id):
    task_deleted = Tasks.objects.get(id=task_id)
    task_deleted.delete()
    return redirect('tasks')


def update_task(request, task_id):
    updated_task = Tasks.objects.get(id=task_id)
    forms = FormTasks(request.POST or None, instance=updated_task)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('tasks')
    return render(request, 'edit_task.html', {'forms': forms})