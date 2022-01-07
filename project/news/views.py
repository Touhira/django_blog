from django.shortcuts import render
from . models import News
from django.views.generic import DetailView

# Create your views here.
def news(request):
    news = News.objects.order_by('-date')
    return render(request,'news/news.html', {'news': news})

class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'