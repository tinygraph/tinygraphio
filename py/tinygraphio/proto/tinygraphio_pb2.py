# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinygraphio.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tinygraphio.proto\x12\x0etinygraphio.v1\"/\n\nFileHeader\x12\x0f\n\x07version\x18\x01 \x02(\x06\x12\x10\n\x08\x63hecksum\x18\x02 \x02(\x06\"+\n\x0bGraphHeader\x12\r\n\x05nodes\x18\x01 \x02(\x06\x12\r\n\x05\x65\x64ges\x18\x02 \x02(\x06\"6\n\nGraphChunk\x12\x13\n\x07offsets\x18\x01 \x03(\x04\x42\x02\x10\x01\x12\x13\n\x07targets\x18\x02 \x03(\x04\x42\x02\x10\x01\x42\x02H\x03')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinygraphio_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _GRAPHCHUNK.fields_by_name['offsets']._options = None
  _GRAPHCHUNK.fields_by_name['offsets']._serialized_options = b'\020\001'
  _GRAPHCHUNK.fields_by_name['targets']._options = None
  _GRAPHCHUNK.fields_by_name['targets']._serialized_options = b'\020\001'
  _FILEHEADER._serialized_start=37
  _FILEHEADER._serialized_end=84
  _GRAPHHEADER._serialized_start=86
  _GRAPHHEADER._serialized_end=129
  _GRAPHCHUNK._serialized_start=131
  _GRAPHCHUNK._serialized_end=185
# @@protoc_insertion_point(module_scope)