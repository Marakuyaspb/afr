from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Article

def index(request):
	latest_articles = Article.objects.order_by('-art_pub_date')[:5]
	return render(request, 'articles/list.html', {'latest_articles':latest_articles})

def detail(request, art_id):
	try:
		a = Article.objects.get( id = art_id )
	except: Http404('Статья потерялась')
	return render(request, 'articles/detail.html', {'article': a})

	latest_comments = a.comment_set.order_by('-id')[:10]



def add_comment(request, art_id):
	try:
		a = Article.objects.get(id = art_id)
	except:
		raise Http404('Статья потерялась')

	a.comment_set.create(author_name =  request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('articles.detail', args = (a.id)) )