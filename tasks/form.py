from django.forms import ModelForm
from .models import Tasks


class FormTasks(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'