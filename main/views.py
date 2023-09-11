from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Ghaisan Luqyana Aqila',
        'npm' : '2206830460',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)