from rest_framework import serializers
from myllist_app import models 


class ReviewSerializer(serializers.ModelSerializer):
    
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = models.Review
        # fields = "__all__"
        exclude = ('show',)

class ProductionCompanySerializer(serializers.ModelSerializer):   
     
    class Meta:
       model = models.ProductionCompany
       fields = "__all__" 
    
class DirectorSerializer(serializers.ModelSerializer): 
    
    class Meta:
       model = models.Director
       fields = "__all__" 
       
class WriterSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = models.Writer
       fields = "__all__" 
       
class ActorSerializer(serializers.ModelSerializer): 
    
    class Meta:
       model = models.Actor
       fields = "__all__" 
       
class GenreSerializer(serializers.ModelSerializer):  
    
    class Meta:
       model = models.Genre 
       fields = "__all__" 

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
       model = models.Type 
       fields = "__all__" 

    
class AlternativeTitleSerializer(serializers.ModelSerializer):  
    
    class Meta:
       model = models.AlternativeTitle 
       fields = "__all__" 
       
class ShowCharacterSerializer(serializers.ModelSerializer):  
    
    class Meta:
       model = models.ShowCharacter 
       fields = "__all__" 
       
       
class StreamingPlatformSerializer(serializers.ModelSerializer):
    
    # show = ShowSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.StreamingPlatform
        fields = "__all__"

       
       
class ShowSerializer(serializers.ModelSerializer):
        
    reviews = ReviewSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    types = TypeSerializer(many=True, read_only=True)
    production_companies = ProductionCompanySerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    writers = WriterSerializer(many=True, read_only=True)
    alternative_titles = AlternativeTitleSerializer(many=True, read_only=True)
    actors = ShowCharacterSerializer(many=True, read_only=True)
    platforms = StreamingPlatformSerializer(many=True, read_only=True)
    
    
    # platforms = serializers.CharField(source='platforms.name')
    
    class Meta:
       model = models.Show 
       fields = "__all__" 


       
