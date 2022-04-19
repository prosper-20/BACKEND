from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def counter(request):
    words = request.GET['text']
    amount = len(words.split())
    context = {
        'amount': amount,
    }
    return render(request, 'counter.html', context)
