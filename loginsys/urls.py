from django.conf.urls import url,include,patterns
import article
urlpatterns = [
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
    url(r'^', 'article.views.articles'),

]