from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

@login_required
def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    room.participants.add(request.user)
    messages = room.messages.all().order_by('timestamp')
    return render(request, 'chat/room.html', {
        'room_name': room.name,
        'messages': messages
    })

@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST['name']
        Room.objects.create(name=name)
        return redirect('room', room_name=name)
    return render(request, 'chat/create_room.html')

# Added signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Make sure 'login' is in your urls
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})
