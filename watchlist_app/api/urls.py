from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api import views
from watchlist_app.api.views import ReviewList, ReviewDetail, ReviewCreate, StreamPlatformViewSet, \
    StreamPlatformModelViewSet, UserReview
from watchlist_app.models import Review, StreamPlatform

router = DefaultRouter()
router.register('stream', StreamPlatformModelViewSet, basename='streamplatform')

urlpatterns = [
    path("list/", views.WatchListAv.as_view(), name='move-list'),
    path("<int:pk>/", views.WatchListDetail.as_view(), name='move-detail'),

    # path("stream/", views.StreamPlatformAV.as_view(), name='streamPlatFromList'),
    # path("stream/<int:pk>/", views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('', include(router.urls)),

    path("<int:pk>/review-create/", ReviewCreate.as_view(), name='review-create'),

    path("<int:pk>/review/", ReviewList.as_view(), name='review-list'),

    path("review/<int:pk>/", ReviewDetail.as_view(), name='review-detail'),

    path("reviews/", UserReview.as_view(), name='user-review-detail'),

]
