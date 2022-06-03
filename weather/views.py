import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    key = 'bb7467c6cbda42b7861153402220306'
    url = 'http://api.weatherapi.com/v1/current.json?key=bb7467c6cbda42b7861153402220306&q={}&aqi=no'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()    
            
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["current"]["temp_c"],
            'icon': res["current"]["condition"]["icon"]
        }    
        all_cities.append(city_info)
    
    context = {'all_info': all_cities, 'form': form}
    
    return render(request, 'weather/index.html', context)