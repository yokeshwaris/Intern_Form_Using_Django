from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from .models import PersonalDetails
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import PersonalDetailSerializer

class PersonalDetailCreateView(APIView):
    # authentication_classes = [OAuth2Authentication]TokenHasReadWriteScope
    permission_classes = [IsAuthenticated,]
    # @swagger_auto_schema(
    #     request_body=PersonalDetailSerializer
    #     )
    def get(self, request):
        queryset = PersonalDetails.objects.all()
        serializer_class3 = PersonalDetailSerializer(queryset, many=True)
        return Response(serializer_class3.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_class4 = PersonalDetailSerializer(data=request.data)
        if serializer_class4.is_valid():
            serializer_class4.save()
            return Response(serializer_class4.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class4.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonalDetailUpdateDeleteView(APIView):
     permission_classes = [IsAuthenticated]
     @swagger_auto_schema(
        request_body=PersonalDetailSerializer
        )
     def get_object(self,pk):
        try:
            return PersonalDetails.objects.get(pk=pk)
        except PersonalDetails.DoesNotExist:
            return None

     def put(self,request,pk):
        queryset = self.get_object(pk)
        serializer_class5 = PersonalDetailSerializer(queryset,data=request.data)
        if serializer_class5.is_valid():
            serializer_class5.save()
            return Response(serializer_class5.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_class5.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class PersonalDetailCreateView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = PersonalDetails.objects.all()
#     serializer_class = PersonalDetailSerializer 
    
# class PersonalDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = PersonalDetails.objects.all()
#     serializer_class = PersonalDetailSerializer
    

