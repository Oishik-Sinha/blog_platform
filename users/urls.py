from django.urls import path
from users.views import SignupView, LoginView, LogoutView, LandingPage

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LandingPage, name='landing'),
]