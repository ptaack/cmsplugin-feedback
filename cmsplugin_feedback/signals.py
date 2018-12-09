import django.dispatch
from django.contrib.sites.models import get_current_site
from django.core.mail import mail_managers, send_mail
from django.core.urlresolvers import reverse
from django.template import loader, Context
from django.conf import settings as global_settings
from . import settings


form_submited = django.dispatch.Signal()


def notify_managers(sender, message, request, *args, **kwargs):
    plugin_model = kwargs.get('plugin_model')
    if plugin_model and plugin_model.email:
        send_mail(
            settings.NOTIFY_SUBJECT,
            render_email(message, request),
            getattr(global_settings, 'DEFAULT_FROM_EMAIL', ''),
            [plugin_model.email],
            fail_silently=True)
    if settings.NOTIFY_MANAGERS:
        mail_managers(
            subject=settings.NOTIFY_SUBJECT,
            message=render_email(message, request),
            fail_silently=True)


form_submited.connect(notify_managers)


def get_admin_url(instance, request):
    meta = instance._meta
    model = hasattr('meta', 'model_name') and \
        meta.model_name or meta.module_name
    url_pattern = 'admin:{app}_{model}_change'.format(
        app=meta.app_label, model=model)
    s = get_current_site(request)
    return 'http://' + s.domain + reverse(url_pattern, args=[instance.pk])


def render_email(message, request):
    t = loader.get_template('cms/plugins/feedback-email.html')
    c = Context({
        'message': message,
        'url': get_admin_url(message, request),
    })
    return t.render(c)
