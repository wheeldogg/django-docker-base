""" Views relating to API functionality"""

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

class HelloWorldView(APIView):
    def get(self, request, *args, **kwargs):
        # any query params
        # method = self.request.query_params.get("method", None)
        data = {'Hello' : 1, 'World' : 2}
        
        return Response(data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        pass
    