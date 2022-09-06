from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


from django.shortcuts import render, get_object_or_404
from .models import Post, PublishedManager
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    posts = Post.published.all()
    posts1 = PublishedManager()
    return render(request, 'blog/post/list.html', {'posts': posts, 'posts1':posts1})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                                publish__month=month,  publish__day=day)
    return render(request,   'blog/post/detail.html', {'post': post})

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'page': page,'posts': posts})

from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list1.html'

