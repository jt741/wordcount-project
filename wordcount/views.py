from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request): #request object
    return render(request, 'home.html', {'hithere': 'im hereee'})

def eggs(request):
    return HttpResponse('eggs')

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()

    singledict = {}
    for word in wordlist:
        if word not in singledict:
            singledict[word] = 1
        else:
            singledict[word] += 1
    
    #sorteddict = sorted(singledict.items(), key=lambda x:x[1], reverse=True) #i prefer this method! using lambda
    sorteddict = sorted(singledict.items(), key=operator.itemgetter(1), reverse=True) #this is a cool way of sorting the list, although u do need to import the operator thing which is less cool


    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'dict': sorteddict})
    
    # worddict = {}
    # for word in wordlist:
    #     if word in worddict:
    #         worddict[word]+=1
    #     else:
    #         worddict[word] = 1
    # return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'dict': worddict.items()})

def about(request):
    return render(request, 'about.html')