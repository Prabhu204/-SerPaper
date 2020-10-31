from django.shortcuts import render, get_object_or_404
from .models import Article, Researchpaper


# All Post View:
def all_post(request):
	posts = Researchpaper.objects.all()
	count = len(posts)
	return render(request, 'post/index.html', {'posts': posts, "count":count})


# Post Detail View:
def post_detail(request, id):
	post = get_object_or_404(Researchpaper, id=id)
	return render(request, 'post/post_detail.html', {"post": post})


# Filter papers as per category:
def filter_post(request, subject):
	# post = get_object_or_404(Researchpaper, id=id)
	print('from filter function',subject)
	# category = post.subject
	results = Researchpaper.objects.filter(subject__exact= subject)
	return render(request, 'post/filteredresult.html', {"posts": results,
														"head_title":subject, "length":len(results)})