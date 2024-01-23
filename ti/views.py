from django.shortcuts import render
# from django.http import HttpResponse
import os, requests
from openai import OpenAI
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from ti.models import Image
from django.shortcuts import redirect


load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
# os.environ["OPENAI_API_KEY"] = api_key
# client = OpenAI()
client = OpenAI(
  api_key=os.environ.get("OPENAI_KEY"),
)

# Create your views here.
def renderhome(request):
    obj = None
    if api_key is not None and request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = client.images.generate(
            model="dall-e-2",
            prompt=user_input,
            size="1024x1024",
            quality="hd",
            n=1,
        )
        image_url = response.data[0].url
        response = requests.get(image_url)
        img_file = ContentFile(response.content)

        count = Image.objects.count() + 1
        file_name = f"ai-image-{count}.jpg"

        obj = Image(phrase=user_input)
        obj.ai_image.save(file_name, img_file)
        obj.save()
        # return render(request, "ai-generator.html", {"object": obj})
        return redirect('about', {"object": obj})
    return render(request, "ai-generator.html")


def renderabout(request):
    return render(request, 'about.html')


def renderservices(request):
    return render(request, 'services.html')


def rendercontact(request):
    return render(request, 'contact-us.html')
