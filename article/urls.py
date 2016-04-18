from django.conf.urls import url,include,patterns
import article
urlpatterns = [
    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_three_simpl'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^article/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^articles/addlike/(?P<article_id>\d)/(?P<page_number>\d)/$', 'article.views.addlike'),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^page/(\d+)/$', 'article.views.articles'),
    url(r'^', 'article.views.articles'),

]