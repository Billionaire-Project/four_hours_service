from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class UserTest(APIView):
    def get(self, request):
        print(request)

        response = {
            "status": HTTP_200_OK,
            # "user": request.user,
        }
        return Response(response, status=HTTP_200_OK)
