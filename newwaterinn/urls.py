"""newwaterinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from devices import views
from devices.views import (
    all_ampv1ListAPIView,
    all_ampv2ListAPIView,
    all_ampv3ListAPIView,
    all_ampv4ListAPIView,
    all_ampv5ListAPIView,
    all_atmListAPIView,
    all_cnd_consenListAPIView,
    all_tds_consenListAPIView,
    all_hppListAPIView,
    all_F_flowsenListAPIView,
    all_P_flowsenListAPIView,
    all_rwpListAPIView,
    all_panelListAPIView,
    all_tap1ListAPIView,
    all_tap2ListAPIView,
    all_tap3ListAPIView,
    all_tap4ListAPIView,
    all_flowsen1ListAPIView,
    all_flowsen2ListAPIView,
    all_flowsen3ListAPIView,
    all_flowsen4ListAPIView,
    all_tdsListAPIView,
    all_cndListAPIView,
    LastRecordsView,
    
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('a',views.Treat_cnd),
    path('',views.testo),
    path('topicapi/',include('devices.urls')),
    path('topicapi/all_ampv1/', all_ampv1ListAPIView.as_view(), name='all-ampv1'),
    path('topicapi/all_ampv2/', all_ampv2ListAPIView.as_view(), name='all_ampv2'),
    path('topicapi/all_ampv3/', all_ampv3ListAPIView.as_view(), name='all-ampv3'),
    path('topicapi/all_ampv4/', all_ampv4ListAPIView.as_view(), name='all-ampv4'),
    path('topicapi/all_ampv5/', all_ampv5ListAPIView.as_view(), name='all-ampv5'),
    path('topicapi/all_rwp/', all_rwpListAPIView.as_view(), name='all-rwp'),
    path('topicapi/all_hpp/', all_hppListAPIView.as_view(), name='all-hpp'),
    path('topicapi/all_tap1/', all_tap1ListAPIView.as_view(), name='all-tap1'),
    path('topicapi/all_tap2/', all_tap2ListAPIView.as_view(), name='all-tap2'),
    path('topicapi/all_tap3/', all_tap3ListAPIView.as_view(), name='all-tap3'),
    path('topicapi/all_tap4/', all_tap4ListAPIView.as_view(), name='all-tap4'),
    path('topicapi/all_cnd/', all_cndListAPIView.as_view(), name='all-cnd'),
    path('topicapi/all_tds/', all_tdsListAPIView.as_view(), name='all-tds'),
    path('topicapi/all_F_flowsen/', all_F_flowsenListAPIView.as_view(), name='all-F_flowsen'),
    path('topicapi/all_P_flowsen/', all_P_flowsenListAPIView.as_view(), name='all-P_flowsen'),
    path('topicapi/all_cnd_consen/', all_cnd_consenListAPIView.as_view(), name='all-cnd_consen'),
    path('topicapi/all_tds_consen/', all_tds_consenListAPIView.as_view(), name='all-tds_consen'),
    path('topicapi/all_panel/', all_panelListAPIView.as_view(), name='all-panel'),
    path('topicapi/all_atm/', all_atmListAPIView.as_view(), name='all-atm'),
    path('topicapi/all_flowsen1/', all_flowsen1ListAPIView.as_view(), name='all-flowsen1'),
    path('topicapi/all_flowsen2/', all_flowsen2ListAPIView.as_view(), name='all-flowsen2'),
    path('topicapi/all_flowsen3/', all_flowsen3ListAPIView.as_view(), name='all-flowsen3'),
    path('topicapi/all_flowsen4/', all_flowsen4ListAPIView.as_view(), name='all-flowsen4'),
    path('api/last-records/', LastRecordsView.as_view()),

    # path('',include('devices.routing')),
    # path('c',views.on_message)
]
