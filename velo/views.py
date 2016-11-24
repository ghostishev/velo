import os
import datetime
from django.shortcuts import render_to_response, render
from django.http import JsonResponse
from velo.models import *
from velo.serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from velokrua.settings import NEWS_ON_PAGE, NAVFILES_LOC
from collections import OrderedDict
from rest_framework import viewsets


# def home(request, page=None):
#     if page is None:
#         page = 1
#     elif page.isdigit():
#         page = int(page)
#     news = News.objects.all()
#     paginator = Paginator(news, NEWS_ON_PAGE)
#
#     try:
#         current_page = paginator.page(page)
#         news = current_page.object_list
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         current_page = paginator.page(page)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         current_page = paginator.page(paginator.num_pages)
#
#     navigation = {
#         'has_previous': current_page.has_previous(),
#         'has_next': current_page.has_next(),
#     }
#     if navigation['has_previous']:
#         navigation['previous_page'] = current_page.previous_page_number()
#     if navigation['has_next']:
#         navigation['next_page'] = current_page.next_page_number()
#
#     news = NewsSerializer(data=news[0])
#
#     context = {
#         # 'request': request,
#            'page_title': u'Кіровоградський велоклуб "Там Де Ми"',
#            'news': NewsSerializer(news).data,
#            'navigation': navigation
#            }
#
#     news.is_valid()
#
#     return JsonResponse({'news': news.data})

    # return render_to_response('velo/home.html', context)


def app(request):
    return render_to_response('app.html')


class ApiNews(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def online_map(request):
    return render_to_response('velo/map.html', {'request': request, 'page_title': u'Карта'})


def nav(request):
    download_count = {}
    file_list = Navfiles.objects.all()

    for f in file_list:
        download_count[f.filename] = f.count

    def hrs(num):
        """
        request size in bytes, return human redable size
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    filelist = {'garmin': [], 'navitel': []}
    navfiles = os.listdir(NAVFILES_LOC)

    navitel = OrderedDict({
        'Navitel-UA-KRIMEA.nm2.zip': 'АР Крим',
        'Navitel-UA-VN.nm2.zip': 'Вінницька область',
        'Navitel-UA-LUTSK.nm2.zip': 'Волинська область',
        'Navitel-UA-DP.nm2.zip': 'Дніпропетровська область',
        'Navitel-UA-DN.nm2.zip': 'Донецька область',
        'Navitel-UA-ZT.nm2.zip': 'Житомирська область',
        'Navitel-UA-UZ.nm2.zip': 'Закарпатська область',
        'Navitel-UA-ZP.nm2.zip': 'Запорізька область',
        'Navitel-UA-IF.nm2.zip': 'Івано-Франківська область',
        'Navitel-UA-KIEV.nm2.zip': 'Київ та Київська область',
        'Navitel-UA-KR.nm2.zip': 'Кіровоградська область',
        'Navitel-UA-LG.nm2.zip': 'Луганська область',
        'Navitel-UA-LVIV.nm2.zip': 'Львівська область',
        'Navitel-UA-MK.nm2.zip': 'Миколаївська область',
        'Navitel-UA-OD.nm2.zip': 'Одеська область',
        'Navitel-UA-PL.nm2.zip': 'Полтавська область',
        'Navitel-UA-RV.nm2.zip': 'Рівненська область',
        'Navitel-UA-SUMY.nm2.zip': 'Сумська область',
        'Navitel-UA-TE.nm2.zip': 'Тернопільська область',
        'Navitel-UA-KH.nm2.zip': 'Харківська область',
        'Navitel-UA-HS.nm2.zip': 'Херсонська область',
        'Navitel-UA-KM.nm2.zip': 'Хмельницька область',
        'Navitel-UA-CK.nm2.zip': 'Черкаська область',
        'Navitel-UA-CV.nm2.zip': 'Чернівецька область',
        'Navitel-UA-CN.nm2.zip': 'Чернігівська область',
    })

    # Garmin UKR
    if 'gmapsupp.img.zip' in navfiles:
        filelist['garmin'].append({
            'title': 'Вся Україна',
            'filename': 'gmapsupp.img.zip',
            'size': hrs(os.path.getsize(os.path.join(NAVFILES_LOC, 'gmapsupp.img.zip'))),
            'date': datetime.date.fromtimestamp(os.path.getmtime(os.path.join(NAVFILES_LOC, 'gmapsupp.img.zip'))),
            'downloads': download_count['gmapsupp.img.zip'],
        })

    for filename, oblast in navitel.items():
        if filename in navfiles:
            filelist['navitel'].append({
                'title': oblast,
                'filename': filename,
                'size': hrs(os.path.getsize(os.path.join(NAVFILES_LOC, filename))),
                'date': datetime.date.fromtimestamp(os.path.getmtime(os.path.join(NAVFILES_LOC, filename))),
                'downloads': download_count[filename],
            })

    garmin = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(NAVFILES_LOC, 'gmapsupp.img.zip')))
    return render_to_response('velo/nav.html',
                              {'request': request, 'page_title': u'OSM для навігаторів Garmin та Navitel',
                               'navfiles': filelist})


def download(request, filename):
    navfiles = Navfiles.objects.get(filename=filename)
    navfiles.count += 1
    navfiles.save()
    return render_to_response('velo/download.html',
                              {'request': request, 'page_title': u'Завантаження файлу', 'filename': filename})


def trip(request, trip_id=None):
    if trip_id:
        return render_to_response('velo/trip.html',
                                  {'request': request, 'page_title': u'Деталі маршруту',
                                   'id': str(trip_id)})
    else:
        trips = Trips.objects.all()
        return render_to_response('velo/trips.html', {'request': request, 'page_title': u'Маршрути', 'trips': trips})


def calendar(request):
    return render_to_response('velo/calendar.html', {'request': request, 'page_title': u'Календар подій велоклубу'})


def about(request):
    about_content = About.objects.get(pk=1)
    if not about_content:
        about_content = ''
    return render_to_response('velo/about.html',
                              {'request': request, 'page_title': u'Про клуб', 'content': about_content})


def contacts(request):
    contact_list = Contacts.objects.all()
    return render_to_response('velo/contacts.html',
                              {'request': request, 'page_title': u'Контакти', 'contacts': contact_list})


def shops(request):
    shop_list = Shop.objects.all()
    return render_to_response('velo/shops.html',
                              {'request': request, 'page_title': u'Веломайстерні', 'shops': shop_list})
