from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from myllist_app import models 
from myllist_app.api import permissions, serializers, pagination  # , throttling

class UserReview(generics.ListAPIView):
    
    serializer_class = serializers.ReviewSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return models.Review.objects.filter(review_user__username=username)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    # throttle_classes = [throttling.ReviewCreateThrottle]
    
    
    def get_queryset(self):
        return models.Review.objects.all()
    
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        showlist = models.Show.objects.get(pk=pk)
        
        review_user = self.request.user 
        review_queryset = models.Review.objects.filter(show=showlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
        
        if showlist.number_rating == 0:
            showlist.avg_rating  = serializer.validated_data['rating']
            
        else:
            showlist.avg_rating = (showlist.avg_rating + serializer.validated_data['rating']) / 2

        showlist.number_rating = showlist.number_rating + 1
        showlist.save()
        
        serializer.save(show=showlist, review_user=review_user)


class ReviewList(generics.ListAPIView):
        
    serializer_class = serializers.ReviewSerializer

    # throttle_classes = [throttling.ReviewListThrottle, AnonRateThrottle]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'rating', 'status']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.Review.objects.filter(show=pk)
    
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsReviewUserOrReadOnly]
    # throttle_classes = [ScopedRateThrottle, AnonRateThrottle]
    # throttle_scope = 'review-detail'
    

class StreamingPlatformVS(viewsets.ModelViewSet):

    queryset = models.StreamingPlatform.objects.all()
    serializer_class = serializers.StreamingPlatformSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]


class ProductionCompanyVS(viewsets.ModelViewSet):
    queryset = models.ProductionCompany.objects.all()
    serializer_class = serializers.ProductionCompanySerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    

class DirectorVS(viewsets.ModelViewSet):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
    
class WriterVS(viewsets.ModelViewSet):
    queryset = models.Writer.objects.all()
    serializer_class = serializers.WriterSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
class ActorVS(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
class GenreVS(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

class TypeVS(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]


class ShowGV(generics.ListAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializer
    pagination_class = pagination.ShowCPagination       
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'platforms__name']
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'platforms__name']

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields  = ['avg_rating']


class ShowAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
    def get(self, request):
        shows = models.Show.objects.all()
        serializer = serializers.ShowSerializer(shows, many=True) # to access multiple objects, many=True
        
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = serializers.ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
        
class ShowDetailAV(APIView):
    
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
    def get(self, request, pk):
        try:
            show = models.Show.objects.get(pk=pk)
        
        except models.Show.DoesNotExist:
            return Response({'Error: not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ShowSerializer(show)
            
        return Response(serializer.data)
    
    def put(self, request, pk):
        show = models.Show.objects.get(pk=pk)
        serializer = serializers.ShowSerializer(show, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show = models.Show.objects.get(pk=pk)
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlternativeTitleVS(viewsets.ModelViewSet):
    queryset = models.AlternativeTitle.objects.all()
    serializer_class = serializers.AlternativeTitleSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
class ShowCharacterVS(viewsets.ModelViewSet):
    queryset = models.ShowCharacter.objects.all()
    serializer_class = serializers.ShowCharacterSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

##### Using with frontend ##########

# import requests
# def Home(request):
        
#     mytoken = "1845fad2d876e5658bc917897a70e05d9c8964ef"
#     myurl = "http://127.0.0.1:8000/api/show/streams/"

#     # A get request (json example):
#     response = requests.get(myurl, headers={'Authorization': 'Token {}'.format(mytoken)})

#     # print(response.status_code)
#     # print(response.json())
    
#     data = response.json()
#     context = {'data': data}
#     return render(request, 'myllist_app/index.html', context)

# import requests
# mytoken = "1845fad2d876e5658bc917897a70e05d9c8964ef"
# myurl = "http://127.0.0.1:8000/api/show/streams/"

# # A get request (json example):
# response = requests.get(myurl, headers={'Authorization': 'Token {}'.format(mytoken)})
# data = response.json()
# print(data)
# A post request:
# data = { < your post data >}
# requests.post(myurl, data=data, headers={'Authorization': 'Token {}'.format(mytoken)})