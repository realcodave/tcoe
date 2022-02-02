from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from operator import attrgetter
from .models import BlogPost


# Create your views here.
def blog(request):
    blog_post = sorted(BlogPost.objects.all(),
                       key=attrgetter('date_updated'), reverse=True)
    content = {"blog_post": blog_post}
    return render(request, "blog/blog.html", content)

def detail(request, slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post
    return render(request, "blog/detail_blog.html", context)
