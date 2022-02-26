from django.shortcuts import render
from rest_framework.views import APIView
class Sub(APIView):
    def get(selt,request) :
        print("method:get")
        return render(request,"junstagram/main.html")
    def post(selt,request) :
        print("method:post")
        return render(request,"junstagram/main.html")
