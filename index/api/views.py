from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PalindromaSerializer


class PostWord(APIView):
    def post(self, request):
        palabra = request.POST.get("palabra")
        serializer = PalindromaSerializer(data=request.data)

        if serializer.is_valid():
            if is_palindrome(palabra):
                serializer.save()
                return Response(status=status.HTTP_200_OK,
                                data={"icon": "success", "message": f"La palabra es palíndroma"})
            else:
                return Response(status=status.HTTP_200_OK,
                                data={"icon": "warning", "message": f"La palabra no es palíndroma"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"icon": "error", "message": f"Campo Vacío"})


def is_palindrome(palabra):
    palabra = palabra.lower().replace(" ", "")  # Simplifica la manipulación de la palabra
    return palabra == palabra[::-1]
