from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('speeches/', views.SpeechesListView.as_view(), name='speeches'),
    path('speeches/<int:pk>', views.SpeechesDetailView.as_view(), name='speech-detail'),

    path('speakers/', views.SpeakerListView.as_view(), name='speakers'),
    path('speaker/<int:pk>', views.SpeakerDetailView.as_view(), name='speaker-detail'),




]