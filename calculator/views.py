from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class additionview(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)

        print(request_body)
        print(type(request_body))
        data={
            "message":"api call for addition working successfully....!"
        }
        return JsonResponse(data)
class substractionview(View):
    def post(self,request):
            request_body=request.body
            form_data=loads(data)
            n1=form_data.get("num1")
            n2=form_data.get('num2')
            differance=n1-n2
            result={
                 "differance":differance
            }
    
            print(request_body)
            print(type(request_body))
            data={
                "message":"api call for addition working successfully....!"
            }
            return JsonResponse(data)
@method_decorator(csrf_exempt,name='dispatch')
class bmiview(View):
     def post(self,request):
          payload=request.body
          form_data=loads(payload)
          weight=form_data.get('weight')
          height=form_data.get('height')
          bmi=weight/(height**2)
          result={
               "BMI:bmi"
          }
          return JsonResponse(result)

class RectangleArea(APIView):

    def post(self, request):
        length = request.data['length']
        width = request.data['width']

        area = length * width

        {
            "area": area
        }
        return JsonResponse(area)