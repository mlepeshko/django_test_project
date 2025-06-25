from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'register_journal/post_list.html', {})
