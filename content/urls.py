from django.urls import path
from .views import UploadFeed, Profile, Main, UploadReply, ToggleLike, ToggleBookmark, delete_feed, update_feed

urlpatterns = [
    path('upload/', UploadFeed.as_view()),
    path('reply/', UploadReply.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
    path('profile/', Profile.as_view()),
    path('main/', Main.as_view()),
    path('<int:id>/delete/', delete_feed),
    path('<int:id>/update/', update_feed),
]

