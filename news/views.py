from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from news.models import Article
from .forms import NewsLetterForms,NewArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, 'all-news/welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html',{"date": date})



def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        pass
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        # assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html',{"date" : date})


def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date, "news": news})


def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

#@login_required(login_url='/accounts/login/')
#def article(request,article_id):
#    try:
#        article = Article.objects.get(id = article_id)
#    except DoesNotExist:
#
#        raise Http404()
#
#    return render(request,"all-news/article.html", {"article":article})
@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('NewsToday')

    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})


def news_today(request):
    if request.method == 'POST':
        form = NewsLetterForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name =name, email=email)
            recipient.save()
            HttpResponseRedirect('news_today')
            #print('valid')

    else:
        form = NewsLetterForms()
    return render(request, 'all-news/today-news.html', {"date": date, "news":news, "letterForm":form})




