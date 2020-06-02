from django.conf.urls import patterns, url
from cmsplugin_feedback.views import FeedbackView
from django.views.decorators.cache import never_cache

urlpatterns = patterns('',  # NOQA
    url(r'^form/(?P<plugin>\d+)/?$', never_cache(FeedbackView.as_view()), name='feedback-form'),
)
