from django.views.generic import ListView, DetailView
from . import models

class HomeView(ListView):

    ''' HomeView Definition ''' 

    model = models.Room 
    paginate_by = 10
    ordering = 'created'
    paginate_orphans = 5
    page_kwarg = 'page' 
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    ''' 
    #11.4 paginator: https://docs.djangoproject.com/en/3.1/ref/paginator/#django.core.paginator.Paginator 
    #11.5 orphan: https://docs.djangoproject.com/en/3.1/ref/paginator/#django.core.paginator.Paginator.orphans 
    #11.6 Handling exception: 
    #11.7 Class Based View - ListView: https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview 
          CCBV - ListView: http://ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/ 
    '''

class RoomDetail(DetailView):
    
    ''' RoomDetail Definition '''

    model = models.Room
    