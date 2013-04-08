from django.conf.urls import patterns, include, url

urlpatterns = patterns('google_calendar.views',
    url("connect", "connect", name="connect"),
    url("oauth2callback", "callback"),
)