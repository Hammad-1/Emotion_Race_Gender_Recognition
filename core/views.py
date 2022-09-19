from django.shortcuts import render, redirect
from PIL import Image
from deepface import DeepFace
import base64


def core(request):

    if request.method == 'POST':
        img = request.FILES['avatar'].read()
        encoded = base64.b64encode(img).decode('ascii')
        mime = "image/jpg"
        mime = mime + ";" if mime else ";"
        input_image = "data:%sbase64,%s" % (mime, encoded)
        predictions = DeepFace.analyze(input_image)
        context = {
            'emotion': predictions['dominant_emotion'],
            'gender': predictions['gender'],
            'race': predictions['dominant_race']
        }
        return render(request, 'design.html', context=context)

    return render(request, 'design.html', {})
