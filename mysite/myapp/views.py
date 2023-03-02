from django.http import HttpResponse

def display(request):
    html = "skye8 internship: django"
    return HttpResponse(html)
def display2(request):
    html = "How I became a Django expert"
    return HttpResponse(html)

# Create your views here.
