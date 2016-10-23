from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'catalog', views.BookViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^api/', include(router.urls)),
]
