from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'blog/main.html',{})

def result(request):
    return render(request, 'blog/result.html',{})