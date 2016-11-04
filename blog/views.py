from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})
def post_details(request, id):
    """create a view that returns a single Post object based on the post ID and render it to the 'postdetail.html'
    template.Or return a 404 error if the post is not found"""
    post = get_object_or_404(Post, pk=id)
    return render(request, "postdetail.html", {'post': post})
def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1#clock up the number of post views
    post.save()
    return render(request, "postdetail.html",{'post':post})