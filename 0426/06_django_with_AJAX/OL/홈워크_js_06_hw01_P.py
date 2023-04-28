from django.shortcuts import redirect
from .models import Article
from django.views.decorators.http import require_POST
from django.http import __(a)__

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = __(b)__
        if __(c)__:
            article.like_users.remove(request.user)
            liked = False
        else:
            article.like_users.add(request.user)
            liked = True
            
        like_status = {
            'liked': liked, 
            'likeCount': article.like_users.count(),
        }
        return __(a)__(like_status)
    
    return redirect('accounts:login')