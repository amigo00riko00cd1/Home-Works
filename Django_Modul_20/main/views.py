from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def news(request):
    return render(request, 'news/news.html')

def chapter(request):
    return render(request, 'chapter/chapter.html')

def facts(request):
    return render(request, 'facts/facts.html')

def management(request):
    return render(request, 'management/management.html')

def history(request):
    return render(request, 'history/history_main.html')

def history_people(request):
    return render(request, 'history/history_people.html')

def history_photos(request):
    return render(request, 'history/history_photos.html')
