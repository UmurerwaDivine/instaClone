from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .email import send_welcome_email
from .form import CommentForm, NewImageForm, NewProfileForm
from .models import Comment, Image, Profile


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request,"all-insta/index.html",{"images":images,"form":form,"comments":comments})
# Create your views here.
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-insta/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-insta/search.html',{"message":message}) 
# def new_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.editor = current_user
#             profile.save()
#         return redirect('index')

#     else:
#         form = NewProfileForm()
#     return render(request, 'all-insta/new-profile.html', {"form": form})

# @login_required(login_url='/accounts/login/') 
# def profile(request):
#     try:
#         profile = Profile.objects.all()
#     except ObjectDoesNotExist:
#         raise Http404()
#     return render(request,"all-insta/profile.html", {"profile":profile})
# def new_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             bio = form.save(commit=False)
#             bio.user = current_user
#             bio.save()
#         return redirect('profile')
#     elif Profile.objects.filter(user=current_user):
#         profile = Profile.objects.filter(user=current_user).first()
#         form = NewProfileForm(instance=profile)
#     else:
#         form = NewProfileForm()

#     return render(request,'all-insta/new-profile.html',{"form":form})
@login_required(login_url='accounts/login/')
def image(request):
    current_user = request.user
    try:
        # user = User.objects.get(username = username)
        profile = Profile.objects.get(user = current_user)
        images = Image.objects.get(profile = profile)
        
    except ObjectDoesNotExist:
        return redirect('image',request.user)

    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
    else:
        form = NewImageForm()
    return render(request,"newpost.html",{"profile":profile, "images":images, "form":form})
