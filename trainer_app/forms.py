from django.forms import ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from common_app.models import objective, activity


class ObjectiveForm(ModelForm):
    class Meta:
        model = objective
        fields = ['name', 'activities']
