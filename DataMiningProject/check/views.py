from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import pickle
import numpy as np

# Create your views here.
def check(request):
    predict = None
    if request.method == 'POST':
        user_length = request.POST.get('user_length')
        user_has_num = request.POST.get('user_has_num')
        name_length = request.POST.get('name_length')
        name_has_num = request.POST.get('name_has_num')
        is_private = request.POST.get('is_private')
        recent_join = request.POST.get('recent_join')
        is_business_acc = request.POST.get('is_business_acc')
        data = [
                int(user_length),
                int(user_has_num),
                int(name_has_num),
                int(name_length),
                int(is_private),
                int(recent_join),
                int(is_business_acc)
            ]
        predict = load_model([data])
        print("prediction: " + str(predict))
    return render(request, 'check/predict.html', {'predict' : predict})

def index(request):
    return render(request, 'check/index.html')

model = None

def load_model(data):
    global model
    if model is None:
        with open('check/model.pkl', 'rb') as f:
            model = pickle.load(f)
    result = model.predict(data)[0]

    return result