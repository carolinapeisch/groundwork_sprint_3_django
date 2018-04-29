from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

class HomePageView(View):
    form_class = NameForm
    initial = {'city_input': ''}
    template_name = 'index.html'

    def get(self, request, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['city_input'].lower().title()
            return HttpResponseRedirect('/city_overview/{}'.format(name))
        return render(request, self.template_name, {'form': form})

class AboutPageView(TemplateView):
    template_name = "about.html"


class CityOverview(View):
    template_name = "city_overview.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name, {'message': "OH HEY THERE"})



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
