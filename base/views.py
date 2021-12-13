from django.shortcuts import render
from django.http import HttpResponse
from base.models import UrlTable
import uuid
from base.forms import UrlForm

# Create your views here.
def index_view(request):
    form = UrlForm()
    return render(request, 'base/index.html', {
        'form':form
    })

def process_url(request):
    url, uid, url_obj = None, None, None
    if request.method == 'POST' and 'shorten' in request.POST:
        try:
            url = request.POST.get('name')
            uid = str(uuid.uuid4())[:7]
            url_obj = UrlTable(name=url, uuid=uid)
        except KeyError as e:
            print(e)
        else:
            url_obj.save()
    return HttpResponse(f"<a href='{url_obj.name}' class='response'>localhost:8000/{url_obj.uuid}</a>")