from django.shortcuts import render, redirect
from .forms import messageForm
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        form = messageForm()
        context = {
            'form':form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form =  messageForm(request.POST)

        if form.is_valid():
            messages.success(request, f"Message received {form.cleaned_data['name']}. I'll get back to you in a short while." )

            
            contact = form.save()

            return redirect('resume:resume')
        else:
            messages.error(request, "Error. Message not sent.")
            return redirect('resume:resume')

