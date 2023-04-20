from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import AppointmentSerializer,UserSerializers
from rest_framework.response import Response
from .models import appointments
from rest_framework import status
from django.http import JsonResponse
import jwt,datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import pdb;
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET','POST'])
def signup(request):
    try:
        if request.method == 'POST':
            user = request.data
            serializer = UserSerializers(data=request.data,partial=True)
            print('data',request.data)
            
            if serializer.is_valid() :
                print('errorr',serializer.errors)
                serializer.save()
                print('uyuyu',user['email'],user['username'])
                return Response(serializer.data,200)
            return Response(serializer.errors)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','POST'])       
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]  
    
    return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
       
        token['first_name'] = user.first_name
        
        # ...
    
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
   



@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) 
def add_appointment(request):
    data = request.data
    try:
        if request.method == 'POST':
            serializer = AppointmentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    

@api_view(['GET', 'POST']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) 
def get_appointment(request):
    try:
        if request.method == 'GET':
            appointment = appointments.objects.all()
            serializer = AppointmentSerializer(appointment, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT','GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])  
def update_appoinments(request,id):
    try:
        appointment = appointments.objects.get(id=id)
        print('outiff')
        if request.method == 'PUT':
            print('inputt')
            serializer = AppointmentSerializer(appointment, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            return Response(serializer.errors, status=400)
        elif request.method == 'GET':
            print('ingetttt')
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data)
    except appointments.DoesNotExist:
        return Response({'error': 'Appointment not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
    

@api_view(['DELETE']) 
def delete_appointments(request,id):
    try:
        appointment = appointments.objects.get(id=id)
        appointment.delete()
        return Response({'success': 'Appointment deleted successfully.'}, status=status.HTTP_200_OK)
    except appointments.DoesNotExist:
        return Response({'error': 'Appointment not found.'}, status=status.HTTP_404_NOT_FOUND)
    

# @api_view(['PUT', 'DELETE'])
# def appointment_details(request,id):
#     appointment = appointments.objects.get(id=id)
#     serializer = AppointmentSerializer(appointment, data=request.data)
    
#     if request.method == 'GET':
#         serializer = AppointmentSerializer(appointment, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         appointment.delete()
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
        
    
    


        
    