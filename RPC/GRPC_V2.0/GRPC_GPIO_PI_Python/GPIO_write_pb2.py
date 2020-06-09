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
  serialized_pb=b'\n\x10GPIO_write.proto\"6\n\x0fModeInputParams\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x11\n\tgpio_mode\x18\x02 \x01(\r\"6\n\x0eSetInputParams\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x12\n\ngpio_level\x18\x02 \x01(\r\"\x1d\n\tPinNumber\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\"$\n\nGPIO_Level\x12\x16\n\x0egpio_pin_level\x18\x01 \x01(\r\".\n\x08GPIO_PUD\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x10\n\x08gpio_pud\x18\x02 \x01(\r\"@\n\nPWM_params\x12\x10\n\x08gpio_pin\x18\x01 \x01(\r\x12\x0f\n\x07PWMfreq\x18\x02 \x01(\r\x12\x0f\n\x07PWMduty\x18\x03 \x01(\r\" \n\nPWM_Status\x12\x12\n\nPWM_return\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\"@\n\x10SerialOpenParams\x12\x0b\n\x03tty\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61ud\x18\x02 \x01(\x05\x12\x11\n\tser_flags\x18\x03 \x01(\x05\"+\n\x13SerialHandleMessage\x12\x14\n\x0cSerialHandle\x18\x01 \x01(\x05\"\x1e\n\nSerialByte\x12\x10\n\x08ReadByte\x18\x01 \x01(\x05\"9\n\x15SerialWriteByteParams\x12\x0e\n\x06handle\x18\x01 \x01(\x05\x12\x10\n\x08\x62yte_val\x18\x02 \x01(\x05\"1\n\x11SerialWriteParams\x12\x0e\n\x06handle\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"#\n\rNumberofBytes\x12\x12\n\nNumofBytes\x18\x01 \x01(\x05\x32\xb0\x04\n\x07PI_GPIO\x12&\n\x08set_mode\x12\x10.ModeInputParams\x1a\x06.Empty\"\x00\x12\"\n\x05write\x12\x0f.SetInputParams\x1a\x06.Empty\"\x00\x12!\n\x04read\x12\n.PinNumber\x1a\x0b.GPIO_Level\"\x00\x12\'\n\x10set_pull_up_down\x12\t.GPIO_PUD\x1a\x06.Empty\"\x00\x12*\n\x0chardware_PWM\x12\x0b.PWM_params\x1a\x0b.PWM_Status\"\x00\x12\x38\n\x0bserial_open\x12\x11.SerialOpenParams\x1a\x14.SerialHandleMessage\"\x00\x12.\n\x0cserial_close\x12\x14.SerialHandleMessage\x1a\x06.Empty\"\x00\x12\x37\n\x10serial_read_byte\x12\x14.SerialHandleMessage\x1a\x0b.SerialByte\"\x00\x12\x35\n\x11serial_write_byte\x12\x16.SerialWriteByteParams\x1a\x06.Empty\"\x00\x12,\n\x0cserial_write\x12\x12.SerialWriteParams\x1a\x06.Empty\"\x00\x12?\n\x15serial_data_available\x12\x14.SerialHandleMessage\x1a\x0e.NumberofBytes\"\x00\x12\x18\n\x04stop\x12\x06.Empty\x1a\x06.Empty\"\x00\x62\x06proto3'
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


_SERIALOPENPARAMS = _descriptor.Descriptor(
  name='SerialOpenParams',
  full_name='SerialOpenParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tty', full_name='SerialOpenParams.tty', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baud', full_name='SerialOpenParams.baud', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ser_flags', full_name='SerialOpenParams.ser_flags', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=358,
  serialized_end=422,
)


_SERIALHANDLEMESSAGE = _descriptor.Descriptor(
  name='SerialHandleMessage',
  full_name='SerialHandleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SerialHandle', full_name='SerialHandleMessage.SerialHandle', index=0,
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
  serialized_start=424,
  serialized_end=467,
)


_SERIALBYTE = _descriptor.Descriptor(
  name='SerialByte',
  full_name='SerialByte',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ReadByte', full_name='SerialByte.ReadByte', index=0,
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
  serialized_start=469,
  serialized_end=499,
)


_SERIALWRITEBYTEPARAMS = _descriptor.Descriptor(
  name='SerialWriteByteParams',
  full_name='SerialWriteByteParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='SerialWriteByteParams.handle', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='byte_val', full_name='SerialWriteByteParams.byte_val', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=501,
  serialized_end=558,
)


_SERIALWRITEPARAMS = _descriptor.Descriptor(
  name='SerialWriteParams',
  full_name='SerialWriteParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='SerialWriteParams.handle', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='SerialWriteParams.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=560,
  serialized_end=609,
)


_NUMBEROFBYTES = _descriptor.Descriptor(
  name='NumberofBytes',
  full_name='NumberofBytes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NumofBytes', full_name='NumberofBytes.NumofBytes', index=0,
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
  serialized_start=611,
  serialized_end=646,
)

DESCRIPTOR.message_types_by_name['ModeInputParams'] = _MODEINPUTPARAMS
DESCRIPTOR.message_types_by_name['SetInputParams'] = _SETINPUTPARAMS
DESCRIPTOR.message_types_by_name['PinNumber'] = _PINNUMBER
DESCRIPTOR.message_types_by_name['GPIO_Level'] = _GPIO_LEVEL
DESCRIPTOR.message_types_by_name['GPIO_PUD'] = _GPIO_PUD
DESCRIPTOR.message_types_by_name['PWM_params'] = _PWM_PARAMS
DESCRIPTOR.message_types_by_name['PWM_Status'] = _PWM_STATUS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['SerialOpenParams'] = _SERIALOPENPARAMS
DESCRIPTOR.message_types_by_name['SerialHandleMessage'] = _SERIALHANDLEMESSAGE
DESCRIPTOR.message_types_by_name['SerialByte'] = _SERIALBYTE
DESCRIPTOR.message_types_by_name['SerialWriteByteParams'] = _SERIALWRITEBYTEPARAMS
DESCRIPTOR.message_types_by_name['SerialWriteParams'] = _SERIALWRITEPARAMS
DESCRIPTOR.message_types_by_name['NumberofBytes'] = _NUMBEROFBYTES
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

SerialOpenParams = _reflection.GeneratedProtocolMessageType('SerialOpenParams', (_message.Message,), {
  'DESCRIPTOR' : _SERIALOPENPARAMS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:SerialOpenParams)
  })
_sym_db.RegisterMessage(SerialOpenParams)

SerialHandleMessage = _reflection.GeneratedProtocolMessageType('SerialHandleMessage', (_message.Message,), {
  'DESCRIPTOR' : _SERIALHANDLEMESSAGE,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:SerialHandleMessage)
  })
_sym_db.RegisterMessage(SerialHandleMessage)

SerialByte = _reflection.GeneratedProtocolMessageType('SerialByte', (_message.Message,), {
  'DESCRIPTOR' : _SERIALBYTE,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:SerialByte)
  })
_sym_db.RegisterMessage(SerialByte)

SerialWriteByteParams = _reflection.GeneratedProtocolMessageType('SerialWriteByteParams', (_message.Message,), {
  'DESCRIPTOR' : _SERIALWRITEBYTEPARAMS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:SerialWriteByteParams)
  })
_sym_db.RegisterMessage(SerialWriteByteParams)

SerialWriteParams = _reflection.GeneratedProtocolMessageType('SerialWriteParams', (_message.Message,), {
  'DESCRIPTOR' : _SERIALWRITEPARAMS,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:SerialWriteParams)
  })
_sym_db.RegisterMessage(SerialWriteParams)

NumberofBytes = _reflection.GeneratedProtocolMessageType('NumberofBytes', (_message.Message,), {
  'DESCRIPTOR' : _NUMBEROFBYTES,
  '__module__' : 'GPIO_write_pb2'
  # @@protoc_insertion_point(class_scope:NumberofBytes)
  })
_sym_db.RegisterMessage(NumberofBytes)



_PI_GPIO = _descriptor.ServiceDescriptor(
  name='PI_GPIO',
  full_name='PI_GPIO',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=649,
  serialized_end=1209,
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
  _descriptor.MethodDescriptor(
    name='serial_open',
    full_name='PI_GPIO.serial_open',
    index=5,
    containing_service=None,
    input_type=_SERIALOPENPARAMS,
    output_type=_SERIALHANDLEMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='serial_close',
    full_name='PI_GPIO.serial_close',
    index=6,
    containing_service=None,
    input_type=_SERIALHANDLEMESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='serial_read_byte',
    full_name='PI_GPIO.serial_read_byte',
    index=7,
    containing_service=None,
    input_type=_SERIALHANDLEMESSAGE,
    output_type=_SERIALBYTE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='serial_write_byte',
    full_name='PI_GPIO.serial_write_byte',
    index=8,
    containing_service=None,
    input_type=_SERIALWRITEBYTEPARAMS,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='serial_write',
    full_name='PI_GPIO.serial_write',
    index=9,
    containing_service=None,
    input_type=_SERIALWRITEPARAMS,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='serial_data_available',
    full_name='PI_GPIO.serial_data_available',
    index=10,
    containing_service=None,
    input_type=_SERIALHANDLEMESSAGE,
    output_type=_NUMBEROFBYTES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stop',
    full_name='PI_GPIO.stop',
    index=11,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PI_GPIO)

DESCRIPTOR.services_by_name['PI_GPIO'] = _PI_GPIO

# @@protoc_insertion_point(module_scope)
