from django.urls import path

from .views import SignUpView, DetailUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('detail', DetailUserView.as_view(), name='user_detail'),
]