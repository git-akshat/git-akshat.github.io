from django import forms
from predict_risk.models import Predictions
from predict_risk.models import PredictionsDiabetes

class Predict_Form(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = ('age','sex','cp','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate',
        'exercise_induced_angina','st_depression','st_slope','number_of_vessels','thallium_scan_results')
        widgets = {'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'sex': forms.Select(attrs={'class': 'form-control'}),
                   'cp': forms.Select(attrs={'class': 'form-control'}),
                   'resting_bp':forms.TextInput(attrs={'class': 'form-control'}),
                   'serum_cholesterol':forms.TextInput(attrs={'class': 'form-control'}),
                   'fasting_blood_sugar':forms.Select(attrs={'class': 'form-control'}),
                   'resting_ecg':forms.Select(attrs={'class': 'form-control'}),
                   'max_heart_rate':forms.TextInput(attrs={'class': 'form-control'}),
                   'exercise_induced_angina':forms.Select(attrs={'class': 'form-control'}),
                   'st_depression':forms.TextInput(attrs={'class': 'form-control'}),
                   'st_slope':forms.Select(attrs={'class': 'form-control'}),
                   'number_of_vessels':forms.Select(attrs={'class': 'form-control'}),
                   'thallium_scan_results':forms.Select(attrs={'class': 'form-control'}),
                   }


class Predict_Diabetes_Form(forms.ModelForm):
  class Meta:
      model = PredictionsDiabetes
      fields = ('pregnancies','glucose','bloodpressure','skinthickness','insulin','bmi','pedigree','age')
      widgets = {'pregnancies': forms.TextInput(attrs={'class': 'form-control'}),
                  'glucose':forms.TextInput(attrs={'class': 'form-control'}),
                  'bloodpressure':forms.TextInput(attrs={'class': 'form-control'}),
                  'skinthickness':forms.TextInput(attrs={'class': 'form-control'}),
                  'insulin':forms.TextInput(attrs={'class': 'form-control'}),
                  'bmi':forms.TextInput(attrs={'class': 'form-control'}),
                  'pedigree':forms.TextInput(attrs={'class': 'form-control'}),
                  'age':forms.TextInput(attrs={'class': 'form-control'}),
                  }
