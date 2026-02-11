from django import forms
from .models import Battle


class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ["date", "trainer"]
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
        }
