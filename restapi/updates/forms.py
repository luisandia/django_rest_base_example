from django import forms

from .models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            raise forms.ValidationError('Content is required')
        image = data.get("image", None)
        # if content is None or image is None:
        #     raise forms.ValidationError('Content or image is required')
        return super().clean(*args, **kwargs)
