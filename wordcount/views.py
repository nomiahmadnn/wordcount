from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def residential(request):
    return render(request, 'residential.html')

def count(request):
    data= request.GET['fulltextarea']
    word_list=data.split()
    len_word=len(word_list)

    worddictionary={}
    for word in data:
        if word in word_list:
            worddictionary[word] = worddictionary[word]+1
        else:
            worddictionary[word]=1
    sorted_list = sorted(worddictionary.items(), key = operator.itemgetter(1))

    return render(request, 'count.html',{'fulltext':data, 'words':len_word, 'worddictionary':sorted_list})

