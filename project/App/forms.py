from django import forms
from App.models import table_p,table_l,table_t

class p_form(forms.ModelForm):
    class Meta :
        model = table_p
        fields = "__all__"

class l_form(forms.ModelForm):
    class Meta :
        model = table_l
        fields = "__all__"
