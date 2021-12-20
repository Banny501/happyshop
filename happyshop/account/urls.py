from django.urls import path, include

from .views import RegisterUser

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', RegisterUser.as_view(), name='register')
]
