from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})

class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-list')
        return render(request, 'blog/post_form.html', {'form': form})

class PostUpdateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
        return render(request, 'blog/post_form.html', {'form': form})

class PostDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_confirm_delete.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post-list')

class CommentCreateView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            print("valid form")
            comment = form.save(commit=False)
            comment.post = post
            comment.comment_author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)
        return render(request, 'blog/post_detail.html', {'post': post, 'form': form})