from django.forms import ModelForm

from myapp.models import todo


class formtodo(ModelForm):
    class Meta:
        model = todo
        fields=['title','status','priority']
