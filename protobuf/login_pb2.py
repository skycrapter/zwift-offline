# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import per_session_info_pb2 as per__session__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blogin.proto\x1a\x16per-session-info.proto\"s\n\rLoginResponse\x12\x15\n\rsession_state\x18\x01 \x02(\t\x12\x1d\n\x04info\x18\x02 \x02(\x0b\x32\x0f.PerSessionInfo\x12\x18\n\x10relay_session_id\x18\x03 \x01(\r\x12\x12\n\nexpiration\x18\x04 \x01(\r\"J\n\x0cLoginRequest\x12-\n\nproperties\x18\x01 \x02(\x0b\x32\x19.AnalyticsEventProperties\x12\x0b\n\x03key\x18\x02 \x02(\x0c\"0\n\x16\x41nalyticsEventProperty\x12\n\n\x02\x66\x31\x18\x01 \x02(\t\x12\n\n\x02\x66\x32\x18\x02 \x02(\t\"E\n\x18\x41nalyticsEventProperties\x12)\n\x08property\x18\x02 \x03(\x0b\x32\x17.AnalyticsEventProperty\"K\n\x1bRelaySessionRefreshResponse\x12\x18\n\x10relay_session_id\x18\x01 \x02(\r\x12\x12\n\nexpiration\x18\x02 \x02(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'login_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINRESPONSE._serialized_start=39
  _LOGINRESPONSE._serialized_end=154
  _LOGINREQUEST._serialized_start=156
  _LOGINREQUEST._serialized_end=230
  _ANALYTICSEVENTPROPERTY._serialized_start=232
  _ANALYTICSEVENTPROPERTY._serialized_end=280
  _ANALYTICSEVENTPROPERTIES._serialized_start=282
  _ANALYTICSEVENTPROPERTIES._serialized_end=351
  _RELAYSESSIONREFRESHRESPONSE._serialized_start=353
  _RELAYSESSIONREFRESHRESPONSE._serialized_end=428
# @@protoc_insertion_point(module_scope)
