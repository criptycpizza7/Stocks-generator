# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stocks.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cstocks.proto\"Y\n\x05stock\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0f\n\x07\x63ompany\x18\x03 \x01(\x05\x12\x16\n\x0e\x63hange_percent\x18\x04 \x01(\x02\x12\n\n\x02id\x18\x05 \x01(\x03\"\x1e\n\x06stocks\x12\x14\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x06.stock\"\x15\n\x06number\x12\x0b\n\x03num\x18\x01 \x01(\x05\x32-\n\x0bsend_stocks\x12\x1e\n\nsendStocks\x12\x07.stocks\x1a\x07.numberb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stocks_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOCK._serialized_start=16
  _STOCK._serialized_end=105
  _STOCKS._serialized_start=107
  _STOCKS._serialized_end=137
  _NUMBER._serialized_start=139
  _NUMBER._serialized_end=160
  _SEND_STOCKS._serialized_start=162
  _SEND_STOCKS._serialized_end=207
# @@protoc_insertion_point(module_scope)
