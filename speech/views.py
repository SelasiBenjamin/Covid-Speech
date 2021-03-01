from django.shortcuts import render,redirect, get_object_or_404
from speech.models import Speeches, Speaker
from django.views import generic



class SpeechesDetailView(generic.DetailView):
    model = Speeches


def index(request):

    return render(request, 'index.html')


class SpeechesListView(generic.ListView):
    model = Speeches
    paginate_by = 5

class SpeechesDetailView(generic.DetailView):
    model = Speeches
    

class SpeakerListView(generic.ListView):
    model = Speaker
    

class SpeakerDetailView(generic.DetailView):
    model = Speaker

