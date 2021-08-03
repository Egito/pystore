from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Parcel

class ParcelsDetailView(DetailView):
    queryset = Parcel.available.all()

class ParcelsListView(ListView):
    paginate_by = 6

    def get_queryset(self):
        queryset = Parcel.available.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context["category"] = self.category
#        context["categories"] = Category.objects.all()
        
        return context
