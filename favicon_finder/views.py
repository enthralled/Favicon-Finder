import json

from django.http import HttpResponse
from django.shortcuts import render

from .forms import FaviconForm
from .models import Favicon


def search_view(request):

    if request.method == 'POST':
        input_url = request.POST.get('fav_url')
        get_fresh = (request.POST.get('checked'))
        host_name = Favicon.clean_url(input_url)

        data = Favicon.get_from_db_or_request(host_name, get_fresh)
        return HttpResponse(
            json.dumps(data),
            content_type='application/json')

    else:
        form = FaviconForm()
        return render(request, 'favicon/base.html', {'form': form})
