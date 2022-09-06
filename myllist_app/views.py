from django.shortcuts import render, redirect
import requests
from datetime import datetime
from dateutil import parser

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if username and email and password and password2:
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username taken...')
                    return render(request, 'myllist_app/register.html')

                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email taken...')
                    return render(request, 'myllist_app/register.html')

                else:
                    user = User.objects.create_user(username=username, password=password2, email=email)
                    user.save()
                    messages.info(request, 'User created')
                    return render(request, 'myllist_app/login.html')
            else:
                messages.info(request, 'Password did not match..')
            return render(request, 'myllist_app/register.html')

        else:
            messages.info(request, 'Fill all the fields')
            return render(request, 'myllist_app/register.html')
    else:
        return render(request, 'myllist_app/register.html')


def login(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'myllist_app/login.html')

    else:
        return render(request, 'myllist_app/login.html')


def changePW(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        try:
            user = User.objects.get(username=username)
            
            if username and password1 and password2:
                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    messages.info(request, 'Password changed...')
                    return redirect('myllist:changepw')
                messages.info(request, 'Something went wrong...')
                return render(request, 'myllist_app/change_password.html', {'error': 'Passwords not same'})
        except:
            
            return render(request, 'myllist_app/change_password.html', {'error': 'No matching details'})
    return render(request, 'myllist_app/change_password.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def Home(request):
        
    # token = "1845fad2d876e5658bc917897a70e05d9c8964ef"
    url = "https://myllist.herokuapp.com/api/show/"
    # url = 'http://127.0.0.1:8000/api/show/'
    response = requests.get(url)   
    
    ls = response.json()
    
    top_shows = sorted(ls, key=lambda item: item.get("avg_rating"), reverse=True)
    # print(len(show_sorted[0:3]))

    # # A get request (json example):
    # response = requests.get(url, headers={'Authorization': 'Token {}'.format(token)})

    # print(response.status_code)
    # print(response.json())
    
    
    featured = []
    latest_movies = []
    latest_tvs = []
    top_movies = []
    top_tvs = []
    
    for show in ls:
        if show['featured'] == True:
            featured.append(show)
    
    for show in ls:   
        # print(show['types'][0])     
        if show['types'][0]['name'] == 'Movie':
            latest_movies.append(show)
    
    for show in ls:        
        if show['types'][0]['name'] == 'TV':
            latest_tvs.append(show)
            
    top_movies = sorted(latest_movies, key=lambda item: item.get("avg_rating"), reverse=True)
    top_tvs = sorted(latest_tvs, key=lambda item: item.get("avg_rating"), reverse=True)
    
    featured = featured[0:3]
    top_shows = top_shows[0:6]
    latest_movies = latest_movies[0:8]
    latest_tvs = latest_tvs[0:8]
    top_movies = top_movies[0:3]
    top_tvs = top_tvs[0:3]
    # top = ''
    # latest = ''
    
    # try:
    #     top = request.GET.get('top')
    #     latest = request.GET.get('latest')
    # except:
    #     pass
    
    # url = "http://127.0.0.1:8000/api/show/list2/"
    
    # results = '' 
    # responses = ''

    # if request.method == 'POST':
    #     title = request.POST['movie-input']

    #     querystring = {"title": title}
    #     print(querystring)

    #     response = requests.request("GET", url, params=querystring)
    #     # responses = sorted(response, key=lambda item: item.get("avg_rating"), reverse=True)
        

    #     print(response)
    
    context = {
        'featured': featured, 
        'top_shows': top_shows, 
        'latest_movies': latest_movies, 
        'latest_tvs': latest_tvs, 
        'special_movie': ls[0], 
        'top_movies': top_movies,
        'top_tvs': top_tvs
        # 'top': top,
        # 'latest': latest
    }
    return render(request, 'myllist_app/index.html', context)


def MovieDetail(request, pk):        

    url = "https://myllist.herokuapp.com/api/show/"
    # url = 'http://127.0.0.1:8000/api/show/'
    response = requests.get(url)   
    
    ls = response.json()
    
    top_shows = sorted(ls, key=lambda item: item.get("avg_rating"), reverse=True)
    
    featured = []
    latest_movies = []
    latest_tvs = []
    top_movies = []
    top_tvs = []
    
    for show in ls:
        if show['featured'] == True:
            featured.append(show)
    
    for show in ls:   
        # print(show['types'][0])     
        if show['types'][0]['name'] == 'Movie':
            latest_movies.append(show)
    
    for show in ls:        
        if show['types'][0]['name'] == 'TV':
            latest_tvs.append(show)
            
    top_movies = sorted(latest_movies, key=lambda item: item.get("avg_rating"), reverse=True)
    top_tvs = sorted(latest_tvs, key=lambda item: item.get("avg_rating"), reverse=True)
    

    top_movies = top_movies[0:3]
    top_tvs = top_tvs[0:3]
    
    
    url = 'https://myllist.herokuapp.com/api/show/{}/'.format(pk)
    # url = 'http://127.0.0.1:8000/api/show/{}/'.format(pk)
    response = requests.get(url)  
    
    show = response.json()   
    
    # print(show)
    
    date_string = show['released_date']
    parsed_date = parser.parse(date_string)
    released_date = parsed_date.strftime('%Y-%m-%d')
    
    type = ''
    genre = ''
    producers = ''
    director = ''
    writer = ''
    
    types = show['types']
    genres = show['genres']
    production_companies = show['production_companies']
    directors = show['directors']
    writers = show['writers']
    
    
    
    for i in types:
        if type == '':
            type = type + ' ' + i['name'] 
        else:
            type = type + ', ' + i['name'] 
        
    for i in genres:
        if genre == '':
            genre = genre + ' ' + i['name']
        else:
            genre = genre + ', ' + i['name']
    
    for i in production_companies:
        if producers == '':
            producers = producers + ' ' + i['name']
        else:
            producers = producers + ', ' + i['name']
            
    for i in directors:
        if director == '':
            director = director + ' ' + i['name']
        else:
            director = director + ', ' + i['name']
            
    for i in writers:
        if writer == '':
            writer = writer + ' ' + i['name']
        else:
            writer = writer + ', ' + i['name']
    
    rating = ''
    review = ''
    status = ''
    
    create_review_url = "https://myllist.herokuapp.com/api/show/{}/reviews/create/".format(pk)
    # create_review_url = "http://127.0.0.1:8000/api/show/{}/reviews/create/".format(pk)
    

    
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            
            rating = request.POST['rating']
            review = request.POST['review']
            status = request.POST['status']
            
            
            # print(rating, review, status)

            
            try:
                current_user = request.user
                # print(current_user)
                token = Token.objects.get(user__username=current_user)
                # print(token)
                
                payload = {
                    "rating": rating,
                    "description": review,
                    "status": status
                }
                headers = {"Authorization": "Token {}".format(token)}

                response = requests.request("POST", create_review_url, json=payload, headers=headers)
                # mes = messages.info(request, response.text)
                
                if 'already reviewed' in response.text:
                    messages.info(request, response.text)
                else:
                    messages.info(request, 'Review submitted...')

                # print(response.text)
                
            except:
                pass   
    else:
        messages.info(request, 'You need to login in order to create your own reviews...')
                    
        
    context = {
 
        'top_movies': top_movies,
        'top_tvs': top_tvs,
        
        'show': show,
        'released_date': released_date,
        'types': type,
        'genres': genre,
        'producers': producers,
        'directors': director,
        
        'writers': writer
        
        
    }
    return render(request, 'myllist_app/moviedetail.html', context)


def Movies(request):        
    url = "https://myllist.herokuapp.com/api/show/"
    # url = 'http://127.0.0.1:8000/api/show/'
    response = requests.get(url)   
    
    ls = response.json()


    latest_movies = []
    latest_tvs = []
    top_movies = []
    top_tvs = []
    

    
    for show in ls:   
        # print(show['types'][0])     
        if show['types'][0]['name'] == 'Movie':
            latest_movies.append(show)
    
    for show in ls:        
        if show['types'][0]['name'] == 'TV':
            latest_tvs.append(show)
            
    top_movies = sorted(latest_movies, key=lambda item: item.get("avg_rating"), reverse=True)
    top_tvs = sorted(latest_tvs, key=lambda item: item.get("avg_rating"), reverse=True)
  
    top_three_movie = top_movies[0:3]
    top_three_tv = top_tvs[0:3]


    
    context = {

        'all_movies': top_movies, 
        'latest_movies': latest_movies,
        'top_movies': top_three_movie,
        'top_tvs': top_three_tv
    }
    
    return render(request, 'myllist_app/movies.html', context)


def TV(request):        
    url = "https://myllist.herokuapp.com/api/show/"
    # url = 'http://127.0.0.1:8000/api/show/'
    response = requests.get(url)   
    
    ls = response.json()
    

    latest_movies = []
    latest_tvs = []
    top_movies = []
    top_tvs = []
    

    
    for show in ls:   
        # print(show['types'][0])     
        if show['types'][0]['name'] == 'Movie':
            latest_movies.append(show)
    
    for show in ls:        
        if show['types'][0]['name'] == 'TV':
            latest_tvs.append(show)
            # print(latest_tvs)
            
            
    top_movies = sorted(latest_movies, key=lambda item: item.get("avg_rating"), reverse=True)
    top_tvs = sorted(latest_tvs, key=lambda item: item.get("avg_rating"), reverse=True)
  

    top_three_movie = top_movies[0:3]
    top_three_tv = top_tvs[0:3]

    
    context = {

        'all_tvs': top_tvs, 

        'top_movies': top_three_movie,
        'top_tvs': top_three_tv
    }
    return render(request, 'myllist_app/tvs.html', context)


def About(request):     
    url = "https://myllist.herokuapp.com/api/show/"
    # url = 'http://127.0.0.1:8000/api/show/'
    response = requests.get(url)   
    
    ls = response.json()
    

    latest_movies = []
    latest_tvs = []
    top_movies = []
    top_tvs = []
    

    
    for show in ls:   
        # print(show['types'][0])     
        if show['types'][0]['name'] == 'Movie':
            latest_movies.append(show)
    
    for show in ls:        
        if show['types'][0]['name'] == 'TV':
            latest_tvs.append(show)
            
    top_movies = sorted(latest_movies, key=lambda item: item.get("avg_rating"), reverse=True)
    top_tvs = sorted(latest_tvs, key=lambda item: item.get("avg_rating"), reverse=True)
  

    top_three_movie = top_movies[0:3]
    top_three_tv = top_tvs[0:3]

    
    context = {
        'top_movies': top_three_movie,
        'top_tvs': top_three_tv
    }   
    return render(request, 'myllist_app/about.html', context)
