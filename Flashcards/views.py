from django.shortcuts import render
from django.http import HttpResponse
from Flashcards.models import FlashCard
# Create your views here.
from django.utils import timezone
from django.shortcuts import redirect
def firstview(request):
    # FlashCard.objects.all().filter(id=2).delete()
    return HttpResponse("My First View from Django!!")


def bulletpoints(request, title):
    flashcard = (FlashCard.objects.all().filter(title = title))[0]
    # print(flashcardid,flashcard.title)
    # print(FlashCard.objects.all())
    bulletpoints = flashcard.bulletpoint_set.all()
    bulletpointlist=[bulletpoint.point for bulletpoint in bulletpoints]
    # output=" -- \n".join(bulletpoints)
    print(bulletpointlist)
    context={
        "bulletpointslist": bulletpointlist,
        "flashcard": flashcard.title
    }
    return render(request, "readflashcard.html", context)


def flashcards(request):
    flashcards=FlashCard.objects.all()
    context={"flashcards": flashcards}
    return render(request, "displayflashcards.html",context)


def createflashcardform(request):
    return render(request, "createflashcard.html")


def createflashcard(request):
    # if request.method == 'POST':
        if FlashCard.createflashcard(request.POST['title'],request.POST['addedby'], timezone.now(), request.POST['description']):
             return HttpResponse("Created your new flashcard")
        else:
            return ("something wrong happended")


def editFlashcard(request, title):
    print("I am Here")
    f = FlashCard.objects.all().filter(title = title)
    f[0].addbulletpoint(request.POST['bulletpoint'])
    # return HttpResponse("Added new bulletpoint to flashcard {} :: {}".format(title,request.POST['bulletpoint']))
    return redirect('../../../flashcards/flashcards/')