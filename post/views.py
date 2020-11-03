from django.shortcuts import render, get_object_or_404
from .models import Article, Researchpaper
from django.views.generic.list import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# All Post View:
def all_post(request):
	posts = Researchpaper.objects.all()
	unique_values = Researchpaper.objects.order_by().values('subject').distinct()
	print(unique_values)
	count = len(posts)
	return render(request, 'post/index.html', {'posts': posts, "count":count, "unique_values":unique_values})


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

class TaskSearch(ListView):
	model = Researchpaper
	template_name = 'post/search_results.html'

	def get_queryset(self):
		query= self.request.GET.get('q')
		object_list = Researchpaper.objects.filter (Q(subject__icontains=query) | Q(title__icontains=query) )
		return object_list