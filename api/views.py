from datetime import datetime
import json
from django.db import connection
from rest_framework import views
from requests import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Rider, Requester
from .serializers import  RiderSerializer, RequesterSerializer
from rest_framework.filters import OrderingFilter
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
class RiderAPI(generics.ListCreateAPIView):
    model = Rider
    serializer_class = RiderSerializer
    queryset = Rider.objects.all()


class RequesterAPI(generics.ListCreateAPIView):
    model = Requester
    serializer_class = RequesterSerializer
    queryset = Requester.objects.all()

class UserRequestorList(generics.ListAPIView):
    
    serializer_class = RequesterSerializer
    name = 'requester-list'

    
    def get_queryset(self):
        query_params = (dict(self.request.GET.items()))
        if query_params and "status" in query_params:
            print("here")
            if query_params['status'] == "EXPIRED":
                return Requester.objects.filter(user=self.request.user,date_time__lt=timezone.now()).order_by('date_time')
            if query_params['status'] == "PENDING":
                return Requester.objects.filter(user=self.request.user,date_time__gt=timezone.now()).order_by('date_time')
        return Requester.objects.all().filter(user=self.request.user)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['asset_type', ]
    ordering_fields = ['date_time']


class UserRequesterUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = RequesterSerializer
    queryset = Requester.objects.all()

class UserRequestMatchListAPI(APIView):
    def get_queryset(self):
        dataset = []
        columns = []
        cursor = connection.cursor()
        query = f'select * from (select * from api_requester where user_id={self.request.user.id}) as requester, (select c.id as riderid, c.user_id as rider_user_id, first_name as ridername, from_location, to_location, datetime from api_rider as c left join authapp_user on c.user_id = authapp_user.id) as rider where requester.from_location = rider.from_location and requester.to_location = rider.to_location and (select date(date_time)) = (select date(datetime))'
        data=cursor.execute(query)
        for column in data.description:
            columns.append(column[0])
        cursor.execute(query)
        data = cursor.fetchall()

        for row in data:
            
            dataset.append(dict(zip(columns,row)))
        print(dataset)
        
        return dataset
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        
        return Response(self.get_queryset())

    

