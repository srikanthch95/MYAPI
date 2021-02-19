from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.views import View,APIView

from SrikanthFTL.populate_data import populate

def welcome(request):
    return render(request,'welcome.html')

class UserActivities(APIView):
    def get(self,request):
        all = User.objects.all()
        all_users = UserSerializer(all, many=True)
        return Response(all_users.data)


def data_populate(request):
    print('start')
    populate(1)
    print('end')
    return render(request,'welcome.html',{'populate':'Data populated Successfully'})


