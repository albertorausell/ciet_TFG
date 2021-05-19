from django.db.models.base import Model
from django.forms import FileInput, ChoiceField, CheckboxInput, CheckboxSelectMultiple, TextInput, Form, ImageField, Textarea, ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from common_app.models import text_component, image_component, video_component, document_component, link_component, game_component, training_technique, objective, activity, capability, stakeholders, content, dimension


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


class Text(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 300; padding: 10'
        })

    class Meta:
        model = text_component
        fields = ['value']


class Image(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True

    class Meta:
        model = image_component
        fields = ['value']


class Video(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = FileInput(attrs={'accept': '.mp4'})

    class Meta:
        model = video_component
        fields = ['value']


class Document(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True

    class Meta:
        model = document_component
        fields = ['value']


class Link(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = TextInput(attrs={'style': 'width: 100%'})

    class Meta:
        model = link_component
        fields = ['value']


class Game(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = TextInput(attrs={'style': 'width: 100%'})

    class Meta:
        model = game_component
        fields = ['value']
