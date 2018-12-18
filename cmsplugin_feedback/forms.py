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
        form_type = None
        try:
            form_type = kwargs.pop('form_type')
        except KeyError:
            if 'phone' in args[0]:
                form_type = 'P'
        super(FeedbackMessageForm, self).__init__(*args, **kwargs)
        if form_type:
            field = 'email' if form_type == 'P' else 'phone'
            self.fields.pop(field)
