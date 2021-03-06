from django.shortcuts import render, get_object_or_404, redirect
from .models import Cupcake
from .forms import CupcakeForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def cupcake_list(request):
    cakes = Cupcake.objects.all().order_by('-createdAt')
    context = {"cakes":cakes}
    return render(request, "menu/list.html", context)

def price_hightolow(request):
    cakes = Cupcake.objects.all().order_by('-price')
    context = {"cakes":cakes}
    return render(request, "menu/list.html", context)

def price_lowtohigh(request):
    cakes = Cupcake.objects.all().order_by('price')
    context = {"cakes":cakes}
    return render(request, "menu/list.html", context)

def rating_hightolow(request):
    cakes = Cupcake.objects.all().order_by('-rating')
    context = {"cakes":cakes}
    return render(request, "menu/list.html", context)


def cupcake_detail(request, pk):
    cake = get_object_or_404(Cupcake, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = cake
            comment.writer = request.user
            comment.approved_comment = True
            comment.save()
            return redirect('menu:cupcake_detail', pk=cake.pk)
    else:
        form = CommentForm()
    context = {'cake':cake, 'form':form}
    return render(request, 'menu/detail.html', context)


@login_required
def cupcake_new(request):
    if request.method == "POST":
        form = CupcakeForm(request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.createdAt = timezone.now()
            cake.writer = request.user
            cake.save()
            return redirect('menu:cupcake_detail', pk=cake.pk)
    else:
        form = CupcakeForm()
    context = {'form':form}
    return render(request, 'menu/cupcake_new.html', context)
