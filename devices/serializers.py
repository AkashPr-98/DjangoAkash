# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import *

# # Create a model serializer
# class GeeksSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = GeeksModel
# 		fields = ('Topic',)


# class TopicSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = MyObject
# 		fields = ('__all__')
# class DeviceSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 			model = Decice_details
# 			fields = ('__all__')


# class NewDeviceSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = NewDecice_details
# 		fields = ('__all__')

class TopicSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = topics
		fields=('__all__')




# # Create a model serializer
# class GeeksSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = GeeksModel
# 		fields = ('Topic',)



class TopicSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = topics
		fields=('__all__')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = device_info
		fields='__all__'

class KeySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = key_info
		fields='__all__'

class cnd_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_repo_yearly
		fields='__all__'

class cnd_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_repo_hourly
		fields='__all__'

class cnd_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_repo_monthly
		fields='__all__'

class cnd_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_repo_daily
		fields='__all__'

class tds_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_repo_yearly
		fields='__all__'

class tds_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_repo_hourly
		fields='__all__'

class tds_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_repo_monthly
		fields='__all__'

class tds_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_repo_daily
		fields='__all__'


class rwp_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = rwp_repo_daily
		fields='__all__'

class rwp_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = rwp_repo_hourly
		fields='__all__'

class rwp_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = rwp_repo_monthly
		fields='__all__'

class rwp_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = rwp_repo_yearly
		fields='__all__'


class hpp_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_repo_daily
		fields='__all__'

class hpp_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_repo_hourly
		fields='__all__'

class hpp_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_repo_monthly
		fields='__all__'

class hpp_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_repo_yearly
		fields='__all__'

class panel_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = panel_repo_daily
		fields='__all__'

class panel_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = panel_repo_hourly
		fields='__all__'

class panel_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = panel_repo_monthly
		fields='__all__'

class panel_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = panel_repo_yearly
		fields='__all__'


class F_flowsen_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = F_flowsen_repo_daily
		fields='__all__'
class P_flowsen_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = P_flowsen_repo_daily
		fields='__all__'

class F_flowsen_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = F_flowsen_repo_hourly
		fields='__all__'
class P_flowsen_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = P_flowsen_repo_hourly
		fields='__all__'

class F_flowsen_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = F_flowsen_repo_monthly
		fields='__all__'
class P_flowsen_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = P_flowsen_repo_monthly
		fields='__all__'

class F_flowsen_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = F_flowsen_repo_yearly
		fields='__all__'

class P_flowsen_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = P_flowsen_repo_yearly
		fields='__all__'



class ampv1_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_repo_daily
		fields='__all__'

class ampv1_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_repo_hourly
		fields='__all__'

class ampv1_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_repo_monthly
		fields='__all__'

class ampv1_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_repo_yearly
		fields='__all__'
class ampv2_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_repo_daily
		fields='__all__'

class ampv2_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_repo_hourly
		fields='__all__'

class ampv2_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_repo_monthly
		fields='__all__'

class ampv2_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_repo_yearly
		fields='__all__'
class ampv3_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv3_repo_daily
		fields='__all__'

class ampv3_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv3_repo_hourly
		fields='__all__'

class ampv3_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv3_repo_monthly
		fields='__all__'

class ampv3_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv3_repo_yearly
		fields='__all__'
class ampv4_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv4_repo_daily
		fields='__all__'

class ampv4_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv4_repo_hourly
		fields='__all__'

class ampv4_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv4_repo_monthly
		fields='__all__'

class ampv4_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv4_repo_yearly
		fields='__all__'
class ampv5_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv5_repo_daily
		fields='__all__'

class ampv5_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv5_repo_hourly
		fields='__all__'

class ampv5_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv5_repo_monthly
		fields='__all__'

class ampv5_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv5_repo_yearly
		fields='__all__'

class tap1_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap1_repo_daily
		fields='__all__'

class tap1_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap1_repo_hourly
		fields='__all__'

class tap1_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap1_repo_monthly
		fields='__all__'

class tap1_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap1_repo_yearly
		fields='__all__'
class tap2_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap2_repo_daily
		fields='__all__'

class tap2_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap2_repo_hourly
		fields='__all__'

class tap2_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap2_repo_monthly
		fields='__all__'

class tap2_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap2_repo_yearly
		fields='__all__'
class tap3_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap3_repo_daily
		fields='__all__'

class tap3_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap3_repo_hourly
		fields='__all__'

class tap3_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap3_repo_monthly
		fields='__all__'

class tap3_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap3_repo_yearly
		fields='__all__'
class tap4_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap4_repo_daily
		fields='__all__'

class tap4_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap4_repo_hourly
		fields='__all__'

class tap4_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap4_repo_monthly
		fields='__all__'

class tap4_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap4_repo_yearly
		fields='__all__'

class tds_consen_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_consen_repo_daily
		fields='__all__'
class cnd_consen_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_consen_repo_daily
		fields='__all__'
class cnd_consen_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_consen_repo_hourly
		fields='__all__'
class tds_consen_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_consen_repo_hourly
		fields='__all__'

class cnd_consen_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_consen_repo_monthly
		fields='__all__'
class tds_consen_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_consen_repo_monthly
		fields='__all__'

class cnd_consen_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_consen_repo_yearly
		fields='__all__'
class tds_consen_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_consen_repo_yearly
		fields='__all__'

class atm_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = atm_repo_daily
		fields='__all__'
class atm_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = atm_repo_hourly
		fields='__all__'

class atm_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = atm_repo_monthly
		fields='__all__'

class atm_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = atm_repo_yearly
		fields='__all__'



class GraphSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = graph_info
		fields='__all__'

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = device_info
		fields='__all__'

class KeySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = key_info
		fields='__all__'


class rwpsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = rwp_setting
		fields='__all__'
	# 	print("hi am from serilization")
	# 	fields=['olc','drc','spn','unit_type','company_name','componant_name']

	# 	def get_author_serializer(self):
	# 		# here write the logic to compute the value based on object
	# 		print("hi ok satish 1")
	# 		return 1

	# 	def get_publisher_serializer(self):
	# 		# here write the logic to compute the value based on object
	# 		print("hi ok satish 1")
	# 		return 2
	# rss=Meta()
	# rss.get_author_serializer()
	# rss.get_publisher_serializer()

class RwpstateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rwp_state
		fields='__all__'
# class rwpsettingSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = rwp_setting
# 		print("hi am from serilization")
# 		fields=['olc','drc','spn','unit_type','company_name','componant_name']


class hppstateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_state
		fields='__all__'
class hppsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_setting
		fields='__all__'

class cndsettingSerializer(serializers.HyperlinkedModelSerializer):
	# new_field = serializers.CharField()
	class Meta:
		model = cnd_setting
		fields='__all__'

class tdssettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_setting
		fields='__all__'
class FflowsensettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = F_flowsen_setting
		fields='__all__'

class PflowsensettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = P_flowsen_setting
		fields='__all__'
class panelsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = panel_setting
		fields='__all__'
class atmsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = atm_setting
		fields='__all__'
class cnd_consensettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_consen_setting
		fields='__all__'
class tds_consensettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_consen_setting
		fields='__all__'
class tap1settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap1_setting
		fields='__all__'
class tap2settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap2_setting
		fields='__all__'
class tap3settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap3_setting
		fields='__all__'
class tap4settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap4_setting
		fields='__all__'
class ampv1stateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_state
		fields='__all__'
class ampv1settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_setting
		fields='__all__'
class ampv2stateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_state
		fields='__all__'
class ampv2settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_setting
		fields='__all__'
class flowsen1_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen1_repo_daily
		fields='_all_'
class flowsen1_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen1_repo_hourly
		fields='_all_'

class flowsen1_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen1_repo_monthly
		fields='_all_'

class flowsen1_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen1_repo_yearly
		fields='_all_'


class flowsen2_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen2_repo_daily
		fields='_all_'
class flowsen2_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen2_repo_hourly
		fields='_all_'

class flowsen2_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen2_repo_monthly
		fields='_all_'

class flowsen2_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen2_repo_yearly
		fields='_all_'


class flowsen3_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen3_repo_daily
		fields='_all_'
class flowsen3_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen3_repo_hourly
		fields='_all_'

class flowsen3_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen3_repo_monthly
		fields='_all_'

class flowsen3_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen3_repo_yearly
		fields='_all_'


class flowsen4_DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen4_repo_daily
		fields='_all_'
class flowsen4_HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen4_repo_hourly
		fields='_all_'

class flowsen4_MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen4_repo_monthly
		fields='_all_'

class flowsen4_YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = flowsen4_repo_yearly
		fields='_all_'
#all data form minit tables used for fornt end

class all_pannelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = treat_panel
		fields = '__all__'
class all_atmSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = disp_atm
		fields = '__all__'