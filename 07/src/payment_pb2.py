# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: payment.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'payment.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpayment.proto\x12\x07payment\x1a\x1bgoogle/protobuf/empty.proto\"M\n\x07Payment\x12\x18\n\x10\x63reditCardNumber\x18\x01 \x01(\t\x12\x17\n\x0f\x63reditCardOwner\x18\x02 \x01(\t\x12\x0f\n\x07orderId\x18\x03 \x01(\t\"1\n\x0bPaymentList\x12\"\n\x08payments\x18\x01 \x03(\x0b\x32\x10.payment.Payment\"T\n\x0ePaymentRequest\x12\x18\n\x10\x63reditCardNumber\x18\x01 \x01(\t\x12\x17\n\x0f\x63reditCardOwner\x18\x02 \x01(\t\x12\x0f\n\x07orderId\x18\x03 \x01(\t\"!\n\x0fPaymentResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\x8f\x01\n\x0ePaymentService\x12<\n\x0cListPayments\x12\x16.google.protobuf.Empty\x1a\x14.payment.PaymentList\x12?\n\nAddPayment\x12\x17.payment.PaymentRequest\x1a\x18.payment.PaymentResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PAYMENT']._serialized_start=55
  _globals['_PAYMENT']._serialized_end=132
  _globals['_PAYMENTLIST']._serialized_start=134
  _globals['_PAYMENTLIST']._serialized_end=183
  _globals['_PAYMENTREQUEST']._serialized_start=185
  _globals['_PAYMENTREQUEST']._serialized_end=269
  _globals['_PAYMENTRESPONSE']._serialized_start=271
  _globals['_PAYMENTRESPONSE']._serialized_end=304
  _globals['_PAYMENTSERVICE']._serialized_start=307
  _globals['_PAYMENTSERVICE']._serialized_end=450
# @@protoc_insertion_point(module_scope)