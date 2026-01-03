from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# def blog_view(request):
#     # return HttpResponse('index_view')
#     # return HttpResponse('<h1>Home Page<h1>')
#     # posts=Post.objects.all()
#     posts=Post.objects.filter(status=1)
#     context={'posts':posts}
#     return render(request, 'blog/blog-home.html',context)

# def blog_view(request,cat_name=None,author_username=None):

# @login_required
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    # if cat_name:
    if kwargs.get('cat_name') != None:
        # posts=posts.filter(category__name=cat_name)
        posts = posts.filter(category__name=kwargs['cat_name'])
    # if author_username:
    #     posts=posts.filter(author__username=author_username)
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    # post=Post.objects.get(id=pid)
    # عدم تمایش پست های غیر انتشار توسط url
    # posts=Post.objects.filter(status=1)
    # post=get_object_or_404(posts,pk=pid)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Yore Comment Submit Successfully')
        else:
              messages.add_message(request,messages.ERROR,'Yore Comment didnt Submit')
    
    post = get_object_or_404(Post, pk=pid, status=1)
    if not post.login_require:
        comments=Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')
        form=CommentForm()
        context = {'post': post,'comments':comments,'form':form}
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    # print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        posts = posts.filter(content__contains=request.GET.get('s'))
        # Warlus
        # if s:=request.GET.get('s'):
        #     posts=posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


# def blog_single(request):
#     # return HttpResponse('index_view')
#     # return HttpResponse('<h1>Home Page<h1>')
#     context={'title':'آموزش زبان انگلیسی مقدماتی سطح A1',
#              'content':'این دوره برای افرادی طراحی شده که می‌خواهند زبان انگلیسی را از پایه و بدون هیچ پیش‌زمینه‌ای شروع کنند. محتوای دوره به‌صورت کاربردی و مرحله‌به‌مرحله تنظیم شده تا زبان‌آموز بتواند به‌آسانی مفاهیم پایه را یاد',
#              'author':'علی وحدتی'}
#     return render(request, 'blog/blog-single.html',context)

def test(request):
    posts = Post.objects.all()
    # posts=Post.objects.filter(status=0)
    context = {'posts': posts}
    return render(request, 'test.html', context)

# def test2(request,name,family,age):
#     context={'name':name,'family':family,'age':age}
#     return render(request,'test2.html',context)


def test2(request, pid):
    # post=Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    # context={'pid':pid}
    return render(request, 'test2.html', context)


