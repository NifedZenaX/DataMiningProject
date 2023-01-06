from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import pickle
import numpy as np

class IGData(forms.Form):
    user_length = forms.CharField(label="Username length")
    user_has_num = forms.BooleanField(label="Does your username has any numbers", widget=forms.RadioSelect(choices=[(1, "Yes"), (2, "No")]),required=False)
    name_length = forms.CharField(label="Full name length")
    name_has_num = forms.BooleanField(label="Does your full name has any numbers", widget=forms.RadioSelect(choices=[(1, "Yes"), (0, "No")]),required=False)
    is_private = forms.BooleanField(label="Is your account private", widget=forms.RadioSelect(choices=[(1, "Yes"), (0, "No")]),required=False)
    recent_join = forms.BooleanField(label="Do you recently joined instagram", widget=forms.RadioSelect(choices=[(1, "Yes"), (0, "No")]),required=False)
    is_business_acc = forms.BooleanField(label="Is this account a business account", widget=forms.RadioSelect(choices=[(1, "Yes"), (0, "No")]),required=False)

# Create your views here.
def check(request):
    predict = None
    if request.method == 'POST':
        form = IGData(request.POST)
        if form.is_valid():
            data = [
                int(form.cleaned_data['user_length']),
                int(form.cleaned_data['user_has_num']),
                int(form.cleaned_data['name_has_num']),
                int(form.cleaned_data['name_length']),
                int(form.cleaned_data['is_private']),
                int(form.cleaned_data['recent_join']),
                int(form.cleaned_data['is_business_acc'])
            ]
            predict = load_model([data])
            print("prediction: " + str(predict))
    return render(request, 'check/predict.html', {'predict' : predict})

def index(request):
    form = IGData()
    return render(request, 'check/index.html', {'form': form})

def load_model(data):
    with open('D:\OneDrive - Bina Nusantara\Tugas2\Semester-5\Data Mining\model.pkl', 'rb') as f:
        model = pickle.load(f)

    result = model.predict(data)[0]

    return result