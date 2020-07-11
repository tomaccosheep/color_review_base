from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Item, Color, Review

def index(request):
	if request.method == 'POST': # if it's a post request

		# get info out of request
		post_item_id = int(request.POST['item']) 
		post_color_id = int(request.POST['color'])
		post_score = int(request.POST['score'])
		
		# make a new review with that information
		new_rev = Review(
			item_id=post_item_id,
			color_id=post_color_id,
			score=post_score,
		)
		new_rev.save()
		
		return HttpResponseRedirect('/colors/')

	# If it's a get request
	context = {
		'items_context': Item.objects.all(),
		'colors_context': Color.objects.all(),
		'scores_context': range(5, 0, -1),
	}
	return render(
		request,
		'colors/index.html',
		context
	)
