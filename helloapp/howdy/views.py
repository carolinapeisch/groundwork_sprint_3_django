from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"


class CityOverview(TemplateView):
    template_name = "city_overview.html"


class CityRoads(TemplateView):
    template_name = "city_roads_drilldown.html"


# def search_from_stored_data(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             city_name = str(request.POST['city_name'])
#             return render(request, 'search.html', {'search_terms': message})
#     else:
#         form = InputForm()
#
#     return render(request, 'search_form.html', {'form': form})
