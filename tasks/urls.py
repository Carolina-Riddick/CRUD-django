from django.urls import path
from .views import get_tasks, create_task, delete_task, update_task

urlpatterns = [
    path('', get_tasks, name='tasks'),
    path('new/', create_task, name='new_task'),
    path('deleted_task/<int:task_id>/', delete_task, name='deleted_task'),
    path('update_task/<int:task_id>/', update_task, name='edit_task')
]
