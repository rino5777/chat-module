from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat_room.html', {'room': room, 'messages': messages})


@login_required
def test_chat(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        rooms = Room(name = len(rooms)+1, slug = len(rooms)+1)
        rooms.save()
        
        return redirect('rooms')


    return render(request, 'index.html', {'rooms': rooms})


def delete_room(request, id):
    del_room = Room.objects.get(id=id)
    del_room.delete()

    return redirect('rooms')