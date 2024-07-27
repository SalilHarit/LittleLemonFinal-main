from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
    path('api-token-auth/', obtain_auth_token),
    # Add the remaining URL path configurations here
]
