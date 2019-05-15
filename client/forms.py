from django import forms

from client.models import Ticket
from consultant.models import Category


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'thread', 'description']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    thread = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
    )
