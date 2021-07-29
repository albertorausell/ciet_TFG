from django.db.models.base import Model
from django.forms import FileInput, ChoiceField, CheckboxInput, CheckboxSelectMultiple, TextInput, Form, ImageField, Textarea, ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from common_app.models import excel, text_component, image_component, video_component, document_component, link_component, game_component, training_technique, objective, activity, capability, stakeholders, content, dimension


class ObjectiveForm(ModelForm):
    class Meta:
        model = objective
        fields = ['name', 'activities']


class CapabilityName(Form):
    cap_name = CharField(max_length=100, required=True, label=False, widget=TextInput(attrs={
        'class': 'col-7'
    }))


class CapabilityDesc(Form):
    cap_desc = CharField(widget=Textarea(attrs={
        'style': 'width: 100%;',
        'placeholder': 'Here the description...'
    }), required=True, label=False)
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


class Excel_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document'].required = True
        self.fields['document'].widget = FileInput(attrs={'accept': '.xlsx'})

    class Meta:
        model = excel
        fields = ['document']


class Text(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 300; padding: 10',
            'placeholder': 'Here the text...'
        })

    class Meta:
        model = text_component
        fields = ['value']


class Image(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['description'].required = False
        self.fields['description'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 100; padding: 10;border-color: darkgray;',
            'placeholder': 'Add a comment...'
        })

    class Meta:
        model = image_component
        fields = ['value', 'description']


class Video(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = FileInput(attrs={'accept': '.mp4'})
        self.fields['description'].required = False
        self.fields['description'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 100; padding: 10;border-color: darkgray;',
            'placeholder': 'Add a comment...'
        })

    class Meta:
        model = video_component
        fields = ['value', 'description']


class Document(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['description'].required = False
        self.fields['description'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 100; padding: 10;border-color: darkgray;',
            'placeholder': 'Add a comment...'
        })

    class Meta:
        model = document_component
        fields = ['value', 'description']


class Link(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = TextInput(attrs={
            'style': 'width: 100%; padding-left:10',
            'placeholder': 'Link to the page'
        })
        self.fields['description'].required = False
        self.fields['description'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 100; padding: 10;border-color: darkgray;',
            'placeholder': 'Add a comment...'
        })

    class Meta:
        model = link_component
        fields = ['value', 'description']


class Game(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].required = True
        self.fields['value'].widget = TextInput(attrs={
            'style': 'width: 100%; padding-left:10',
            'placeholder': 'Link to the game'
        })
        self.fields['description'].required = False
        self.fields['description'].widget = Textarea(attrs={
            'style': 'width: 100%; height: 100; padding: 10;border-color: darkgray;',
            'placeholder': 'Add a comment...'
        })

    class Meta:
        model = game_component
        fields = ['value', 'description']
