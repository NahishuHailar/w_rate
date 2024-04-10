from django.shortcuts import render


def index(request):


    context = {
        'title': 'Rate me - Главная',
        'content': "Rate me - Workers",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Сервис для оценки профессиональных навыков мастеров своего дела." \
                        "Персональная отвественность - персональная выгода"

    }

    return render(request, 'main/about.html', context)