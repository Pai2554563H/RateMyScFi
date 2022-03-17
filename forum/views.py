from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from forum.models import Post
from forum.models import PostReply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def postList(request):
#     post_list = Post.objects.all()
#     # set how many post per page
#     paginator = Paginator(post_list, 2)
#
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # if user ask for non-integer page number, show page 1
#         posts = paginator.page(1)
#     except EmptyPage:
#         # if user ask for page number exceed the maximum, show last page
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request, 'forum/forum.html', {'posts': posts})

# class ForumView(ListView):
#     model = Post
#     templates_name = 'forum.forum.html'
#     context_object_name = 'post_list'
#     # set the number of post per page
#     paginate_by = 10
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

class ForumView(View):

    def get(self, request):
        post_list = Post.objects.all().values()
        context_dict = {'posts': post_list}
        return render(request, 'forum/forum.html', context_dict)

    def post(self, request):
        pass


class PostView(View):
    def get(self, request, post_id):
        context_dict = {}
        post = Post.objects.get(id=post_id)
        replies = PostReply.objects.filter(post_id=post.id)
        context_dict['replies'] = replies
        context_dict['post'] = post
        return render(request, 'forum/post.html', context=context_dict)


    # def post(self, request):
    #     pass



# @login_required
# def addPost(request):
#     return render(request, 'forum/forum.html')
#
#
# def showPost(request):
#     return render(request, 'forum/forum.html')
