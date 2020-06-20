from django.shortcuts import render
from blog.models import Post, Comments
from .form import CommentForm

def blog_index(request):
	posts = Post.objects.all().order_by('-created_on') # minus sign signifies descending order
	contxt = {'title': ' Blogs', 'posts': posts}

	return render(request, 'blog_index.html', contxt)


def blog_category(request, category):
	posts = Post.objects.filter(
			categories__name__contains=category
		).order_by('-created_on')

	contxt = { 'category': category,
				'posts': posts,
				'title': "Category - "+ category}

	return render(request, 'blog_category.html', contxt)

def blog_detail(request, pkey):
	post = Post.objects.get(pk=pkey)
	form = CommentForm()
	success_msg = ""

	if request.method == 'POST':
		form =  CommentForm(request.POST)
		if form.is_valid():
			comment = Comments(
					author=form.cleaned_data['author'],
					body=form.cleaned_data['body'],
					post=post
				)
			comment.save()
			success_msg = "Successfully Submitted! :)"
			form = CommentForm()
		else:
			success_msg = "Failed to submit. :("

	comments = Comments.objects.filter(post=post)
	contxt = {'title': post.title,
				'post': post,
				'comments': comments,
				'form': form,
				'success_msg': success_msg}

	return render(request, 'blog_detail.html', contxt)


