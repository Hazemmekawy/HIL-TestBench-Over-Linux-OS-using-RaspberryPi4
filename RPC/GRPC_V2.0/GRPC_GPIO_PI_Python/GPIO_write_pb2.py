# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GPIO_write.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GPIO_write.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10GPIO_write.proto\"6\n\x0fModeInputParams\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x11\n\tgpio_mode\x18\x02 \x01(\r\"6\n\x0eSetInputParams\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x12\n\ngpio_level\x18\x02 \x01(\r\"\x1d\n\tPinNumber\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\"$\n\nGPIO_Level\x12\x16\n\x0egpio_pin_level\x18\x01 \x01(\r\".\n\x08GPIO_PUD\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x10\n\x08gpio_pud\x18\x02 \x01(\r\"@\n\nPWM_params\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x0f\n\x07PWMfreq\x18\x02 \x01(\r\x12\x0f\n\x07PWMduty\x18\x03 \x01(\r\" \n\nPWM_Status\x12\x12\n\nPWM_return\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty2\xcd\x01\n\x07PI_GPIO\x12&\n\x08set_mode\x12\x10.ModeInputParams\x1a\x06.Empty\"\x00\x12\"\n\x05write\x12\x0f.SetInputParams\x1a\x06.Empty\"\x00\x12!\n\x04read\x12\n.PinNumber\x1a\x0b.GPIO_Level\"\x00\x12\'\n\x10set_pull_up_down\x12\t.GPIO_PUD\x1a\x06.Empty\"\x00\x12*\n\x0chardware_PWM\x12\x0b.PWM_params\x1a\x0b.PWM_Status\"\x00\x62\x06proto3'
)




_MODEINPUTPARAMS = _descriptor.Descriptor(
  name='ModeInputParams',
  full_name='ModeInputParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpio_pin', full_name='ModeInputParams.gpio_pin', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpio_mode', full_name='ModeInputParams.gpio_mode', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=74,
)


_SETINPUTPARAMS = _descriptor.Descriptor(
  name='SetInputParams',
  full_name='SetInputParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpio_pin', full_name='SetInputParams.gpio_pin', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpio_level', full_name='SetInputParams.gpio_level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=130,
)


_PINNUMBER = _descriptor.Descriptor(
  name='PinNumber',
  full_name='PinNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpio_pin', full_name='PinNumber.gpio_pin', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=161,
)


_GPIO_LEVEL = _descriptor.Descriptor(
  name='GPIO_Level',
  full_name='GPIO_Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpio_pin_level', full_name='GPIO_Level.gpio_pin_level', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=199,
)


_GPIO_PUD = _descriptor.Descriptor(
  name='GPIO_PUD',
  full_name='GPIO_PUD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpio_pin', full_name='GPIO_PUD.gpio_pin', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpio_pud', full_name='GPIO_PUD.gpio_pud', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=247,
)


_PWM_PARAMS = _descriptor.Descriptor(
  name='PWM_params',
  full_name='PWM_params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpio_pin', full_name='PWM_params.gpio_pin', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PWMfreq', full_name='PWM_params.PWMfreq', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PWMduty', full_name='PWM_params.PWMduty', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=313,
)


_PWM_STATUS = _descriptor.Descriptor(
  name='PWM_Status',
  full_name='PWM_Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PWM_return', full_name='PWM_Status.PWM_return', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=347,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=356,
)

DESCRIPTOR.message_types_by_name['ModeInputParams'] = _MODEINPUTPARAMS
DESCRIPTOR.message_types_by_name['SetInputParams'] = _SETINPUTPARAMS
DESCRIPTOR.message_types_by_name['PinNumber'] = _PINNUMBER
DESCRIPTOR.message_types_by_name['GPIO_Level'] = _GPIO_LEVEL
DESCRIPTOR.message_types_by_name['GPIO_PUD'] = _GPIO_PUD
DESCRIPTOR.message_types_by_name['PWM_params'] = _PWM_PARAMS
DESCRIPTOR.message_types_by_name['PWM_Status'] = _PWM_STATUS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModeInputParams = _reflection.GeneratedProtocolMessageType('ModeInputParams', (_message.Message,), {
  'DESCRIPTOR' : _MODEINPUTPARAMS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:ModeInputParams)
  })
_sym_db.RegisterMessage(ModeInputParams)

SetInputParams = _reflection.GeneratedProtocolMessageType('SetInputParams', (_message.Message,), {
  'DESCRIPTOR' : _SETINPUTPARAMS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:SetInputParams)
  })
_sym_db.RegisterMessage(SetInputParams)

PinNumber = _reflection.GeneratedProtocolMessageType('PinNumber', (_message.Message,), {
  'DESCRIPTOR' : _PINNUMBER,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:PinNumber)
  })
_sym_db.RegisterMessage(PinNumber)

GPIO_Level = _reflection.GeneratedProtocolMessageType('GPIO_Level', (_message.Message,), {
  'DESCRIPTOR' : _GPIO_LEVEL,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:GPIO_Level)
  })
_sym_db.RegisterMessage(GPIO_Level)

GPIO_PUD = _reflection.GeneratedProtocolMessageType('GPIO_PUD', (_message.Message,), {
  'DESCRIPTOR' : _GPIO_PUD,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:GPIO_PUD)
  })
_sym_db.RegisterMessage(GPIO_PUD)

PWM_params = _reflection.GeneratedProtocolMessageType('PWM_params', (_message.Message,), {
  'DESCRIPTOR' : _PWM_PARAMS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:PWM_params)
  })
_sym_db.RegisterMessage(PWM_params)

PWM_Status = _reflection.GeneratedProtocolMessageType('PWM_Status', (_message.Message,), {
  'DESCRIPTOR' : _PWM_STATUS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:PWM_Status)
  })
_sym_db.RegisterMessage(PWM_Status)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_PI_GPIO = _descriptor.ServiceDescriptor(
  name='PI_GPIO',
  full_name='PI_GPIO',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=359,
  serialized_end=564,
  methods=[
  _descriptor.MethodDescriptor(
    name='set_mode',
    full_name='PI_GPIO.set_mode',
    index=0,
    containing_service=None,
    input_type=_MODEINPUTPARAMS,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='write',
    full_name='PI_GPIO.write',
    index=1,
    containing_service=None,
    input_type=_SETINPUTPARAMS,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='read',
    full_name='PI_GPIO.read',
    index=2,
    containing_service=None,
    input_type=_PINNUMBER,
    output_type=_GPIO_LEVEL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='set_pull_up_down',
    full_name='PI_GPIO.set_pull_up_down',
    index=3,
    containing_service=None,
    input_type=_GPIO_PUD,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='hardware_PWM',
    full_name='PI_GPIO.hardware_PWM',
    index=4,
    containing_service=None,
    input_type=_PWM_PARAMS,
    output_type=_PWM_STATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PI_GPIO)

DESCRIPTOR.services_by_name['PI_GPIO'] = _PI_GPIO

# @@protoc_insertion_point(module_scope)
