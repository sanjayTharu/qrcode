from django.shortcuts import render
import qrcode
from io import BytesIO
from django.core.files import File
import base64

# Create your views here.

def index(request):
    url=request.POST.get('url')
    img=qrcode.make(url)
    buffer=BytesIO()
    img.save(buffer)
    buffer.seek(0)
    img_str=base64.b64encode(buffer.read()).decode()
    return render(request,'qr/index.html',{'img_str':img_str})
