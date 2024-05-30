from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from accounts.models import User, UserDocument, UserWithName
from accounts.serializers import UserSerializer, UserDocumentSerializer, UserWithNameSerializer


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return True

        if obj.user == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
        # if request.method in SAFE_METHODS:
        #     return True

        # # Write permissions are only allowed to the owner of the blog.
        # return obj.author == request.user
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

class UserDocumentView(ModelViewSet):
    queryset = UserDocument.objects.all()
    serializer_class = UserDocumentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

# class Users(APIView):
#     '''
#     Login page for user
#     '''

#     def get_object(self, pk):
#         try:
#             user = User.objects.filter(id=pk)
#             return user
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk, format=None):
#         users = self.get_object(pk=pk)
#         if users is []:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, pk, format=None):
#         user = self.get_object(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class AllUsers(APIView):

#     ''' Display all users'''

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
