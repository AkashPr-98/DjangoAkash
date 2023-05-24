"""waterinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers
from devices.views import MyTokenObtainPairView, MyTokenRefreshView



router = routers.DefaultRouter()
router.register(r'Topic',TopicViewSet)
router.register(r'device_info',DeviceViewset)
router.register(r'key_info',keyViewset)
router.register(r'graph_info',GraphViewset)

router.register(r'Rwp_state',RwpstateViewset)
router.register(r'rwp_setting',rwpsettingViewset)
router.register(r'hpp_state',hppstateViewset)
router.register(r'hpp_setting',hppsettingViewset)
router.register(r'cnd_setting',cndsettingViewset)
router.register(r'tds_setting',tdssettingViewset)
router.register(r'F_flowsen_setting',FflowsensettingViewset)
router.register(r'P_flowsen_setting',PflowsensettingViewset)
router.register(r'panel_setting',panelsettingViewset)
router.register(r'atm_setting',atmsettingViewset)
router.register(r'cnd_consen_setting',cnd_consensettingViewset)
router.register(r'tds_consen_setting',tds_consensettingViewset)
router.register(r'tap1_setting',tap1settingViewset)
router.register(r'tap2_setting',tap2settingViewset)
router.register(r'tap3_setting',tap3settingViewset)
router.register(r'tap4_setting',tap4settingViewset)
router.register(r'ampv1_setting',ampv1settingViewset)
router.register(r'ampv1_state',ampv1stateViewset)
router.register(r'ampv2_setting',ampv2settingViewset)
router.register(r'ampv2_state',ampv2stateViewset)

router.register(r'cnd_tds_hourly',cnd_tds_HourlyViewset)
router.register(r'cnd_tds_daily',cnd_tds_DailyViewset)
router.register(r'cnd_tds_monthly',cnd_tds_MonthlyViewset)
router.register(r'cnd_tds_yearly',cnd_tds_YearlyViewset)
router.register(r'rwp_hourly',rwp_HourlyViewset)
router.register(r'rwp_daily',rwp_DailyViewset)
router.register(r'rwp_monthly',rwp_MonthlyViewset)
router.register(r'rwp_yearly',rwp_YearlyViewset)
router.register(r'hpp_hourly',hpp_HourlyViewset)
router.register(r'hpp_daily',hpp_DailyViewset)
router.register(r'hpp_monthly',hpp_MonthlyViewset)
router.register(r'hpp_yearly',hpp_YearlyViewset)
router.register(r'panel_hourly',panel_HourlyViewset)
router.register(r'panel_daily',panel_DailyViewset)
router.register(r'panel_monthly',panel_MonthlyViewset)
router.register(r'panel_yearly',panel_YearlyViewset)
router.register(r'F_flowsen_hourly',F_flowsen_HourlyViewset)
router.register(r'P_flowsen_hourly',P_flowsen_HourlyViewset)
router.register(r'F_flowsen_daily',F_flowsen_DailyViewset)
router.register(r'P_flowsen_daily',P_flowsen_DailyViewset)
router.register(r'F_flowsen_monthly',F_flowsen_MonthlyViewset)
router.register(r'P_flowsen_monthly',P_flowsen_MonthlyViewset)
router.register(r'F_flowsen_yearly',F_flowsen_YearlyViewset)
router.register(r'P_flowsen_yearly',P_flowsen_YearlyViewset)
router.register(r'ampv1_hourly',ampv1_HourlyViewset)
router.register(r'ampv1_daily',ampv1_DailyViewset)
router.register(r'ampv1_monthly',ampv1_MonthlyViewset)
router.register(r'ampv1_yearly',ampv1_YearlyViewset)
router.register(r'ampv2_hourly',ampv2_HourlyViewset)
router.register(r'ampv2_daily',ampv2_DailyViewset)
router.register(r'ampv2_monthly',ampv2_MonthlyViewset)
router.register(r'ampv2_yearly',ampv2_YearlyViewset)
router.register(r'ampv3_hourly',ampv3_HourlyViewset)
router.register(r'ampv3_daily',ampv3_DailyViewset)
router.register(r'ampv3_monthly',ampv3_MonthlyViewset)
router.register(r'ampv3_yearly',ampv3_YearlyViewset)
router.register(r'ampv4_hourly',ampv4_HourlyViewset)
router.register(r'ampv4_daily',ampv4_DailyViewset)
router.register(r'ampv4_monthly',ampv4_MonthlyViewset)
router.register(r'ampv4_yearly',ampv4_YearlyViewset)
router.register(r'ampv5_hourly',ampv5_HourlyViewset)
router.register(r'ampv5_daily',ampv5_DailyViewset)
router.register(r'ampv5_monthly',ampv5_MonthlyViewset)
router.register(r'ampv5_yearly',ampv5_YearlyViewset)
router.register(r'tap1_hourly',tap1_HourlyViewset)
router.register(r'tap1_daily',tap1_DailyViewset)
router.register(r'tap1_monthly',tap1_MonthlyViewset)
router.register(r'tap1_yearly',tap1_YearlyViewset)
router.register(r'tap2_hourly',tap2_HourlyViewset)
router.register(r'tap2_daily',tap2_DailyViewset)
router.register(r'tap2_monthly',tap2_MonthlyViewset)
router.register(r'tap2_yearly',tap2_YearlyViewset)
router.register(r'tap3_hourly',tap3_HourlyViewset)
router.register(r'tap3_daily',tap3_DailyViewset)
router.register(r'tap3_monthly',tap3_MonthlyViewset)
router.register(r'tap3_yearly',tap3_YearlyViewset)
router.register(r'tap4_hourly',tap4_HourlyViewset)
router.register(r'tap4_daily',tap4_DailyViewset)
router.register(r'tap4_monthly',tap4_MonthlyViewset)
router.register(r'tap4_yearly',tap4_YearlyViewset)
router.register(r'atm_hourly',atm_HourlyViewset)
router.register(r'atm_daily',atm_DailyViewset)
router.register(r'atm_monthly',atm_MonthlyViewset)
router.register(r'atm_yearly',atm_YearlyViewset)
router.register(r'cnd_consen_hourly',cnd_consen_HourlyViewset)
router.register(r'tds_consen_hourly',tds_consen_HourlyViewset)
router.register(r'cnd_consen_daily',cnd_consen_DailyViewset)
router.register(r'tds_consen_daily',tds_consen_DailyViewset)
router.register(r'cnd_consen_monthly',cnd_consen_MonthlyViewset)
router.register(r'tds_consen_monthly',tds_consen_MonthlyViewset)
router.register(r'cnd_consen_yearly',cnd_consen_YearlyViewset)
router.register(r'tds_consen_yearly',tds_consen_YearlyViewset)

router.register(r'updated_treat_cnd_tds_sen',updated_treat_cnd_tds_senViewset,basename='treat_cnd_tds_sen')
router.register(r'updated_treat_rwp',updated_treat_rwpViewset,basename='treat_rwp')
router.register(r'updated_treat_ampv1',updated_treat_ampv1Viewset,basename='treat_ampv1')
router.register(r'updated_treat_ampv2',updated_treat_ampv2Viewset,basename='_treat_ampv2')
router.register(r'updated_treat_hpp',updated_treat_hppViewset,basename='_treat_hpp')
router.register(r'updated_treat_panel',updated_treat_panelViewset,basename='treat_panel')
router.register(r'updated_treat_F_flowsen',updated_treat_F_flowsenViewset,basename='treat_F_flowsen')
router.register(r'updated_treat_P_flowsen',updated_treat_P_flowsenViewset,basename='treat_P_flowsen')
router.register(r'updated_disp_cnd_consen',updated_disp_cnd_consenViewset,basename='disp_cnd_consen')
router.register(r'updated_disp_tds_consen',updated_disp_tds_consenViewset,basename='disp_tds_consen')
router.register(r'updated_disp_tap1',updated_disp_tap1Viewset,basename='disp_tap1')
router.register(r'updated-disp_tap2',updated_disp_tap2Viewset,basename='disp_tap2')
router.register(r'updated_disp_tap3',updated_disp_tap3Viewset,basename='disp_tap3')
router.register(r'updated_disp_tap4',updated_disp_tap4Viewset,basename='disp_tap4')
router.register(r'updated_disp_atm',updated_disp_atmViewset,basename='disp_atm')
router.register(r'get_device_id',getDeviceID,basename='get_device_id')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('c',views.on_message)
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
