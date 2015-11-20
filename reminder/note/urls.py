from django.conf.urls import url
urlpatterns = [

    # url(r'^$', 'authorization.views.home', name='home'),
    url(r'^$', 'note.views.all', name='all'),
    url(r'^add/$', 'note.views.addNote', name='add'),
    url(r'^addCat/$', 'note.views.addCat', name='addCat'),
    url(r'^addTag/$', 'note.views.addTag', name='addTag'),
    # url(r'^all/$', 'note.views.all', name='all'),
]

