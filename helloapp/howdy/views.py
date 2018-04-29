from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def getCityName(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['city_name']
            return HttpResponseRedirect('/city_overview/{}'.format(name))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def lookup_city(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = NameForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('city-overview/{}'.format(form.cleaned_data['city_input'])) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = NameForm(initial={'city_input': 'Enter a city name.',})

    return render(request, 'index.html', {'form': form})










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
