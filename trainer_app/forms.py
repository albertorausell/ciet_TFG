from django.forms import ModelForm
from common_app.models import objective


class ObjectiveForm(ModelForm):
    class Meta:
        model = objective
        fields = ['name', 'activities']
