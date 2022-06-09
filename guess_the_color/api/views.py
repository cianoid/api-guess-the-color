from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import GuessSerializer


class GuessView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return Response(
            GuessSerializer(request.data).data, status=status.HTTP_200_OK)
