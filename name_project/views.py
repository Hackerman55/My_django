from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Author
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'name_project/news_list.html', {'articles': articles})

def get_article(request, article_id):
    try:
        articles = Article.objects.get(id = article_id)
        author = Author.objects.filter(article__pk=article_id)
    except (Article.DoesNotExist, Author.DoesNotExist) as error:
        return HttpResponseNotFound(error)
    return render(request, 'name_project/news_article.html',
                  {'articles': articles,
                   'author' : author
                   }
                  )
def new_article(request):
    form = ArticleForm()
    return render(request, 'name_project/edit_article.html', {'form': form})



'''articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]'''
