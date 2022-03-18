from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

from forum.models import Post
from forum.models import PostReply
from forum.forms import PostForm, ReplyForm
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

class AddPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        form = PostForm()
        return render(request, 'forum/add_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save(commit=True)
            # automatically fill the author for user when posting
            return redirect(reverse('forum:forum'))
        else:
            print(form.errors)
        return render(request, 'forum/add_post.html', {'form': form})


class ForumView(View):

    def get(self, request):
        post_list = Post.objects.all().values()
        context_dict = {'posts': post_list}
        return render(request, 'forum/forum.html', context_dict)


class PostView(View):
    def get(self, request, post_id):
        context_dict = {}
        post = Post.objects.get(id=post_id)
        replies = PostReply.objects.filter(post_id=post.id)
        context_dict['replies'] = replies
        context_dict['post'] = post
        return render(request, 'forum/post.html', context=context_dict)


class AddReplyView(View):

    @method_decorator(login_required)
    def get(self, request, post_id):
        user = request.user
        post = Post.objects.get(id=post_id)
        form = ReplyForm()
        context_dict = {'form': form, 'post': post}
        return render(request, 'forum/add_reply.html', context=context_dict)

    def post(self, request, post_id):
        form = ReplyForm(request.POST)
        post = Post.objects.get(id=post_id)
        if form.is_valid():
            if post:
                reply = form.save(commit=False)
                reply.author = request.user
                reply.post = post
                reply.save()
            # automatically fill the author for user when posting
            return redirect(reverse('forum:show_post', kwargs={'post_id': post_id}))
        else:
            print(form.errors)


