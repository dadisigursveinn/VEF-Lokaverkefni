from django.shortcuts import render

from .forms import SignUpForm
# Create your views here.
def home(request):
	#if request.user.is_authenticated():
	title = "My Title"
	

	#if request.method == "POST":
	#	print request.POST

	form = SignUpForm(request.POST or None) #or None = dont run validators on refresh

	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		#form.save()  skips stuff we can do to data

		#use this if we want to format data
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()

		context = {
			"title" : "Thank you"
		}
	return render(request, "home.html", context)
