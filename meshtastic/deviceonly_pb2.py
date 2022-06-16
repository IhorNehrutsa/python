# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deviceonly.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2
from . import mesh_pb2 as mesh__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deviceonly.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\nDeviceOnlyH\003Z!github.com/meshtastic/gomeshproto',
  serialized_pb=b'\n\x10\x64\x65viceonly.proto\x1a\rchannel.proto\x1a\nmesh.proto\"\xe6\x01\n\x0b\x44\x65viceState\x12\x1c\n\x07my_node\x18\x02 \x01(\x0b\x32\x0b.MyNodeInfo\x12\x14\n\x05owner\x18\x03 \x01(\x0b\x32\x05.User\x12\x1a\n\x07node_db\x18\x04 \x03(\x0b\x32\t.NodeInfo\x12\"\n\rreceive_queue\x18\x05 \x03(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07version\x18\x08 \x01(\r\x12$\n\x0frx_text_message\x18\x07 \x01(\x0b\x32\x0b.MeshPacket\x12\x0f\n\x07no_save\x18\t \x01(\x08\x12\x15\n\rdid_gps_reset\x18\x0b \x01(\x08J\x04\x08\x0c\x10\r\":\n\x0b\x43hannelFile\x12\x1a\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x08.Channel\x12\x0f\n\x07version\x18\x02 \x01(\r\"\x84\x01\n\x08OEMStore\x12\x16\n\x0eoem_icon_width\x18\x01 \x01(\r\x12\x17\n\x0foem_icon_height\x18\x02 \x01(\r\x12\x15\n\roem_icon_bits\x18\x03 \x01(\x0c\x12\x1e\n\x08oem_font\x18\x04 \x01(\x0e\x32\x0c.ScreenFonts\x12\x10\n\x08oem_text\x18\x05 \x01(\t*>\n\x0bScreenFonts\x12\x0e\n\nFONT_SMALL\x10\x00\x12\x0f\n\x0b\x46ONT_MEDIUM\x10\x01\x12\x0e\n\nFONT_LARGE\x10\x02\x42\x46\n\x13\x63om.geeksville.meshB\nDeviceOnlyH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
  ,
  dependencies=[channel__pb2.DESCRIPTOR,mesh__pb2.DESCRIPTOR,])

_SCREENFONTS = _descriptor.EnumDescriptor(
  name='ScreenFonts',
  full_name='ScreenFonts',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FONT_SMALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FONT_MEDIUM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FONT_LARGE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=475,
  serialized_end=537,
)
_sym_db.RegisterEnumDescriptor(_SCREENFONTS)

ScreenFonts = enum_type_wrapper.EnumTypeWrapper(_SCREENFONTS)
FONT_SMALL = 0
FONT_MEDIUM = 1
FONT_LARGE = 2



_DEVICESTATE = _descriptor.Descriptor(
  name='DeviceState',
  full_name='DeviceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='my_node', full_name='DeviceState.my_node', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='DeviceState.owner', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_db', full_name='DeviceState.node_db', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receive_queue', full_name='DeviceState.receive_queue', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='DeviceState.version', index=4,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_text_message', full_name='DeviceState.rx_text_message', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_save', full_name='DeviceState.no_save', index=6,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='did_gps_reset', full_name='DeviceState.did_gps_reset', index=7,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=48,
  serialized_end=278,
)


_CHANNELFILE = _descriptor.Descriptor(
  name='ChannelFile',
  full_name='ChannelFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='ChannelFile.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='ChannelFile.version', index=1,
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
  serialized_start=280,
  serialized_end=338,
)


_OEMSTORE = _descriptor.Descriptor(
  name='OEMStore',
  full_name='OEMStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='oem_icon_width', full_name='OEMStore.oem_icon_width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oem_icon_height', full_name='OEMStore.oem_icon_height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oem_icon_bits', full_name='OEMStore.oem_icon_bits', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oem_font', full_name='OEMStore.oem_font', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oem_text', full_name='OEMStore.oem_text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=341,
  serialized_end=473,
)

_DEVICESTATE.fields_by_name['my_node'].message_type = mesh__pb2._MYNODEINFO
_DEVICESTATE.fields_by_name['owner'].message_type = mesh__pb2._USER
_DEVICESTATE.fields_by_name['node_db'].message_type = mesh__pb2._NODEINFO
_DEVICESTATE.fields_by_name['receive_queue'].message_type = mesh__pb2._MESHPACKET
_DEVICESTATE.fields_by_name['rx_text_message'].message_type = mesh__pb2._MESHPACKET
_CHANNELFILE.fields_by_name['channels'].message_type = channel__pb2._CHANNEL
_OEMSTORE.fields_by_name['oem_font'].enum_type = _SCREENFONTS
DESCRIPTOR.message_types_by_name['DeviceState'] = _DEVICESTATE
DESCRIPTOR.message_types_by_name['ChannelFile'] = _CHANNELFILE
DESCRIPTOR.message_types_by_name['OEMStore'] = _OEMSTORE
DESCRIPTOR.enum_types_by_name['ScreenFonts'] = _SCREENFONTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

ChannelFile = _reflection.GeneratedProtocolMessageType('ChannelFile', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELFILE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:ChannelFile)
  })
_sym_db.RegisterMessage(ChannelFile)

OEMStore = _reflection.GeneratedProtocolMessageType('OEMStore', (_message.Message,), {
  'DESCRIPTOR' : _OEMSTORE,
  '__module__' : 'deviceonly_pb2'
  # @@protoc_insertion_point(class_scope:OEMStore)
  })
_sym_db.RegisterMessage(OEMStore)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
