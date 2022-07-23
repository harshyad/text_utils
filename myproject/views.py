# I have created this file
#  Website code

from string import punctuation
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html',)


def analyze(request):

    # Get the text

    dj_text = request.POST.get('text', 'default')
    print(dj_text)

    removepunc = request.POST.get('removepunc', 'off')
    print(removepunc)

    UpperCase = request.POST.get('UpperCase', 'off')
    print(UpperCase)

    LowerCase = request.POST.get('LowerCase', 'off')
    print(LowerCase)

    CTFLetter = request.POST.get('CapitilizeTheFirstLetter', 'off')
    print(CTFLetter)

    ExtraSpaceremover = request.POST.get('ExtraSpaceremover', 'off')
    print(ExtraSpaceremover)

    CharCount = request.POST.get('CharCount', 'off')
    print(CharCount)

    # analyze the text

    analyzed = ""

    # removing the punctuation

    if removepunc == "on":
        punct = string.punctuation
        for char in dj_text:
            if char not in punct:
                analyzed = analyzed+char
            dj_text = analyzed

    # Converting to uppercase

    if UpperCase == "on":
        analyzed = dj_text.upper()

    # Converting to lowercase

    if LowerCase == "on":
        analyzed = dj_text.lower()

    # Captilizing the first letter

    if CTFLetter == "on":
        analyzed = dj_text.capitalize()

    # Removing the extra space

    if ExtraSpaceremover == "on":
        analyzed = " ".join(dj_text.split())

    i = len(analyzed)
    j = 0
    # Checking if the char_count was on or not and returning according to that

    if(CharCount == "on"):
        params = {'analyzed_text': analyzed, 'Char_count': i}
        return render(request, 'analyze.html', params)
    else:
        params = {'analyzed_text': analyzed, 'Char_count': j}
        return render(request, 'analyze.html', params)
