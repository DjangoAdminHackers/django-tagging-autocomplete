try:
    from django.conf.urls.defaults import *
except:
    from django.conf.urls import *

urlpatterns = patterns('tagging_autocomplete.views',
    url(r'^list$', 'list_tags', name='tagging_autocomplete-list'),
)
