from django.forms import ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from common_app.models import objective, activity, capability


class ObjectiveForm(ModelForm):
    class Meta:
        model = objective
        fields = ['name', 'activities']
