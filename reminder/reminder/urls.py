from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'reminder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', 'reminder.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authorization.urls', namespace='author')),
    url(r'^note/', include('note.urls', namespace='note')),
    url(r'^$', 'note.views.all', name='home'),
]
