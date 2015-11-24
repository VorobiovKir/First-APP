from django.conf.urls import url

urlpatterns = [

    url(r'^login/$', 'authorization.views.login', name='login'),
    url(r'^registration/$', 'authorization.views.registration', name='regist'),
    url(r'^logout/$', 'authorization.views.logout', name='logout'),
]