
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.
class TestApiView(APIView):
    def get(self, request):
        return JsonResponse( {'key':'data is exchanged'},status = 500)
    def post(self, request):
        return JsonResponse( {'key':'data is changed'},status = 500)