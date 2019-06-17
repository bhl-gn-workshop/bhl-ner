# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protob.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protob.proto',
  package='protob',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cprotob.proto\x12\x06protob\"\x18\n\x07Version\x12\r\n\x05value\x18\x01 \x01(\t\"\x06\n\x04Void\"C\n\x05Title\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\narchive_id\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04lang\x18\x04 \x01(\t\"\x0b\n\tTitlesOpt\"y\n\x04Page\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x0c\n\x04text\x18\x03 \x01(\x0c\x12\x10\n\x08title_id\x18\x04 \x01(\t\x12\x12\n\ntitle_path\x18\x05 \x01(\t\x12!\n\x05names\x18\x06 \x03(\x0b\x32\x12.protob.NameString\"0\n\x08PagesOpt\x12\x11\n\twith_text\x18\x01 \x01(\x08\x12\x11\n\ttitle_ids\x18\x02 \x03(\x05\"\xda\x01\n\nNameString\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0c\n\x04odds\x18\x02 \x01(\x02\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0f\n\x07\x63urated\x18\x04 \x01(\x08\x12\x15\n\redit_distance\x18\x05 \x01(\x05\x12\x1a\n\x12\x65\x64it_distance_stem\x18\x06 \x01(\x05\x12\x11\n\tsource_id\x18\x07 \x01(\x05\x12 \n\x05match\x18\x08 \x01(\x0e\x32\x11.protob.MatchType\x12\x14\n\x0coffset_start\x18\t \x01(\x05\x12\x12\n\noffset_end\x18\n \x01(\x05*p\n\tMatchType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45XACT\x10\x01\x12\x13\n\x0f\x43\x41NONICAL_EXACT\x10\x02\x12\x13\n\x0f\x43\x41NONICAL_FUZZY\x10\x03\x12\x11\n\rPARTIAL_EXACT\x10\x04\x12\x11\n\rPARTIAL_FUZZY\x10\x05\x32\x8f\x01\n\x08\x42HLIndex\x12&\n\x03Ver\x12\x0c.protob.Void\x1a\x0f.protob.Version\"\x00\x12+\n\x05Pages\x12\x10.protob.PagesOpt\x1a\x0c.protob.Page\"\x00\x30\x01\x12.\n\x06Titles\x12\x11.protob.TitlesOpt\x1a\r.protob.Title\"\x00\x30\x01\x62\x06proto3')
)

_MATCHTYPE = _descriptor.EnumDescriptor(
  name='MatchType',
  full_name='protob.MatchType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXACT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANONICAL_EXACT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANONICAL_FUZZY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTIAL_EXACT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTIAL_FUZZY', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=534,
  serialized_end=646,
)
_sym_db.RegisterEnumDescriptor(_MATCHTYPE)

MatchType = enum_type_wrapper.EnumTypeWrapper(_MATCHTYPE)
NONE = 0
EXACT = 1
CANONICAL_EXACT = 2
CANONICAL_FUZZY = 3
PARTIAL_EXACT = 4
PARTIAL_FUZZY = 5



_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='protob.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='protob.Version.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=24,
  serialized_end=48,
)


_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='protob.Void',
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
  serialized_start=50,
  serialized_end=56,
)


_TITLE = _descriptor.Descriptor(
  name='Title',
  full_name='protob.Title',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protob.Title.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archive_id', full_name='protob.Title.archive_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='protob.Title.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='protob.Title.lang', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=58,
  serialized_end=125,
)


_TITLESOPT = _descriptor.Descriptor(
  name='TitlesOpt',
  full_name='protob.TitlesOpt',
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
  serialized_start=127,
  serialized_end=138,
)


_PAGE = _descriptor.Descriptor(
  name='Page',
  full_name='protob.Page',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protob.Page.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='protob.Page.offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='protob.Page.text', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_id', full_name='protob.Page.title_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_path', full_name='protob.Page.title_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='names', full_name='protob.Page.names', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=140,
  serialized_end=261,
)


_PAGESOPT = _descriptor.Descriptor(
  name='PagesOpt',
  full_name='protob.PagesOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='with_text', full_name='protob.PagesOpt.with_text', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_ids', full_name='protob.PagesOpt.title_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=263,
  serialized_end=311,
)


_NAMESTRING = _descriptor.Descriptor(
  name='NameString',
  full_name='protob.NameString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='protob.NameString.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='odds', full_name='protob.NameString.odds', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='protob.NameString.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curated', full_name='protob.NameString.curated', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edit_distance', full_name='protob.NameString.edit_distance', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edit_distance_stem', full_name='protob.NameString.edit_distance_stem', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_id', full_name='protob.NameString.source_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match', full_name='protob.NameString.match', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset_start', full_name='protob.NameString.offset_start', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset_end', full_name='protob.NameString.offset_end', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=314,
  serialized_end=532,
)

_PAGE.fields_by_name['names'].message_type = _NAMESTRING
_NAMESTRING.fields_by_name['match'].enum_type = _MATCHTYPE
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['Title'] = _TITLE
DESCRIPTOR.message_types_by_name['TitlesOpt'] = _TITLESOPT
DESCRIPTOR.message_types_by_name['Page'] = _PAGE
DESCRIPTOR.message_types_by_name['PagesOpt'] = _PAGESOPT
DESCRIPTOR.message_types_by_name['NameString'] = _NAMESTRING
DESCRIPTOR.enum_types_by_name['MatchType'] = _MATCHTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(
  DESCRIPTOR = _VERSION,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.Version)
  ))
_sym_db.RegisterMessage(Version)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), dict(
  DESCRIPTOR = _VOID,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.Void)
  ))
_sym_db.RegisterMessage(Void)

Title = _reflection.GeneratedProtocolMessageType('Title', (_message.Message,), dict(
  DESCRIPTOR = _TITLE,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.Title)
  ))
_sym_db.RegisterMessage(Title)

TitlesOpt = _reflection.GeneratedProtocolMessageType('TitlesOpt', (_message.Message,), dict(
  DESCRIPTOR = _TITLESOPT,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.TitlesOpt)
  ))
_sym_db.RegisterMessage(TitlesOpt)

Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), dict(
  DESCRIPTOR = _PAGE,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.Page)
  ))
_sym_db.RegisterMessage(Page)

PagesOpt = _reflection.GeneratedProtocolMessageType('PagesOpt', (_message.Message,), dict(
  DESCRIPTOR = _PAGESOPT,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.PagesOpt)
  ))
_sym_db.RegisterMessage(PagesOpt)

NameString = _reflection.GeneratedProtocolMessageType('NameString', (_message.Message,), dict(
  DESCRIPTOR = _NAMESTRING,
  __module__ = 'protob_pb2'
  # @@protoc_insertion_point(class_scope:protob.NameString)
  ))
_sym_db.RegisterMessage(NameString)



_BHLINDEX = _descriptor.ServiceDescriptor(
  name='BHLIndex',
  full_name='protob.BHLIndex',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=649,
  serialized_end=792,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ver',
    full_name='protob.BHLIndex.Ver',
    index=0,
    containing_service=None,
    input_type=_VOID,
    output_type=_VERSION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Pages',
    full_name='protob.BHLIndex.Pages',
    index=1,
    containing_service=None,
    input_type=_PAGESOPT,
    output_type=_PAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Titles',
    full_name='protob.BHLIndex.Titles',
    index=2,
    containing_service=None,
    input_type=_TITLESOPT,
    output_type=_TITLE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BHLINDEX)

DESCRIPTOR.services_by_name['BHLIndex'] = _BHLINDEX

# @@protoc_insertion_point(module_scope)