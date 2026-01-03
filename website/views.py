from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsLetterForm
from django.contrib import messages

def index_view(request):
    # return HttpResponse('index_view')
    # return HttpResponse('<h1>Home Page<h1>')
    return render(request, 'website/index.html')

def about_view(request):
    # return HttpResponse('<h1>About Page<h1>')
    return render(request, 'website/about.html')

def contact_view(request):
    # return HttpResponse('<h1>Contact Page<h1>')
    if request.method=='POST':
       form=ContactForm(request.POST)
       if form.is_valid():
           form.save()
           messages.add_message(request,messages.SUCCESS,'Yore Ticket Submit Successfully')
    #        return HttpResponse('done')
       else:
           messages.add_message(request,messages.ERROR,'Yore Ticket didnt Submit')
    #        return HttpResponse('not valid')
    form=ContactForm()
    return render(request, 'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method=='POST':
       form=NewsLetterForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
    else:
        return  HttpResponseRedirect('/')
    

# def test_view(request):
#     # return HttpResponse('<h1>Contact Page<h1>')
#     return render(request, 'website/test.html',{'name':'ali','family':'vahdati'})

# def test_view(request):
#     if request.method=='POST':
#     #     print('post')
#     # elif request.method=='GET':
#     #     print('get')    
#     #  print(request.POST.get('name'))
#        name=request.POST.get('name')
#        email=request.POST.get('email')
#        subject=request.POST.get('subject')
#        messaeg=request.POST.get('message')
#        c=Contact()
#        c.name=name
#        c.email=email
#        c.subject=subject
#        c.messaeg=messaeg
#        c.save()

#     return render(request, 'website/test.html')
# def test_view(request):
#     if request.method=='POST':
#     #    name=request.POST.get('name')
#     #    print(name)
#        form=NameForm(request.POST)
#        if form.is_valid():
#            name=form.cleaned_data['name']
#            email=form.cleaned_data['email']
#            subject=form.cleaned_data['subject']
#            messaeg=form.cleaned_data['messaeg']
#            print(name,email,subject,messaeg)

#            c=Contact()
#            c.name=name
#            c.email=email
#            c.subject=subject
#            c.messaeg=messaeg
#            c.save()
#            return HttpResponse('done')
#        else:
#            return HttpResponse('not valid')
#     form=NameForm()
#     return render(request, 'website/test.html',{'form':form})

def test_view(request):
    if request.method=='POST':
       form=ContactForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse('done')
       else:
           return HttpResponse('not valid')
    form=ContactForm()
    return render(request, 'website/test.html',{'form':form})

def json_test(request):
    return JsonResponse({'name':'ali'})
