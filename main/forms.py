from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "base_atk", "substat",
                  "weapon_passive", "weapon_type", "rarity"]