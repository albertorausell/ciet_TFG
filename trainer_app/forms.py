from django.forms import ChoiceField, CheckboxInput, CheckboxSelectMultiple, TextInput, Form, ImageField, Textarea, ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from common_app.models import training_technique, objective, activity, capability, stakeholders, content, dimension


class ObjectiveForm(ModelForm):
    class Meta:
        model = objective
        fields = ['name', 'activities']


class CapabilityName(Form):
    cap_name = CharField(max_length=100, required=True, label=False, widget=TextInput(attrs={
        'class': 'col-7'
    }))


class CapabilityDesc(Form):
    cap_desc = CharField(widget=Textarea, required=True, label=False)
    cap_image = ImageField(required=True, label=False)


class CapabilityLearners(ModelForm):
    stakeholders = ModelMultipleChoiceField(
        queryset=stakeholders.objects.all(),
        widget=CheckboxSelectMultiple,
        required=True,
        label=False
    )

    class Meta:
        model = capability
        fields = ['stakeholders']


class CapabilityObjectives(ModelForm):
    objectives = ModelMultipleChoiceField(
        queryset=objective.objects.all(),
        widget=CheckboxSelectMultiple,
        required=True,
        label=False
    )

    class Meta:
        model = capability
        fields = ['objectives']


class Contents(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['dimension'].required = True

    class Meta:
        model = content
        fields = ['name', 'dimension']


class Component(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['types'].required = True
        self.fields['reference'].required = True

    class Meta:
        model = training_technique
        fields = ['types', 'reference']
