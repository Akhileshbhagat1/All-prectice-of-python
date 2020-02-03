from django.shortcuts import render
from .models import Board
from django.http import Http404


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

    # boards_names = list()
        # for board in boards:
    #     boards_names.append(board.name)
        # response_html = '<br>'.join(boards_names)
        # return HttpResponse(response_html)


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
    # board = Board.objects.get()
    # return render(request, 'topics.html', {'board': board})


def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})

