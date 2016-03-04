from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from django.db.models import Q
from .models import Post, Category, Author, Tag


# from django.conf import settings
# from django.template import RequestContext
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from polls.models import Question, Choice
def view_home(request):
    posts = Post.objects.order_by('-published_date')[0:5]
    return render(request, '../templates/tikhinuch4/index.html', {'post': posts})

def view_home_en(request):
    # posts = Post.objects.order_by('-published_date')[0:5]
    return render(request, '../templates/tikhinuch4/index-en.html', {})

def view_about(request):
    return render(request, 'blog/about.html', {})

def view_scholarships(request):
    return render(request, 'blog/scholarships.html',{})

def view_post_list(request):
    today = timezone.now().date()
    #, status='p', category=cat.pk
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    category = Category.objects.all()
    #
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
            # Q(author__icontains=query)
            # Q(categories=query)
        ).distinct()

    paginator = Paginator(posts, 2)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context={
        "posts":queryset,
        "title":"list",
        "page_request_var":page_request_var,
        "today": today,
    }

    return render(request, 'blog/post_list.html', context)


def view_post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})