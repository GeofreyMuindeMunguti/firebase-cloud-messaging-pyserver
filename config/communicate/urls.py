# your_app/urls.py
from django.conf.urls import url, include
from rest_framework import routers
from communicate.views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    url(r'^v2/', include(router.urls))

]