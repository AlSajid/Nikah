from django.shortcuts import render,redirect
from nikah.forms import postForm
from nikah.models import post
from django.contrib import messages 
from notifications.signals import notify
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
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request,"প্রকাশিত হয়েছে")
            return redirect('home')
    posts = post.objects.all()
    return render(request,'home.htm',{'form':form,'posts':posts})


def profile(request):
    user = request.user
    return render(request,'profile.htm',{'user':user})

def deletePost(request, id):
    post.objects.get(id=id).delete()
    return redirect('profile')

def interest(request, id):
    Post = post.objects.get(id=id)
    notify.send(request.user, recipient = post.author,  verb=f''' <a href="/otherprofile/{request.user.username}/">{request.user.first_name} {request.user.last_name}</a>'''+"আগ্রহ প্রকাশ করেছেন ।")
    return redirect('home')