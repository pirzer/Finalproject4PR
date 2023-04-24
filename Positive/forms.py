from django import forms
from .models import Positive
from django_summernote.widgets import SummernoteWidget


class PositiveForm(forms.ModelForm):
    """
    Form for adding a story
    """
    class Meta:
        model = Positive
        fields = [
            'title',
            'excerpt',
            'impact',
            'serves',
            'championship_numbers',
            'team_avg_season',
            'team_avg_playoffs',
            'pitch_the_story',
            'team_image',
        ]

        widgets = {
            'pitch_the_story': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PositiveForm, self).__init__(*args, **kwargs)
