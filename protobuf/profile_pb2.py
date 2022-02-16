# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprofile.proto\"\x1e\n\x10\x41\x63hievementEntry\x12\n\n\x02id\x18\x01 \x02(\x05\"7\n\x0c\x41\x63hievements\x12\'\n\x0c\x61\x63hievements\x18\x01 \x03(\x0b\x32\x11.AchievementEntry\"\xc2\x1f\n\x07Profile\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08world_id\x18\x02 \x01(\x03\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\x12\x0f\n\x07is_male\x18\x06 \x01(\x08\x12\n\n\x02\x66\x37\x18\x07 \x01(\t\x12\x17\n\x0fweight_in_grams\x18\t \x01(\r\x12\x0b\n\x03\x66tp\x18\n \x01(\r\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\r\x12\x11\n\tbody_type\x18\x0c \x01(\r\x12\x11\n\thair_type\x18\r \x01(\r\x12\x18\n\x10\x66\x61\x63ial_hair_type\x18\x0e \x01(\r\x12\x18\n\x10ride_helmet_type\x18\x0f \x01(\r\x12\x14\n\x0cglasses_type\x18\x10 \x01(\r\x12\x17\n\x0fride_shoes_type\x18\x11 \x01(\r\x12\x17\n\x0fride_socks_type\x18\x12 \x01(\r\x12\x13\n\x0bride_gloves\x18\x13 \x01(\r\x12\x13\n\x0bride_jersey\x18\x14 \x01(\x07\x12\x0b\n\x03\x66\x32\x31\x18\x15 \x01(\x07\x12\x18\n\x10\x62ike_wheel_front\x18\x16 \x01(\x07\x12\x17\n\x0f\x62ike_wheel_rear\x18\x17 \x01(\x07\x12\x12\n\nbike_frame\x18\x18 \x01(\x07\x12\x0b\n\x03\x66\x32\x35\x18\x19 \x01(\x07\x12\x0b\n\x03\x66\x32\x36\x18\x1a \x01(\x07\x12\x19\n\x11\x62ike_frame_colour\x18\x1b \x01(\x06\x12\x0b\n\x03\x66\x32\x38\x18\x1c \x01(\x06\x12\x0b\n\x03\x66\x32\x39\x18\x1d \x01(\x06\x12\x0b\n\x03\x66\x33\x30\x18\x1e \x01(\x06\x12\x0b\n\x03\x66\x33\x31\x18\x1f \x01(\x06\x12\x0b\n\x03\x66\x33\x32\x18  \x01(\x06\x12\x12\n\nsaved_game\x18! \x01(\x0c\x12\x14\n\x0c\x63ountry_code\x18\" \x01(\r\x12 \n\x18total_distance_in_meters\x18# \x01(\r\x12 \n\x18\x65levation_gain_in_meters\x18$ \x01(\r\x12\x1e\n\x16time_ridden_in_minutes\x18% \x01(\r\x12\x1b\n\x13total_in_kom_jersey\x18& \x01(\r\x12!\n\x19total_in_sprinters_jersey\x18\' \x01(\r\x12\x1e\n\x16total_in_orange_jersey\x18( \x01(\r\x12\x18\n\x10total_watt_hours\x18) \x01(\r\x12\x1d\n\x15height_in_millimeters\x18* \x01(\r\x12\x0b\n\x03\x64ob\x18+ \x01(\t\x12\x16\n\x0emax_heart_rate\x18, \x01(\r\x12\x1b\n\x13\x63onnected_to_strava\x18- \x01(\x08\x12\x10\n\x08total_xp\x18. \x01(\r\x12\x18\n\x10total_gold_drops\x18/ \x01(\r\x12(\n\x0bplayer_type\x18\x30 \x01(\x0e\x32\x13.Profile.PlayerType\x12\x19\n\x11\x61\x63hievement_level\x18\x31 \x01(\r\x12\x12\n\nuse_metric\x18\x32 \x01(\x08\x12\x0b\n\x03\x66\x35\x31\x18\x33 \x01(\x08\x12\x1a\n\x12power_source_model\x18\x34 \x01(\r\x12\x0b\n\x03\x66\x35\x33\x18\x35 \x01(\r\x12\x0b\n\x03\x66\x35\x34\x18\x36 \x01(\r\x12\x0b\n\x03\x61ge\x18\x37 \x01(\r\x12\x0b\n\x03\x66\x35\x36\x18\x38 \x01(\x07\x12\x0b\n\x03\x66\x35\x37\x18\x39 \x01(\r\x12\x18\n\x10large_avatar_url\x18: \x01(\t\x12\x14\n\x0cprivacy_bits\x18; \x01(\x06\x12)\n\x0c\x65ntitlements\x18< \x03(\x0b\x32\x13.ProfileEntitlement\x12*\n\x0csocial_facts\x18= \x01(\x0b\x32\x14.Profile.SocialFacts\x12$\n\rfollow_status\x18> \x01(\x0e\x32\r.FollowStatus\x12#\n\x1b\x63onnected_to_training_peaks\x18? \x01(\x08\x12 \n\x18\x63onnected_to_todays_plan\x18@ \x01(\x08\x12\x32\n\x10\x65nrolled_program\x18\x41 \x01(\x0e\x32\x18.Profile.EnrolledProgram\x12\x15\n\rtodayplan_url\x18\x42 \x01(\t\x12\x0b\n\x03\x66\x36\x37\x18\x43 \x01(\r\x12\x16\n\x0erun_shirt_type\x18\x44 \x01(\x07\x12\x17\n\x0frun_shorts_type\x18\x45 \x01(\x07\x12\x16\n\x0erun_shoes_type\x18\x46 \x01(\x07\x12\x16\n\x0erun_socks_type\x18G \x01(\x07\x12\x17\n\x0frun_helmet_type\x18H \x01(\x07\x12\x19\n\x11run_arm_accessory\x18I \x01(\x07\x12\x1a\n\x12total_run_distance\x18J \x01(\r\x12#\n\x1btotal_run_experience_points\x18K \x01(\r\x12\x0b\n\x03\x66\x37\x36\x18L \x01(\x07\x12\x0b\n\x03\x66\x37\x37\x18M \x01(\x07\x12\x0b\n\x03\x66\x37\x38\x18N \x01(\x07\x12\x0b\n\x03\x66\x37\x39\x18O \x01(\x07\x12\x0b\n\x03\x66\x38\x30\x18P \x01(\r\x12\x0b\n\x03\x66\x38\x31\x18Q \x01(\r\x12#\n\x0csubscription\x18R \x01(\x0b\x32\r.Subscription\x12\x1d\n\x15mix_panel_distinct_id\x18S \x01(\t\x12\x1d\n\x15run_achievement_level\x18T \x01(\r\x12!\n\x19total_run_time_in_minutes\x18U \x01(\r\x12\x1d\n\x05sport\x18V \x01(\x0e\x32\x0e.Profile.Sport\x12\x0b\n\x03\x66\x38\x37\x18W \x01(\r\x12!\n\x19\x63onnected_to_under_armour\x18X \x01(\x08\x12\x1a\n\x12preferred_language\x18Y \x01(\t\x12\x13\n\x0bhair_colour\x18Z \x01(\r\x12\x1a\n\x12\x66\x61\x63ial_hair_colour\x18[ \x01(\r\x12\x0b\n\x03\x66\x39\x32\x18\\ \x01(\r\x12\x0b\n\x03\x66\x39\x33\x18] \x01(\r\x12\x19\n\x11run_shorts_length\x18^ \x01(\r\x12\x0b\n\x03\x66\x39\x35\x18_ \x01(\r\x12\x18\n\x10run_socks_length\x18` \x01(\r\x12\x0b\n\x03\x66\x39\x37\x18\x61 \x01(\r\x12\x19\n\x11ride_socks_length\x18\x62 \x01(\r\x12\x0b\n\x03\x66\x39\x39\x18\x63 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x30\x18\x64 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x31\x18\x65 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x32\x18\x66 \x01(\r\x12\x0c\n\x04\x66\x31\x30\x33\x18g \x01(\r\x12\x0c\n\x04\x66\x31\x30\x34\x18h \x01(\r\x12\x1d\n\x15\x63onnected_to_withings\x18i \x01(\x08\x12\x1b\n\x13\x63onnected_to_fitbit\x18j \x01(\x08\x12\x1c\n\x14launched_game_client\x18l \x01(\t\x12\x1b\n\x13\x63urrent_activity_id\x18m \x01(\x03\x12\x1b\n\x13\x63onnected_to_garmin\x18n \x01(\x08\x12$\n\treminders\x18o \x03(\x0b\x32\x11.Profile.Reminder\x12\x0c\n\x04\x66\x31\x31\x32\x18p \x01(\x08\x12&\n\x12private_attributes\x18q \x03(\x0b\x32\n.Attribute\x12%\n\x11public_attributes\x18r \x03(\x0b\x32\n.Attribute\x12\x1a\n\x12total_run_calories\x18s \x01(\x05\x12\x0c\n\x04\x66\x31\x31\x36\x18t \x01(\x03\x12\x1f\n\x17run_time_1mi_in_seconds\x18u \x01(\x05\x12\x1f\n\x17run_time_5km_in_seconds\x18v \x01(\x05\x12 \n\x18run_time_10km_in_seconds\x18w \x01(\x05\x12)\n!run_time_half_marathon_in_seconds\x18x \x01(\x05\x12)\n!run_time_full_marathon_in_seconds\x18y \x01(\x05\x12\x0c\n\x04\x66\x31\x32\x32\x18z \x01(\x05\x12:\n\x14\x63ycling_organization\x18{ \x01(\x0e\x32\x1c.Profile.CyclingOrganization\x12\x0c\n\x04\x66\x31\x32\x34\x18| \x01(\t\x12>\n\x18\x64\x65\x66\x61ult_activity_privacy\x18} \x01(\x0e\x32\x1c.Profile.ActivityPrivacyType\x12\x1e\n\x16\x63onnected_to_runtastic\x18~ \x01(\x08\x12)\n\x10property_changes\x18\x7f \x03(\x0b\x32\x0f.PropertyChange\x1a\xa7\x02\n\x0bSocialFacts\x12\x12\n\nprofile_id\x18\x01 \x01(\x03\x12\x17\n\x0f\x66ollowers_count\x18\x02 \x01(\x05\x12\x17\n\x0f\x66ollowees_count\x18\x03 \x01(\x05\x12\x31\n)followees_in_common_with_logged_in_player\x18\x04 \x01(\x05\x12:\n#follower_status_of_logged_in_player\x18\x05 \x01(\x0e\x32\r.FollowStatus\x12:\n#followee_status_of_logged_in_player\x18\x06 \x01(\x0e\x32\r.FollowStatus\x12\'\n\x1fis_favorite_of_logged_in_player\x18\x07 \x01(\x08\x1a\x96\x01\n\x08Reminder\x12\n\n\x02\x66\x31\x18\x01 \x01(\x03\x12\n\n\x02\x66\x32\x18\x02 \x01(\t\x12\n\n\x02\x66\x33\x18\x03 \x01(\x03\x12.\n\x02\x66\x34\x18\x04 \x03(\x0b\x32\".Profile.Reminder.ReminderProperty\x1a\x36\n\x10ReminderProperty\x12\n\n\x02\x66\x31\x18\x01 \x01(\x03\x12\n\n\x02\x66\x32\x18\x02 \x01(\t\x12\n\n\x02\x66\x33\x18\x03 \x01(\t\"\x9f\x01\n\nPlayerType\x12\x0f\n\x0bPLAYERTYPE0\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0f\n\x0bPRO_CYCLIST\x10\x02\x12\x0f\n\x0bZWIFT_STAFF\x10\x03\x12\x0e\n\nAMBASSADOR\x10\x04\x12\x0c\n\x08VERIFIED\x10\x05\x12\x07\n\x03ZED\x10\x06\x12\x07\n\x03ZAC\x10\x07\x12\x12\n\x0ePRO_TRIATHLETE\x10\x08\x12\x0e\n\nPRO_RUNNER\x10\t\"|\n\x0f\x45nrolledProgram\x12\x14\n\x10\x45NROLLEDPROGRAM0\x10\x00\x12\x11\n\rZWIFT_ACADEMY\x10\x01\x12\x14\n\x10\x45NROLLEDPROGRAM2\x10\x02\x12\x14\n\x10\x45NROLLEDPROGRAM3\x10\x03\x12\x14\n\x10\x45NROLLEDPROGRAM4\x10\x04\"E\n\x05Sport\x12\x0b\n\x07\x43YCLING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06ROWING\x10\x02\x12\n\n\x06SPORT3\x10\x03\x12\n\n\x06SPORT4\x10\x04\"w\n\x13\x43yclingOrganization\x12\x16\n\x12NO_CYCLING_LICENSE\x10\x00\x12\x18\n\x14\x43YCLING_SOUTH_AFRICA\x10\x01\x12\x15\n\x11\x43YCLING_AUSTRALIA\x10\x02\x12\x17\n\x13\x43YCLING_NEW_ZEALAND\x10\x03\";\n\x13\x41\x63tivityPrivacyType\x12\n\n\x06PUBLIC\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01\x12\x0b\n\x07\x46RIENDS\x10\x02\"&\n\x08Profiles\x12\x1a\n\x08profiles\x18\x01 \x03(\x0b\x32\x08.Profile\"\xb0\x06\n\x12ProfileEntitlement\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.ProfileEntitlement.EntitlementType\x12\n\n\x02\x66\x32\x18\x02 \x01(\x03\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.ProfileEntitlement.ProfileEntitlementStatus\x12\x0e\n\x06period\x18\x04 \x01(\t\x12\x17\n\x0f\x62\x65gin_time_unix\x18\x05 \x01(\r\x12\x15\n\rend_time_unix\x18\x06 \x01(\r\x12\x12\n\nkilometers\x18\x07 \x01(\r\x12\x1c\n\x14\x62\x65gin_total_distance\x18\x08 \x01(\r\x12\x1a\n\x12\x65nd_total_distance\x18\t \x01(\r\x12\x0e\n\x06source\x18\n \x01(\t\x12.\n\x08platform\x18\x0b \x01(\x0e\x32\x1c.ProfileEntitlement.Platform\x12\x19\n\x11renewal_date_unix\x18\x0c \x01(\r\x12\x18\n\x10new_trial_system\x18\r \x01(\x08\x12/\n\tplatforms\x18\x0e \x03(\x0e\x32\x1c.ProfileEntitlement.Platform\"L\n\x0f\x45ntitlementType\x12\x14\n\x10\x45NTITLEMENTTYPE0\x10\x00\x12\x08\n\x04RIDE\x10\x01\x12\x07\n\x03RUN\x10\x02\x12\x07\n\x03ROW\x10\x03\x12\x07\n\x03USE\x10\x04\"\x91\x01\n\x18ProfileEntitlementStatus\x12\x16\n\x12\x45NTITLEMENTSTATUS0\x10\x00\x12\x0b\n\x07\x45XPIRED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0c\n\x08INACTIVE\x10\x04\x12(\n$APPLIED_AS_SUBSCRIPTION_TRIAL_PERIOD\x10\x05\"\x86\x01\n\x08Platform\x12\x10\n\x0cPLATFORM_OSX\x10\x00\x12\x0f\n\x0bPLATFORM_PC\x10\x01\x12\x10\n\x0cPLATFORM_IOS\x10\x02\x12\x14\n\x10PLATFORM_ANDROID\x10\x03\x12\x11\n\rPLATFORM_TVOS\x10\x04\x12\r\n\tPLATFORM5\x10\x05\x12\r\n\tPLATFORM6\x10\x06\"\xcc\x02\n\x0cSubscription\x12&\n\x07gateway\x18\x01 \x01(\x0e\x32\x15.Subscription.Gateway\x12\x30\n\x06status\x18\x02 \x01(\x0e\x32 .Subscription.SubscriptionStatus\"#\n\x07Gateway\x12\r\n\tBRAINTREE\x10\x00\x12\t\n\x05\x41PPLE\x10\x01\"\xbc\x01\n\x12SubscriptionStatus\x12\x07\n\x03NEW\x10\x00\x12\x0b\n\x07\x45XPIRED\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0c\n\x08PAST_DUE\x10\x04\x12\x0b\n\x07PENDING\x10\x05\x12\x0c\n\x08SUBERROR\x10\x06\x12\x10\n\x0cUNRECOGNIZED\x10\x07\x12\x0b\n\x07UNKNOWN\x10\x08\x12\x1f\n\x1b\x41\x43TIVE_WITH_PAYMENT_FAILURE\x10\t\x12\r\n\tABANDONED\x10\n\"\x96\x01\n\x0ePropertyChange\x12)\n\rproperty_name\x18\x01 \x02(\x0e\x32\x12.PropertyChange.Id\x12\x14\n\x0c\x63hange_count\x18\x02 \x01(\x05\x12\x13\n\x0bmax_changes\x18\x03 \x01(\x05\".\n\x02Id\x12\t\n\x05TYPE0\x10\x00\x12\x11\n\rDATE_OF_BIRTH\x10\x01\x12\n\n\x06GENDER\x10\x02\"X\n\tAttribute\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x14\n\x0cnumber_value\x18\x02 \x01(\x03\x12\x13\n\x0b\x66loat_value\x18\x03 \x01(\x02\x12\x14\n\x0cstring_value\x18\x05 \x01(\t*\x9e\x01\n\x0c\x46ollowStatus\x12\x11\n\rFOLLOWSTATUS0\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12REQUESTS_TO_FOLLOW\x10\x02\x12\x10\n\x0cIS_FOLLOWING\x10\x03\x12\x15\n\x11HAS_BEEN_DECLINED\x10\x07\x12\x0e\n\nIS_BLOCKED\x10\x04\x12\x13\n\x0fNO_RELATIONSHIP\x10\x05\x12\x08\n\x04SELF\x10\x06')

_FOLLOWSTATUS = DESCRIPTOR.enum_types_by_name['FollowStatus']
FollowStatus = enum_type_wrapper.EnumTypeWrapper(_FOLLOWSTATUS)
FOLLOWSTATUS0 = 0
UNKNOWN = 1
REQUESTS_TO_FOLLOW = 2
IS_FOLLOWING = 3
HAS_BEEN_DECLINED = 7
IS_BLOCKED = 4
NO_RELATIONSHIP = 5
SELF = 6


_ACHIEVEMENTENTRY = DESCRIPTOR.message_types_by_name['AchievementEntry']
_ACHIEVEMENTS = DESCRIPTOR.message_types_by_name['Achievements']
_PROFILE = DESCRIPTOR.message_types_by_name['Profile']
_PROFILE_SOCIALFACTS = _PROFILE.nested_types_by_name['SocialFacts']
_PROFILE_REMINDER = _PROFILE.nested_types_by_name['Reminder']
_PROFILE_REMINDER_REMINDERPROPERTY = _PROFILE_REMINDER.nested_types_by_name['ReminderProperty']
_PROFILES = DESCRIPTOR.message_types_by_name['Profiles']
_PROFILEENTITLEMENT = DESCRIPTOR.message_types_by_name['ProfileEntitlement']
_SUBSCRIPTION = DESCRIPTOR.message_types_by_name['Subscription']
_PROPERTYCHANGE = DESCRIPTOR.message_types_by_name['PropertyChange']
_ATTRIBUTE = DESCRIPTOR.message_types_by_name['Attribute']
_PROFILE_PLAYERTYPE = _PROFILE.enum_types_by_name['PlayerType']
_PROFILE_ENROLLEDPROGRAM = _PROFILE.enum_types_by_name['EnrolledProgram']
_PROFILE_SPORT = _PROFILE.enum_types_by_name['Sport']
_PROFILE_CYCLINGORGANIZATION = _PROFILE.enum_types_by_name['CyclingOrganization']
_PROFILE_ACTIVITYPRIVACYTYPE = _PROFILE.enum_types_by_name['ActivityPrivacyType']
_PROFILEENTITLEMENT_ENTITLEMENTTYPE = _PROFILEENTITLEMENT.enum_types_by_name['EntitlementType']
_PROFILEENTITLEMENT_PROFILEENTITLEMENTSTATUS = _PROFILEENTITLEMENT.enum_types_by_name['ProfileEntitlementStatus']
_PROFILEENTITLEMENT_PLATFORM = _PROFILEENTITLEMENT.enum_types_by_name['Platform']
_SUBSCRIPTION_GATEWAY = _SUBSCRIPTION.enum_types_by_name['Gateway']
_SUBSCRIPTION_SUBSCRIPTIONSTATUS = _SUBSCRIPTION.enum_types_by_name['SubscriptionStatus']
_PROPERTYCHANGE_ID = _PROPERTYCHANGE.enum_types_by_name['Id']
AchievementEntry = _reflection.GeneratedProtocolMessageType('AchievementEntry', (_message.Message,), {
  'DESCRIPTOR' : _ACHIEVEMENTENTRY,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:AchievementEntry)
  })
_sym_db.RegisterMessage(AchievementEntry)

Achievements = _reflection.GeneratedProtocolMessageType('Achievements', (_message.Message,), {
  'DESCRIPTOR' : _ACHIEVEMENTS,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:Achievements)
  })
_sym_db.RegisterMessage(Achievements)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {

  'SocialFacts' : _reflection.GeneratedProtocolMessageType('SocialFacts', (_message.Message,), {
    'DESCRIPTOR' : _PROFILE_SOCIALFACTS,
    '__module__' : 'profile_pb2'
    # @@protoc_insertion_point(class_scope:Profile.SocialFacts)
    })
  ,

  'Reminder' : _reflection.GeneratedProtocolMessageType('Reminder', (_message.Message,), {

    'ReminderProperty' : _reflection.GeneratedProtocolMessageType('ReminderProperty', (_message.Message,), {
      'DESCRIPTOR' : _PROFILE_REMINDER_REMINDERPROPERTY,
      '__module__' : 'profile_pb2'
      # @@protoc_insertion_point(class_scope:Profile.Reminder.ReminderProperty)
      })
    ,
    'DESCRIPTOR' : _PROFILE_REMINDER,
    '__module__' : 'profile_pb2'
    # @@protoc_insertion_point(class_scope:Profile.Reminder)
    })
  ,
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:Profile)
  })
_sym_db.RegisterMessage(Profile)
_sym_db.RegisterMessage(Profile.SocialFacts)
_sym_db.RegisterMessage(Profile.Reminder)
_sym_db.RegisterMessage(Profile.Reminder.ReminderProperty)

Profiles = _reflection.GeneratedProtocolMessageType('Profiles', (_message.Message,), {
  'DESCRIPTOR' : _PROFILES,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:Profiles)
  })
_sym_db.RegisterMessage(Profiles)

ProfileEntitlement = _reflection.GeneratedProtocolMessageType('ProfileEntitlement', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEENTITLEMENT,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:ProfileEntitlement)
  })
_sym_db.RegisterMessage(ProfileEntitlement)

Subscription = _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTION,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:Subscription)
  })
_sym_db.RegisterMessage(Subscription)

PropertyChange = _reflection.GeneratedProtocolMessageType('PropertyChange', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYCHANGE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:PropertyChange)
  })
_sym_db.RegisterMessage(PropertyChange)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
  'DESCRIPTOR' : _ATTRIBUTE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:Attribute)
  })
_sym_db.RegisterMessage(Attribute)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FOLLOWSTATUS._serialized_start=5581
  _FOLLOWSTATUS._serialized_end=5739
  _ACHIEVEMENTENTRY._serialized_start=17
  _ACHIEVEMENTENTRY._serialized_end=47
  _ACHIEVEMENTS._serialized_start=49
  _ACHIEVEMENTS._serialized_end=104
  _PROFILE._serialized_start=107
  _PROFILE._serialized_end=4141
  _PROFILE_SOCIALFACTS._serialized_start=3152
  _PROFILE_SOCIALFACTS._serialized_end=3447
  _PROFILE_REMINDER._serialized_start=3450
  _PROFILE_REMINDER._serialized_end=3600
  _PROFILE_REMINDER_REMINDERPROPERTY._serialized_start=3546
  _PROFILE_REMINDER_REMINDERPROPERTY._serialized_end=3600
  _PROFILE_PLAYERTYPE._serialized_start=3603
  _PROFILE_PLAYERTYPE._serialized_end=3762
  _PROFILE_ENROLLEDPROGRAM._serialized_start=3764
  _PROFILE_ENROLLEDPROGRAM._serialized_end=3888
  _PROFILE_SPORT._serialized_start=3890
  _PROFILE_SPORT._serialized_end=3959
  _PROFILE_CYCLINGORGANIZATION._serialized_start=3961
  _PROFILE_CYCLINGORGANIZATION._serialized_end=4080
  _PROFILE_ACTIVITYPRIVACYTYPE._serialized_start=4082
  _PROFILE_ACTIVITYPRIVACYTYPE._serialized_end=4141
  _PROFILES._serialized_start=4143
  _PROFILES._serialized_end=4181
  _PROFILEENTITLEMENT._serialized_start=4184
  _PROFILEENTITLEMENT._serialized_end=5000
  _PROFILEENTITLEMENT_ENTITLEMENTTYPE._serialized_start=4639
  _PROFILEENTITLEMENT_ENTITLEMENTTYPE._serialized_end=4715
  _PROFILEENTITLEMENT_PROFILEENTITLEMENTSTATUS._serialized_start=4718
  _PROFILEENTITLEMENT_PROFILEENTITLEMENTSTATUS._serialized_end=4863
  _PROFILEENTITLEMENT_PLATFORM._serialized_start=4866
  _PROFILEENTITLEMENT_PLATFORM._serialized_end=5000
  _SUBSCRIPTION._serialized_start=5003
  _SUBSCRIPTION._serialized_end=5335
  _SUBSCRIPTION_GATEWAY._serialized_start=5109
  _SUBSCRIPTION_GATEWAY._serialized_end=5144
  _SUBSCRIPTION_SUBSCRIPTIONSTATUS._serialized_start=5147
  _SUBSCRIPTION_SUBSCRIPTIONSTATUS._serialized_end=5335
  _PROPERTYCHANGE._serialized_start=5338
  _PROPERTYCHANGE._serialized_end=5488
  _PROPERTYCHANGE_ID._serialized_start=5442
  _PROPERTYCHANGE_ID._serialized_end=5488
  _ATTRIBUTE._serialized_start=5490
  _ATTRIBUTE._serialized_end=5578
# @@protoc_insertion_point(module_scope)
