# coding=utf-8
from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Message


class FeedbackMessageForm(forms.ModelForm):
    captcha = CaptchaField(
        label=_('Type the code shown'),
        widget=CaptchaTextInput(attrs={'class': 'captcha-input'}))

    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'text', 'captcha',)

    def __init__(self, *args, **kwargs):
        form_type = kwargs.pop('form_type')
        super(FeedbackMessageForm, self).__init__(*args, **kwargs)
        field = 'email' if form_type == 'P' else 'phone'
        self.fields.pop(field)
