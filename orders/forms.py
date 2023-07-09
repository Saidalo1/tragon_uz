from django import forms

from services.models import SubService
from .models import UserFeedback


class UserFeedbackForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=SubService.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = UserFeedback
        fields = ('name', 'phone', 'source', 'services')
