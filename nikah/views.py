from django.shortcuts import render,redirect
from nikah.forms import postForm
from nikah.models import post
from django.contrib import messages 
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'index.htm')

def home(request):
    form = postForm()
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,"Post created")
            return redirect('home')
    return render(request,'home.htm',{'form':form})


def profile(request):
    user = request.user
    return render(request,'profile.htm',{'user':user})

def deletePost(request, id):
    post.objects.get(id=id).delete()
    return redirect('profile')