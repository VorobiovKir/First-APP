from django.conf.urls import url
urlpatterns = [

    # url(r'^$', 'authorization.views.home', name='home'),
    url(r'^$', 'note.views.all', name='all'),
    url(r'^add/$', 'note.views.addNote', name='add'),
    url(r'^addCat/$', 'note.views.addCat', name='addCat'),
    url(r'^addTag/$', 'note.views.addTag', name='addTag'),
    url(r'^delNote/(?P<note_id>[0-9]+)/$', 'note.views.delNote', name='delNote'),
    url(r'^add/(?P<note_id>[0-9]+)/$', 'note.views.addNote', name='editNote'),
    url(r'^delCat/(?P<cat_id>[0-9]+)/$', 'note.views.delCat', name='delCat'),
    # url(r'^all/$', 'note.views.all', name='all'),
]

