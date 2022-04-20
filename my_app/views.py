from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')


def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    context = {
        'amount': amount,
    }
    return render(request, 'counter.html', context)
