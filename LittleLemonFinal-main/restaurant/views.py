from django.shortcuts import render
from .forms import BookingForm
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# View function for the home page
def home(request):
    return render(request, 'index.html')



# View function for the booking page
def booking(request):
    return render(request, 'book.html')

# View function for the menu page
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu": menu_data
    }
    return render(request, 'menu.html', main_data)
# Add your code here to create new views
def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    return render(request, 'menu_item.html', {'menu_item': menu_item})


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
