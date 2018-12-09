# coding=utf-8
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

TYPE_CHOICE = (
    ('E', _(u'Email')),
    ('P', _(u'Phone')),
)


class Message(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=20, null=True)
    text = models.TextField(_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)


class FeedbackPlugin(CMSPlugin):
    form_type = models.CharField(_("Type"), max_length=1, choices=TYPE_CHOICE, default='E')
    email = models.EmailField(_('Email'), blank=True, null=True)
