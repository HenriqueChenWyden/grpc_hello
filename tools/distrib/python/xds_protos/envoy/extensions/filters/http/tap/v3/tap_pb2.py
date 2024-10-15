# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/tap/v3/tap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.extensions.common.tap.v3 import common_pb2 as envoy_dot_extensions_dot_common_dot_tap_dot_v3_dot_common__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.envoy/extensions/filters/http/tap/v3/tap.proto\x12$envoy.extensions.filters.http.tap.v3\x1a+envoy/extensions/common/tap/v3/common.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xda\x01\n\x03Tap\x12V\n\rcommon_config\x18\x01 \x01(\x0b\x32\x35.envoy.extensions.common.tap.v3.CommonExtensionConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12$\n\x1crecord_headers_received_time\x18\x02 \x01(\x08\x12$\n\x1crecord_downstream_connection\x18\x03 \x01(\x08:/\x9a\xc5\x88\x1e*\n(envoy.config.filter.http.tap.v2alpha.TapB\x9b\x01\n2io.envoyproxy.envoy.extensions.filters.http.tap.v3B\x08TapProtoP\x01ZQgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/tap/v3;tapv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.filters.http.tap.v3.tap_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n2io.envoyproxy.envoy.extensions.filters.http.tap.v3B\010TapProtoP\001ZQgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/tap/v3;tapv3\272\200\310\321\006\002\020\002'
  _TAP.fields_by_name['common_config']._options = None
  _TAP.fields_by_name['common_config']._serialized_options = b'\372B\005\212\001\002\020\001'
  _TAP._options = None
  _TAP._serialized_options = b'\232\305\210\036*\n(envoy.config.filter.http.tap.v2alpha.Tap'
  _globals['_TAP']._serialized_start=225
  _globals['_TAP']._serialized_end=443
# @@protoc_insertion_point(module_scope)
