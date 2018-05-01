"""helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include  #  include wasn't part of the generated import statement
from django.contrib import admin


# def search_from_stored_data(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             city_name = str(request.POST['pairs'])
#             return render(request, 'about.html', {'search_terms': message})
#     else:
#         form = InputForm()
#
#     return render(request, 'about.html', {'form': form})

urlpatterns = [
    url(r'^', include('howdy.urls')),
    url(r'^admin/', admin.site.urls),
    # this isn't sent in to the include() function.
]
