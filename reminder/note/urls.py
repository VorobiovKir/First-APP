from django.conf.urls import url
urlpatterns = [

    # url(r'^$', 'authorization.views.home', name='home'),
    url(r'^$', 'note.views.all', name='all'),
    url(r'^add/$', 'note.views.addNote', name='add'),
    url(r'^addCat/$', 'note.views.addCat', name='addCat'),
    url(r'^addTag/$', 'note.views.addTag', name='addTag'),
    url(r'^delNote/(?P<note_id>[0-9]+)/$', 'note.views.delNote', name='delNote'),
    url(r'^edit/(?P<note_id>[0-9]+)/$', 'note.views.addNote', name='editNote'),
    url(r'^editCat/(?P<cat_id>[0-9]+)/$', 'note.views.addCat', name='editCat'),
    url(r'^delCat/(?P<cat_id>[0-9]+)/$', 'note.views.delCat', name='delCat'),
    url(r'^delTag/(?P<tag_id>[0-9]+)/$', 'note.views.delTag', name='delTag'),
    url(r'^editTag/(?P<tag_id>[0-9]+)/$', 'note.views.addTag', name='editTag'),
    url(r'^cat(?P<cat_id>[0-9]+)/$', 'note.views.all', name='showCat'),
    url(r'^tag(?P<tag_id>[0-9]+)/$', 'note.views.all', name='showTag'),
    # url(r'^all/$', 'note.views.all', name='all'),
]

