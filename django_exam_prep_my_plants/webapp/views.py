from django.shortcuts import render, redirect
from . import forms

# Create your views here.
from django_exam_prep_my_plants.webapp.models import Plant, UserProfile


def index(request):
    return render(request, 'webapp/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }
    return render(request, 'webapp/catalogue.html', context)


def profile_create(request):
    form = forms.ProfileCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'webapp/create-profile.html', context)


def profile_details(request):
    user = UserProfile.objects.first()
    plants = Plant.objects.all()
    context = {
        'user': user,
        'plants': plants,
    }
    return render(request, 'webapp/profile-details.html', context)


def profile_edit(request):
    profile = UserProfile.objects.first()
    form = forms.ProfileEdit(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'webapp/edit-profile.html', context)


def profile_delete(request):
    user = UserProfile.objects.first()
    plants = Plant.objects.all()
    if request.method == 'POST':
        user.delete()
        plants.delete()
        return redirect('index')

    return render(request, 'webapp/delete-profile.html')


def plant_create(request):
    pass


def plant_details(request, pk):
    pass


def plant_edit(request, pk):
    pass


def plant_delete(request, pk):
    pass
