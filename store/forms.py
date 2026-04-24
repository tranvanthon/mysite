from django import forms

class BarcodeScanForm(forms.Form):
    barcode_input = forms.CharField(
        label='Quét mã vạch', 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Đưa mã vạch vào đây...',
            'autofocus': True, # Tự động focus vào ô này khi tải trang
        })
    )