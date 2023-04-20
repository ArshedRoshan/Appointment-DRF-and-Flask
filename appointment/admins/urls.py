from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
   path('signup',signup,name='signup'),
   path('add',add_appointment,name='add'),
   path('get_appointment',get_appointment,name='get_appointment'),
   path('update_appoinment/<int:id>',update_appoinments,name='update_appoinment'),
   path('delete_appointments/<int:id>',delete_appointments,name='delete_appointments'),
   path('',getRoutes,name='routes'),
   path('token',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh',TokenRefreshView.as_view(), name='token_refresh'),
]