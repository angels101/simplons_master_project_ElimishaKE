from news.models import Article
from . import views
from django.urls import path
from django.conf.urls .static import static
from django.conf import settings


urlpatterns = [
        path('', views.welcome, name= 'welcome'),
        path('news_today/', views.news_today, name='newsToday'),
        path('archives/<str:past_date>/', views.past_days_news, name = 'pastNews'),
        path('search/', views.search_results, name='search_results'),
        #path('article/(\d+)', views.article, name='article'),
        path('new/article', views.new_article, name='new-article'),
        path('ajax/newsletter/', views.newsletter, name='newsletter'),
        path('api/merch/', views.MerchList.as_view()),
        path('api/merch/merch-id/(?p<pk>[0-9]+)/', views.MerchDescription.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
