from django.shortcuts import render

from my_secrets import API_KEY
from .models import Chat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai


def chat(request):
    chats = Chat.objects.all()
    # render takes 3 arguments: request, template, context
    return render(request, 'chat.html', {
        'chats': chats,
    })


@csrf_exempt
def ajax(request):
    # check whether the request is ajax
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # text in the input field and send it to the API
        text = request.POST.get('text')
        print(text)

        openai.api_key = API_KEY
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{text}"}
            ]
        )

        # get response from API and display it
        response = res.choices[0].message["content"]
        print(response)

        chat = Chat.objects.create(
            text=text,
            gpt=response
        )

        return JsonResponse({'data': response})
    return JsonResponse({})
