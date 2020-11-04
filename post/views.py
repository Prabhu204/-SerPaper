from django.shortcuts import get_object_or_404
from .models import Researchpaper,Subscription, Contact
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



def index(request):
	return render(request, 'post/index.html', {'abc':'abc'})


def my_paginator(request, posts_list):
	"""It helps for other pages pagination"""
	page = request.GET.get('page', 1)
	paginator = Paginator(posts_list, 10)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return posts

# All Post View:
def all_post(request):
	posts_list = Researchpaper.objects.order_by("title")
	unique_values = Researchpaper.objects.order_by().values('subject').distinct()
	count = len(posts_list)

	posts = my_paginator(request=request, posts_list=posts_list)
	if request.method == 'POST':
		value = request.POST['email']
		try:
			validate_email(value)
		except ValidationError as e:
			messages.error(request, 'Please enter valid email')
		else:
			messages.success(request, 'Your registration was successful')
			email = Subscription.objects.create(email=value)
			email.save()

	return render(request, 'post/research_papers.html', {'posts': posts, "count":count, "unique_values":unique_values})


# Post Detail View:
def post_detail(request, id):
	post = get_object_or_404(Researchpaper, id=id)
	return render(request, 'post/post_detail.html', {"post": post})


# Filter papers as per category:
def filter_post(request, subject):
	results = Researchpaper.objects.filter(subject__exact= subject)
	posts = my_paginator(request=request, posts_list=results)
	return render(request, 'post/category.html', {"posts": posts,
														"head_title":subject, "length":len(results)})


def search_result(request):
	"""It has url pattern for preserving your query in the url"""
	GET_params = request.GET.copy()
	if 'page' in GET_params:
		del GET_params['page']
	query = request.GET.get('q')
	object_list = Researchpaper.objects.filter(Q(subject__icontains=query) | Q(title__icontains=query))
	length = len(object_list)
	object_list = my_paginator(request=request, posts_list=object_list)
	return render(request, 'post/search_results.html', {"object_list": object_list, "length":length,
														'GET_params':GET_params})


def contactView(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)

	if form.is_valid():
		subject = form.cleaned_data['subject']
		from_email = form.cleaned_data['from_email']
		message = form.cleaned_data['message']
		data = Contact.objects.create(email=from_email,subject = subject, message= message)
		data.save()
		print(subject,from_email,message)
		# try:
		# 	send_mail(subject, message, from_email, ['admin@example.com'])
		# except BadHeaderError:
		# 	return HttpResponse('Invalid header found.')
		return redirect('success')
	return render(request, "post/email.html", {'form': form})

def successView(request):
	return HttpResponse('Success! Thank you for your message.')