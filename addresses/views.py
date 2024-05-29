
from .serializers import AddressSerializer
from .models import Address
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Addresses(APIView):
    ''' Display all addresses in home page '''

    def get_object(self, pk):
        try:
            address = Address.objects.filter(pk=pk)
            return address
        except Address.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug=None, format=None):
        if slug is None:
            addresses = Address.objects.all()
            serializer = AddressSerializer(addresses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        addresses = self.get_object(pk=slug)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    ''' Get details of address by address name or address city '''

    def post(self, request):
        address = AddressSerializer(data=request.data)
        if address.is_valid():
            address.save()
            return Response(address.data, status=status.HTTP_201_CREATED)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)

    ''' Update address details '''

    def put(self, request, slug=None):
        try:
            address = Address.objects.get(slug=slug)
            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Address.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    ''' Delete address details '''

    def delete(self, request, slug=None):
        try:
            address = Address.objects.get(id=slug)
            address.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Address.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
