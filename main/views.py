from django.shortcuts import render
from django.http import HttpResponse
from main.forms import UserForm, UserProfileForm

def index(request):
    context_dict = {'message': 'Hello Andrea.'}
    return render(request, 'main/index.html', context=context_dict)

def about(request):
    context_dict = {'message': 'Hello Marc.'}
    return render(request, 'main/index.html', context=context_dict)

def userpage(request):
    context_dict = {'message': 'Hello Inesh.'}
    return render(request, 'main/index.html', context=context_dict)

def userBookmarks(request):
    context_dict = {'message': 'Hello (again) Inesh.'}
    return render(request, 'main/index.html', context=context_dict)

def explore(request):
    context_dict = {'message': 'Hello Toby.'}
    return render(request, 'main/index.html', context=context_dict)

def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'main/signup.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
