
from django.http import JsonResponse

# Create your views here.


data = {

   "Name" : "Alison Salomon",

    "Track" : "Backend(Python)",

    "Message" : "Hi mentors, you're doing a great job! Thank you! :)"

}
def index(request):
    return JsonResponse(data)