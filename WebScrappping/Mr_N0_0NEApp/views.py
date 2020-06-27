from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAISSLIST_URL = 'https://bangalore.craigslist.org/search/?query={}'
BASE_IMAGE_URL ='https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAISSLIST_URL.format(quote_plus(search))
    # print(final_url)
    response = requests.get(final_url)
    data=response.text
    soup = BeautifulSoup(data,features='html.parser')
    post_listings=soup.find_all('li',{'class':'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_ ='result-title').text
        post_url = post.find('a').get('href')
        if(post.find(class_='result-price')):
            post_price = post.find(class_ ='result-price').text
        else:
            post_price = 'N/A' 
        
        if(post.find(class_='result-image').get('data-ids')):
            post_image = post.find(class_ ='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image = BASE_IMAGE_URL.format(post_image)

        else:
            post_image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.autoinfluence.com%2Fwp-content%2Fuploads%2F2015%2F11%2FCraigslist-Page.jpg&f=1&nofb=1'
    
        final_postings.append((post_title, post_url, post_price,post_image))
        
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request,'Mr_NO_ONEApp/new_search.html', stuff_for_frontend)