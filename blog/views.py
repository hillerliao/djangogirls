from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Secs
from .forms import PostForm

from rest_framework import viewsets
from .serializers import PostSerializer

from django_tables2 import RequestConfig
from .tables import PostTable, SecsTable

from .crawl_secs import crawl_secs

# for restful api
class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('-published_date')
	serializer_class = PostSerializer

# for html tables of secs
def secs(request):
	crawl_secs()
	table = SecsTable(Secs.objects.all())
	table.order_by = 'gqj_rank' # 指定默认排序
	RequestConfig(request).configure(table)
	# table.paginate(page=request.GET.get('page', 1), per_page=1) # 翻页
	return render(request, 'blog/secs.html', {'table': table})

# for html tables
def post_table(request):
	table = PostTable(Post.objects.all())
	table.order_by = '-id' # 指定默认排序
	RequestConfig(request).configure(table)
	# table.paginate(page=request.GET.get('page', 1), per_page=1) # 翻页
	return render(request, 'blog/post_table.html', {'table': table})

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form  = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})