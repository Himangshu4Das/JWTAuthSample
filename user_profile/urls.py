from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, ProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]