from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, UpdateProfileForm, UpdateUserForm, NeighbourHoodForm, BusinessForm, PostForm
from .models import Profile, User, Neighbourhood, Business, Post
from .email import send_welcome_email

# Create your views here.


@login_required(login_url='login')
def index(request):
  return render(request, 'index.html')


def register(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      email = form.cleaned_data['email']
      send_welcome_email(username=username,email=email)
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('index')
  else:
    form = SignupForm()
  return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'editprofile.html', {'user_form': user_form, 'prof_form': prof_form})


def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()

            return redirect('hoods')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})


def hoods(request):
    hoods = Neighbourhood.objects.all()
    hoods = hoods[::-1]

    return render(request, 'hoods.html', {"hoods": hoods})


def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hoods')


def leave_hood(request, id):
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hoods')


def hood(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    return render(request, 'hood.html', {'hood': hood})


def hood_occupants(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    occupants = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'occupants.html', {'occupants': occupants})


def business(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.neighbourhood = hood
            form.user = request.user.profile
            form.save()
            return redirect('business', hood.id)
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'business': business, 'form': form})

def post(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    post = Post.objects.filter(neighbourhood=hood)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.neighbourhood = hood
            form.user = request.user.profile
            form.save()
            return redirect('post', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'post': post,'form':form})

def search(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        searchresults = Business.objects.filter(name__icontains=name).all()
        message = f'name'
        return render(request, 'searchresults.html', {'searchresults': searchresults,'message': message  })
    else:
        message = "You haven't searched for any image category"
    return render(request, "searchresults.html") 