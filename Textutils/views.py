# this file is created by Jibran
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Home</h1> <a href="http://127.0.0.1:8000/about/">about</a><br>
    # <a href="http://127.0.0.1:8000/removepunc/">removing punc</a>''')


def aboutus(request):
    return render(request, 'about us.html')


def contactus(request):
    return render(request, 'contact us.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == 'on':
        # analyzed = djtext
        Punctuation = '''!#$%&'()*+,\"-./:;<=>?@[]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'removing new line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'removing extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error...Please Select an Option and try again")

    return render(request, 'analyze.html', params)
