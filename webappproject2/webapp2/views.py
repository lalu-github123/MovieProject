from django.shortcuts import render,redirect
from .models import film1
from .models import film
from .forms import MovieForm


# Create your views here.
def home(request):
    movie = film1.objects.all()
    context = {'movielist': movie}
    return render(request,"home.html",context)
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie1=film1(name=name, desc=desc, year=year, img=img)
        movie1.save();
    return render(request,"add.html")
def detail(request,id):
    movie=film.objects.get(id=id)
    return render(request,"show.html", {'movie':movie})
def update(request,id):
    movie = film1.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form})
def delete(request,id):
    if request.method=='POST':
        movie=film1.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")

