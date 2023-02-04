from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from events.models import Event
from events.forms import EventForm

def get_index(request):
    queryset = Event.objects.all()
    context = {
        'events': queryset
    }
    return render(request, 'index.html', context)

def event_detail_view(request, event_id):
    try:
        queryset = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        queryset = None
    context = {
        'event': queryset
    }
    return render(request, 'event-detail.html', context)


@login_required
@staff_member_required
def event_create_view(request):
    # An alternate way to check
    # if not request.user.is_staff:
    #     return redirect('unauthorized')
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'event-create-form.html', context)

@login_required
@staff_member_required
def event_update_view(request, event_id):
    # An alternate way to check
    # if not request.user.is_staff:
    #     return redirect('unauthorized')
    context = {}
    try:
        event = Event.objects.get(id=event_id)
        context['event'] = event
        context['form'] = EventForm(instance=event)
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES, instance=event)
            if form.is_valid():
                event.save()
                return redirect('event_detail', event_id=event.id)
    except Event.DoesNotExist:
        context['event'] = None
    return render(request, 'event-update-form.html', context)

@login_required
@staff_member_required
def event_delete_view(request, event_id):
    # An alternate way to check
    # if not request.user.is_staff:
    #     return redirect('unauthorized')
    if request.user.is_staff:
        event = get_object_or_404(Event, id=event_id)
        event.delete()
    return redirect('home')
