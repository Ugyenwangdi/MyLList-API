from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import datetime

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name  
    
class ProductionCompany(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    # profile_image = models.ImageField(null=True, blank=True, upload_to="producers")
    profile_image = models.URLField(max_length=500, null=True, blank=True)  
    country = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'ProductionCompanies'
    
    def __str__(self):
        return self.name  
    
    
class Director(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    # profile_image = models.ImageField(null=True, blank=True, upload_to="directors")
    profile_image = models.URLField(max_length=500, null=True, blank=True) 
    nationality = models.CharField(max_length = 50, null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
class Writer(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)
    # profile_image = models.ImageField(null=True, blank=True, upload_to="writers")
    profile_image = models.URLField(max_length=500, null=True, blank=True) 
    nationality = models.CharField(max_length = 50, null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
class Actor(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(null=True, blank=True, max_length=200)
    link = models.URLField(max_length=100, null=True, blank=True)
    # profile_image = models.ImageField(null=True, blank=True, upload_to="actors")
    profile_image = models.URLField(max_length=500, null=True, blank=True) 
    nationality = models.CharField(max_length = 50, null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Show(models.Model):
    options = (
        ('None', 'None'),
        ('Upcoming', 'Upcoming'),
        ('Airing', 'Airing'),
        ('Finished Airing', 'Finished Airing')
    )

    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='genres')
    types = models.ManyToManyField(Type)
    running_time = models.DurationField(default=datetime.timedelta(0))
    # poster = models.ImageField(null=True, blank=True, upload_to="posters")
    poster = models.URLField(max_length=500, null=True, blank=True)   
    show_backdrop = models.URLField(max_length=500, null=True, blank=True)     
    # video_preview = models.FileField(null=True, blank=True, upload_to='videos')
    video_preview = models.URLField(max_length=500, null=True, blank=True)   
    synopsis = models.TextField()
    background = models.TextField(null=True, blank=True, max_length=500)
    status = models.CharField(max_length=50, choices=options, default='none') 
    countries_origin = models.CharField(max_length=50, null=True, blank=True)
    languages = models.CharField(max_length=60)
    platforms = models.ManyToManyField(StreamingPlatform)
    production_companies = models.ManyToManyField(ProductionCompany)
    directors = models.ManyToManyField(Director)
    writers = models.ManyToManyField(Writer)
    featured = models.BooleanField(default=False)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    link = models.URLField(max_length=100, null=True, blank=True)
    released_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-released_date',)
    
    def __str__(self):
        return self.title
    
class AlternativeTitle(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='alternative_titles')
    language = models.CharField(max_length=50)
    alternative_title = models.CharField(max_length=100)

    def __str__(self):
        return self.alternative_title  
    
class ShowCharacter(models.Model):
    options = (
        ('None', 'None'),
        ('Supporting', 'Supporting'),
        ('Main', 'Main')
    )
    
    character_name = models.CharField(max_length=50)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='actors')
    cast = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='casts', null=True, blank=True)
    character_role = models.CharField(max_length=50, choices=options, default='none')
    credit_value = models.PositiveIntegerField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True, upload_to="characters")
    image = models.URLField(max_length=500, null=True, blank=True) 
    description = models.TextField(null=True, blank=True, max_length=200)
    
    def __str__(self):
        return self.character_name  

class Review(models.Model):
    options = (
        ('none', 'None'),
        ('plan', 'Plan'),
        ('watching', 'Watching'),
        ('completed', 'Completed')
    )
    
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.CharField(max_length=200, null=True, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='reviews')
    status = models.CharField(max_length=50, choices=options, default='none', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.rating) + " | " + self.show.title + " | " + str(self.review_user)
    
    

