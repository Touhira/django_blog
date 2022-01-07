from django.shortcuts import render
from .form import  FeedBackForm
import telebot

def contact(request):

    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        message = f'{request.POST["name"]}\n' \
                  f'{request.POST["email"]}\n' \
                  f'{request.POST["message"]}'
        try:
            if form.is_valid():
                bot = telebot.TeleBot('5037334587:AAEK5sYnfnNAtJYqHgpWJxzASzbMSjD0Px4')
                bot.send_message(434401197, message)
                form.save()
        except Exception:
             pass

    data = {"title": "Связаться с нами"}
    return render(request,'contact/contact.html', data)

