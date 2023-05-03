# Django import
from django.http import JsonResponse
from django.shortcuts import render

# Drf import
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# 사용자 모듈 import
from .models import BraiilePicture, KoreanPicture
from .serializers import BraiilePictureSerializer, KoreanPictureSerializer
from .braiile import play
from .translate import PyJsHoisted_analyze_b_

import os
import pytesseract

def index_view(request):
    if request.method == 'POST':
        BP = BraiilePicture()
        BP.image = request.FILES["images"]
        BP.save()
        full_name = BraiilePicture.objects.all()
        img = full_name[0].image
        return render(request, 'index.html', {'img': img})

    elif request.method == 'GET':
        return render(request, 'index.html')


class BraiileVeiwSet(viewsets.ModelViewSet):
    '''
    2가지 설정이 필요
    1. braiile.py 의 chromedriver의 절대경로 변경해주기 
    2. 아래 변수 temp 절대경로 
    '''
    queryset = BraiilePicture.objects.all()
    serializer_class = BraiilePictureSerializer

    # @action(detail=False, methods=['GET'])
    # def search(self, request):

    #     # 사진 쌓이는것 방지 (메모리 관련 문제)
    #     temp ='./media'
    #     file_name = os.listdir(temp)[0]
    #     full_name = os.path.abspath(temp + "\\" + file_name)
    #     braille = play(full_name)
    #     answer = str(PyJsHoisted_analyze_b_(1, braille))
    #     os.remove(full_name)

    #     # DB 삭제
    #     BraiilePicture.objects.all().delete()

    #     return JsonResponse({'answer': answer, 'braille': braille})
    
    @action(detail=False, methods=['GET'])
<<<<<<< HEAD:Kyebraiile/main/views.py
    def translate(self, request):

        # 사진 쌓이는것 방지 (메모리 관련 문제)
        temp = os.getcwd() + r'/media/Braille/'
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        braille = play(full_name)
        answer = str(PyJsHoisted_analyze_b_(1, braille))
        os.remove(full_name)

        # DB 삭제
        BraiilePicture.objects.all().delete()

        return JsonResponse({'answer': answer, 'braille': braille})
    
    
class KoreanVeiwSet(viewsets.ModelViewSet):
    queryset = KoreanPicture.objects.all()
    serializer_class = KoreanPictureSerializer
    
    @action(detail=False, methods=['GET'])
    def translate(self, request):
        
        # 사진 쌓이는것 방지 (메모리 관련 문제)
        temp = os.getcwd() + r'/media/Korean/'
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        
        pytesseract.pytesseract.tesseract_cmd=r"C:\Users\j3hea\OneDrive\바탕 화면\Python-CapstonDesign-main\Tesseract-OCR\tesseract.exe"
        korean = pytesseract.image_to_string(full_name, lang="kor+eng")
        
        os.remove(full_name)
        KoreanPicture.objects.all().delete()
        

        # DB 삭제

        return JsonResponse({'korean': korean})
    
