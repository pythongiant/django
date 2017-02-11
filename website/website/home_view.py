from django.http import HttpResponse
def index(request):
    return HttpResponse("Music app homepage click <a href='http://127.0.0.1:8000/music'>here</a> to go to the actual music app")