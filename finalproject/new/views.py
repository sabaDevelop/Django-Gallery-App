from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import PhotoForm
from .models import Photo


@login_required
def index(requset):
    img=Photo.objects.all()
    return render(requset, "new/index.html" , {'img':img})


def upload(request):
    if request.method == "POST":
        form=PhotoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse('new:index')) 
    else:
        form=PhotoForm()
        return render(request, "new/img_upload.html", {'form':form})