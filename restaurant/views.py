from django.shortcuts import render
from django.views import View

# Create your views here.

class index(View):
    def get(self, request):
        context = {}
        return render(request, "index.html", context)