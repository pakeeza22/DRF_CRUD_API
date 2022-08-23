from rest_framework import generics, viewsets, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import AdminRenderer, JSONRenderer
from rest_framework.response import Response
# from knox.models import AuthToken
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.views import JWTAuthentication

from .serializers import RegisterSerializer, EmployeeSerializer
from .models import Employee


# Register API
class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    # form_class = UserCreationForm
    authentication_classes = [BasicAuthentication]

    permission_classes = [AllowAny]
    renderer_classes = [ JSONRenderer]

    # def create(self, request):
    #     serializer = RegisterSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({
    #         # "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "user": str(request.user),
    #         "auth": str(request.auth)
    #     })
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({
    #         # "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "user": str(user.username),
    #         "auth": str(request.auth)
    #     })


# class EmployeeViewSet(viewsets.ModelViewSet):
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         authentication_classes = [JWTAuthentication]
#         permission_classes = [IsAuthenticated]
#         user = self.request.user
#         return Employee.objects.filter(user=user)


# class EmployeeList(ListAPIView):
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         authentication_classes = [JWTAuthentication]
#         permission_classes = [IsAuthenticated]
#         user = self.request.user
#         return Employee.objects.filter(user=user)
#
#
# class EmployeeCreate(CreateAPIView):
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         authentication_classes = [JWTAuthentication]
#         permission_classes = [IsAuthenticated]
#         user = self.request.user
#         return Employee.objects.filter(user=user)
#
#
# class EmployeeRetrieve(RetrieveAPIView):
#     def get_queryset(self):
#         authentication_classes = [JWTAuthentication]
#         permission_classes = [IsAuthenticated]
#         user = self.request.user
#         return Employee.objects.filter(user=user)
#
#
# class EmployeeUpdate(LoginRequiredMixin, UpdateAPIView):
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         authentication_classes = [JWTAuthentication]
#         permission_classes = [IsAuthenticated]
#         user = self.request.user
#         return Employee.objects.filter(user=user)
#
#
# class EmployeeDestroy(DestroyAPIView):
#     serializer_class = EmployeeSerializer
#
#     def get_queryset(self):
#         authentication_classes = [JWTAuthentication]
#         permission_classes = [IsAuthenticated]
#         user = self.request.user
#         return Employee.objects.filter(user=user)


class EmployeeListCreate(ListCreateAPIView):
    model = Employee
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        user = self.request.user
        return self.model.objects.all().filter(user=user)


class EmployeeRUD(RetrieveUpdateDestroyAPIView):
    model = Employee
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        user = self.request.user
        return self.model.objects.all().filter(user=user)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
