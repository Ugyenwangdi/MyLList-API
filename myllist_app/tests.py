
from asyncio.windows_events import NULL
from django.contrib.auth.models import User 
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from myllist_app.api import serializers
from myllist_app import models 


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.stream = models.StreamingPlatform.objects.create(name="Netflix", about="#1 Platform", link="https://www.netflix.com") # created element manually since a normal user cannt create
    
    
    def test_streamingplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "#1 Streaming platform",
            "link": "http://www.netflix.com"
        }
        
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class ProductionCompanyTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.producer = models.ProductionCompany.objects.create(name="Dorji", about="#1 producer", link="https://www.dorji.com") # created element manually
    
    
    def test_producer_create(self):
        data = {
            "name": "Dorji",
            "about": "#1 producer",
            "link": "http://www.dorji.com"
        }
        
        response = self.client.post(reverse('productioncompany-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_producer_list(self):
        response = self.client.get(reverse('productioncompany-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_producer_ind(self):
        response = self.client.get(reverse('productioncompany-detail', args=(self.producer.id, ))) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class DirectorTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.director = models.Director.objects.create(name="Dechen", about="#1 Director", link="https://www.dechen.com") # created element manually
    
    
    def test_director_create(self):
        data = {
            "name": "Dechen",
            "about": "#1 Director",
            "link": "http://www.dechen.com"
        }
        
        response = self.client.post(reverse('director-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_director_list(self):
        response = self.client.get(reverse('director-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_director_ind(self):
        response = self.client.get(reverse('director-detail', args=(self.director.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WriterTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.writer = models.Writer.objects.create(name="Dechen", about="#1 writer", link="https://www.dechen.com") # created element manually
    
    
    def test_writer_create(self):
        data = {
            "name": "Dechen",
            "about": "#1 writer",
            "link": "http://www.dechen.com"
        }
        
        response = self.client.post(reverse('writer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_writer_list(self):
        response = self.client.get(reverse('writer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_writer_ind(self):
        response = self.client.get(reverse('writer-detail', args=(self.writer.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class ActorTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.actor = models.Actor.objects.create(name="Dechen", about="#1 Actor", link="https://www.dechen.com") # created element manually
    
    
    def test_actor_create(self):
        data = {
            "name": "Dechen",
            "about": "#1 Actor",
            "link": "http://www.dechen.com"
        }
        
        response = self.client.post(reverse('actor-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_actor_list(self):
        response = self.client.get(reverse('actor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actor_ind(self):
        response = self.client.get(reverse('actor-detail', args=(self.actor.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
       
class GenreTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.genre = models.Genre.objects.create(name="Comedy") # created element manually
    
    
    def test_genre_create(self):
        data = {
            "name": "Comedy"
        }
        
        response = self.client.post(reverse('genre-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_genre_list(self):
        response = self.client.get(reverse('genre-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genre_ind(self):
        response = self.client.get(reverse('genre-detail', args=(self.genre.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


       
class TypeTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.type = models.Type.objects.create(name="TV") # created element manually
    
    
    def test_type_create(self):
        data = {
            "name": "TV"
        }
        
        response = self.client.post(reverse('type-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_type_list(self):
        response = self.client.get(reverse('type-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_type_ind(self):
        response = self.client.get(reverse('type-detail', args=(self.type.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                              
        

class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.stream = models.StreamingPlatform.objects.create(name="Netflix", about="#1 Platform", link="https://www.netflix.com") # created element manually
        self.genre = models.Genre.objects.create(name="Horror")
        self.type = models.Type.objects.create(name="Movie")
        self.producer = models.ProductionCompany.objects.create(name="Tashi ProductionCompany", about="#1 Top", link="https://www.tashi.com") # created element manually
        self.director = models.Director.objects.create(name="Lhakpa", about="#Director", link="https://www.lhakpa.com") # created element manually
        self.writer = models.Writer.objects.create(name="Pema", about="writer", link="https://www.pema.com") # created element manually
        
            
        self.show = models.Show.objects.create(title="Example Movie", poster=NULL, video_preview=NULL, synopsis="Example Movie", background="Background", status="airing", countries_origin="Bhutan", languages="Dzongkha") # created
        self.show.platforms.add(self.stream)
        self.show.genres.add(self.genre)
        self.show.types.add(self.type)
        self.show.production_companies.add(self.producer)
        self.show.directors.add(self.director)
        self.show.writers.add(self.writer)
        
    def test_show_create(self):
        
        data = {
            
            "title": "Old man",
            "running_time": "02:00:00",
            "poster": NULL,
            "video_preview": NULL,
            "synopsis": "The story about red film from one piece",
            "background": "Background of movie, just started last month and released this month",
            "status": "airing",
            "countries_origin": "Bhutan",
            "languages": "Dzongkha",
            "released_date": "2022-07-06"
        }
        self.show.platforms.add(self.stream)
        self.show.genres.add(self.genre)
        self.show.types.add(self.type)
        self.show.production_companies.add(self.producer)
        self.show.directors.add(self.director)
        self.show.writers.add(self.writer)
        response = self.client.post(reverse('show-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
    def test_show_list(self):
        response = self.client.get(reverse('show-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # individual show 
    def test_show_ind(self):
        response = self.client.get(reverse('show-detail', args=(self.show.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Show.objects.count(), 1)
        self.assertEqual(models.Show.objects.get().title, 'Example Movie')
    
    
class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # logged in as user
    
        self.stream = models.StreamingPlatform.objects.create(name="Netflix", about="#1 Platform", link="https://www.netflix.com") # created element manually
        self.genre = models.Genre.objects.create(name="Horror")
        self.type = models.Type.objects.create(name="Movie")
        self.producer = models.ProductionCompany.objects.create(name="Tashi ProductionCompany", about="#1 Top", link="https://www.tashi.com") # created element manually
        self.director = models.Director.objects.create(name="Lhakpa", about="#Director", link="https://www.lhakpa.com") # created element manually
        self.writer = models.Writer.objects.create(name="Pema", about="writer", link="https://www.pema.com") # created element manually
        
        # show1    
        self.show = models.Show.objects.create(title="Example Movie", synopsis="Example Movie", status="airing", countries_origin="Bhutan", languages="Dzongkha") # created
        self.show.platforms.add(self.stream)
        self.show.genres.add(self.genre)
        self.show.types.add(self.type)
        self.show.production_companies.add(self.producer)
        self.show.directors.add(self.director)
        self.show.writers.add(self.writer)
        
        # show 2
        self.show2 = models.Show.objects.create(title="Example Movie 2", synopsis="Example Movie2", status="airing", countries_origin="Bhutan", languages="Dzongkha") # created
        self.show2.platforms.add(self.stream)
        self.show2.genres.add(self.genre)
        self.show2.types.add(self.type)
        self.show2.production_companies.add(self.producer)
        self.show2.directors.add(self.director)
        self.show2.writers.add(self.writer)
        
        self.review = models.Review.objects.create(review_user=self.user, rating=5, description="Great Movie", show= self.show2, status='plan')
    
        # add some more items
    
    # test to create a review 
    def test_review_create(self):
        
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great Movie",
            "show": self.show,
            "status": "plan"
        }
        
        response = self.client.post(reverse('review-create', args=(self.show.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)
        # self.assertEqual(models.Review.objects.get().rating, 5)
    
        
        # Two times to check for restrictions
        response = self.client.post(reverse('review-create', args=(self.show.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # unauthenticated user review create test 
    def test_review_create_unauth(self):    
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie",
            "show": self.show,
            "status": "plan"
        }
        
        self.client.force_authenticate(user=None)  # help us to login as any other user or user as none, as not logged in
        response = self.client.post(reverse('review-create', args=(self.show.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def test_review_update(self):    
        
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great Movie - updated",
            "show": self.show,
            "status": "watching"
        }
        
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # get all the reviews    
    def test_review_list(self): 
        response = self.client.get(reverse('review-list', args=(self.show.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # get users' review in particular show
    def test_show_review_list(self): 
        response = self.client.get('/api/show/' + str(self.show.id) + '/reviews/?review_user__username=' +  self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
   # get individual reviews 
    def test_review_ind(self): 
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_review_ind_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    # how to pass url instead of reverse    
    def test_review_user(self):
        response = self.client.get('/api/show/user-reviews/?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)