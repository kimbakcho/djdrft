from django.urls import path

from watchlist_app.api import views
from watchlist_app.api.views import ReviewList, ReviewDetail
from watchlist_app.models import Review

urlpatterns = [
    path("list/", views.WatchListAv.as_view(), name='move-list'),
    path("<int:pk>/", views.WatchListDetail.as_view(), name='move-detail'),
    path("stream/", views.StreamPlatformAV.as_view(), name='streamPlatFromList'),
    path("stream/<int:pk>/", views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path("review/", ReviewList.as_view(), name='review-list'),
    path("review/<int:pk>", ReviewDetail.as_view(), name='review-detail')
]
