from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_view(request):
    return Response({"message": "Hola, esta es la API de usuarios!"})
