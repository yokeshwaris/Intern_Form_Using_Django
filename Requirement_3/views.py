from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from .serializers import InternsEnquiryFormSerializers
from .models import InternsEnguiryForm

# class InternsEnquiryFormView(APIView):
#     # authentication_classes = [OAuth2Authentication]TokenHasReadWriteScope
#      permission_classes = [IsAuthenticated,]
#      def get(self,request):
#         queryset = InternsEnguiryForm.objects.all()
#         serializer_class6 = InternsEnquiryFormSerializers(queryset , many = True)
#         return Response(serializer_class6.data, status= status.HTTP_200_OK)
    
#      def post(self, request):
#         serializer_class7 = InternsEnquiryFormSerializers(data=request.data)
#         if serializer_class7.is_valid():
#             serializer_class7.save()
#             return Response(serializer_class7.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class7.errors, status=status.HTTP_400_BAD_REQUEST)
# class InternsEnquiryFormUpdateDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get_object(self,id):
#         try:
#            return InternsEnguiryForm.objects.get(id=id)
#         except InternsEnguiryForm.DoesNotExist :
#             return None
#     def put(self,request,id):
#         queryset = self.get_object(id)
#         serializer_class8 = InternsEnquiryFormSerializers(queryset,data=request.data)
#         if serializer_class8.is_valid():
#             serializer_class8.save()
#             return Response(status=status.HTTP_202_ACCEPTED)
#     def delete(self,id):
#         queryset = self.get_object(id)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
class InternsEnquiryFormView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=InternsEnguiryForm.objects.all()
    serializer_class = InternsEnquiryFormSerializers
    
class InternsEnquiryFormUpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=InternsEnguiryForm.objects.all()
    serializer_class = InternsEnquiryFormSerializers
    