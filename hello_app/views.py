from django.shortcuts import render

# Create your views here.
def index_view(requests):
    return render(request, "index.html")