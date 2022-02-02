from django.shortcuts import render
from .forms import CreateTestimonyForm, NewsletterForm
# Create your views here.


def index(request):

    context = {}
    form = CreateTestimonyForm(request.POST or None, request.FILES or None)
    form1 = NewsletterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        form = CreateTestimonyForm()
    if form1.is_valid():
        obj = form1.save(commit=False)
        obj.save()
        form = NewsletterForm()
    context['form'] = form
    context['form1'] = form1
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def liveStream(request):
    return render(request, 'main/livestream.html')


def services(request):
    return render(request, 'main/services.html')