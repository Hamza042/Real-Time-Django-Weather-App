from django.shortcuts import render 
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Islamabad'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=43604a9073ba78d6d4d5b72eafed60f1'
    
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyAJ_JQT4c4yxdzooP1tD8A6RiWsDAqTGYM'
    SEARCH_ENGINE_ID = '92dc4e33cb4634efe'
    
    query = city + "1920x1080"
    page = 1
    start = (page-1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
    
    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    
    
    try:
        
       data = requests.get(url,params=PARAMS).json()
    
       description = data['weather'][0]['description']
       icon = data['weather'][0]['icon']
       temp = data['main']['temp']
    
       day = datetime.date.today()
    
       return render(request,'wavpro/App_Home.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred':False,'image_url':image_url})
    
    except KeyError:
       
       exception_occurred=True
       messages.error(request,'Entered Data Not Available To API')
       day=datetime.date.today()
       
       return render(request,'wavpro/App_Home.html',{'description':'sunny','icon':'01d','temp':20,'day':day, 'city':'islamabad', 'exception_occurred': exception_occurred})
    