from django.shortcuts import render

# Create your views here.
from .models import Song, Artist, SongInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_songs = Song.objects.all().count()
    num_instances = SongInstance.objects.all().count()


    # The 'all()' is implied by default.
    num_artists = Artist.objects.count()

    context = {
        'num_songs': num_songs,
        'num_instances': num_instances,
        
        'num_artists': num_artists,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
from django.views import generic

class SongListView(generic.ListView):
    model = Song
    paginate_by = 10
class SongDetailView(generic.DetailView):
    model = Song
from django.contrib.auth.mixins import LoginRequiredMixin

class MySongsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing songs on loan to current user."""
    model = SongInstance
    template_name = 'songcatalog/songinstance_list_mysongs_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            SongInstance.objects.filter(mysongs=self.request.user)
            
        )
