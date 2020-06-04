from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('user', views.UserView)
router.register('post', views.PostView)
router.register('clap', views.ClapView)
router.register('comment', views.CommentView)
router.register('feed', views.FeedView)

urlpatterns = [
    path('', include(router.urls))
]
