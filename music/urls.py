from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from music import views

urlpatterns = [
    path('songs/', views.ListCreateSongsView.as_view(), name="songs-list-create"),
    path('songs/<int:pk>', views.SongDetail.as_view()),
]
