from django import forms
from .models import product


class newproduct(forms.ModelForm):
    class Meta:
        model=product
        fields=('category','name','description','price','image',)
        widgets={
        "category":forms.Select(attrs={'class':'w-full py-4 px-6 rounded-xl border'}),
         "name":forms.TelInput(attrs={'class':'w-full py-4 px-6 rounded-xl border'}),
          "description":forms.Textarea(attrs={'class':'w-full py-4 px-6 rounded-xl border'}),
           "price":forms.TelInput(attrs={'class':'w-full py-4 px-6 rounded-xl border'}),
            "image":forms.FileInput(attrs={'class':'w-full py-4 px-6 rounded-xl border'})
        }    
    