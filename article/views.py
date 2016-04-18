from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from  django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from article.forms import CommentForm
from article.models import Article, Comments
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" %view
    return HttpResponse(html)

def template_two(request):
    view = 'template_two'
    t = get_template("myview.html")
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_three_simpl(request):
    view = 'template_three'
    return render_to_response("myview.html",{'name':view})

def articles(request, page_number = 1):
    all_articles = Article.objects.all()
    curent_page = Paginator(all_articles,3)
    return render_to_response('articles.html',{'articles':curent_page.page(page_number),  'comments':Comments.objects.all(), 'username':auth.get_user(request).username})

def article(request, article_id = 1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username

    return render_to_response('article.html', args)

def addlike(request, article_id, page_number ):
    try:
        if article_id in request.COOKIES:
            redirect('/page/{}/'.format(page_number))
        else:
            article = Article.objects.get( id = article_id)
            article.article_likes +=1
            article.save()
            response = redirect('/page/{}/'.format(page_number))
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/page/{}/'.format(page_number))


def addcomment(request, article_id):
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id = article_id)
            if request.user.is_anonymous():
                return redirect('/article/get/%s/' % article_id)
            else:
                comment.comments_from = request.user
                form.save()
                return redirect('/article/get/%s/' % article_id)
