from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'^api/v1/posts',views.PostViewSet)

urlpatterns = [
	url(r'^$',views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$',views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^',include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'post_table', views.post_table, name='post_table'),
	url(r'secs', views.secs, name='secs'),
]