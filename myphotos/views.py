from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from .forms import PhotoForm
def list(request):
    title = "My Title"
	form = PhotoForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
    # Handle file upload
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect(reverse('ljosmyndasida.myphotos.views.list'))

    # Render list page with the documents and the form
    return render(request, "list.html", context)