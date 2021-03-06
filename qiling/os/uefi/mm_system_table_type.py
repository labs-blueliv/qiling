# -*- coding: utf-8 -*-
#
# TARGET arch is: []
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16

# if local wordsize is same as target, keep ctypes pointer function.
# required to access _ctypes
import _ctypes
# Emulate a pointer class using the approriate c_int32/c_int64 type
# The new class should have :
# ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
# but the class should be submitted to a unique instance for each base type
# to that if A == B, POINTER_T(A) == POINTER_T(B)
ctypes._pointer_t_type_cache = {}
def POINTER_T(pointee):
    # a pointer should have the same length as LONG
    fake_ptr_base_type = ctypes.c_uint64 
    # specific case for c_void_p
    if pointee is None: # VOID pointer type. c_void_p.
        pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
        clsname = 'c_void'
    else:
        clsname = pointee.__name__
    if clsname in ctypes._pointer_t_type_cache:
        return ctypes._pointer_t_type_cache[clsname]
    # make template
    _class = type('LP_%d_%s'%(8, clsname), (fake_ptr_base_type,),{}) 
    ctypes._pointer_t_type_cache[clsname] = _class
    return _class



undefined = ctypes.c_ubyte
ImageBaseOffset32 = ctypes.c_uint32
byte = ctypes.c_ubyte
dword = ctypes.c_uint32
longlong = ctypes.c_int64
qword = ctypes.c_uint64
uchar = ctypes.c_ubyte
uint = ctypes.c_uint32
ulonglong = ctypes.c_uint64
undefined1 = ctypes.c_ubyte
undefined2 = ctypes.c_uint16
undefined4 = ctypes.c_uint32
undefined8 = ctypes.c_uint64
ushort = ctypes.c_uint16
word = ctypes.c_uint16
class struct__EFI_MM_SYSTEM_TABLE(ctypes.Structure):
    pass

class struct_GUID(ctypes.Structure):
    pass

class struct__EFI_MM_CPU_IO_PROTOCOL(ctypes.Structure):
    pass

class struct_EFI_MM_IO_ACCESS(ctypes.Structure):
    pass


# values for enumeration 'enum_859'
enum_859__enumvalues = {
    1: 'MM_IO_UINT16',
    2: 'MM_IO_UINT32',
    3: 'MM_IO_UINT64',
    0: 'MM_IO_UINT8',
}
MM_IO_UINT16 = 1
MM_IO_UINT32 = 2
MM_IO_UINT64 = 3
MM_IO_UINT8 = 0
enum_859 = ctypes.c_int # enum
struct_EFI_MM_IO_ACCESS._pack_ = True # source:False
struct_EFI_MM_IO_ACCESS._functions_ = []
struct_EFI_MM_IO_ACCESS._fields_ = [
    ('Read', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct__EFI_MM_CPU_IO_PROTOCOL), enum_859, ctypes.c_uint64, ctypes.c_uint64, POINTER_T(None)))),
    ('Write', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct__EFI_MM_CPU_IO_PROTOCOL), enum_859, ctypes.c_uint64, ctypes.c_uint64, POINTER_T(None)))),
]

struct_EFI_MM_IO_ACCESS._functions_.append(("Read",['ctypes.c_uint64', 'POINTER_T(struct__EFI_MM_CPU_IO_PROTOCOL)', 'enum_859', 'ctypes.c_uint64', 'ctypes.c_uint64', 'POINTER_T(None)']))
struct_EFI_MM_IO_ACCESS._functions_.append(("Write",['ctypes.c_uint64', 'POINTER_T(struct__EFI_MM_CPU_IO_PROTOCOL)', 'enum_859', 'ctypes.c_uint64', 'ctypes.c_uint64', 'POINTER_T(None)']))
struct__EFI_MM_CPU_IO_PROTOCOL._pack_ = True # source:False
struct__EFI_MM_CPU_IO_PROTOCOL._functions_ = []
struct__EFI_MM_CPU_IO_PROTOCOL._fields_ = [
    ('Mem', struct_EFI_MM_IO_ACCESS),
    ('Io', struct_EFI_MM_IO_ACCESS),
]

EFI_MM_CPU_IO_PROTOCOL = struct__EFI_MM_CPU_IO_PROTOCOL
class struct_EFI_CONFIGURATION_TABLE(ctypes.Structure):
    pass

struct_GUID._pack_ = True # source:False
struct_GUID._functions_ = []
struct_GUID._fields_ = [
    ('Data1', ctypes.c_uint32),
    ('Data2', ctypes.c_uint16),
    ('Data3', ctypes.c_uint16),
    ('Data4', ctypes.c_ubyte * 8),
]

EFI_GUID = struct_GUID
struct_EFI_CONFIGURATION_TABLE._pack_ = True # source:False
struct_EFI_CONFIGURATION_TABLE._functions_ = []
struct_EFI_CONFIGURATION_TABLE._fields_ = [
    ('VendorGuid', EFI_GUID),
    ('VendorTable', POINTER_T(None)),
]


# values for enumeration 'enum_494'
enum_494__enumvalues = {
    2: 'AllocateAddress',
    0: 'AllocateAnyPages',
    1: 'AllocateMaxAddress',
    3: 'MaxAllocateType',
}
AllocateAddress = 2
AllocateAnyPages = 0
AllocateMaxAddress = 1
MaxAllocateType = 3
enum_494 = ctypes.c_int # enum

# values for enumeration 'enum_16'
enum_16__enumvalues = {
    10: 'EfiACPIMemoryNVS',
    9: 'EfiACPIReclaimMemory',
    3: 'EfiBootServicesCode',
    4: 'EfiBootServicesData',
    7: 'EfiConventionalMemory',
    1: 'EfiLoaderCode',
    2: 'EfiLoaderData',
    15: 'EfiMaxMemoryType',
    11: 'EfiMemoryMappedIO',
    12: 'EfiMemoryMappedIOPortSpace',
    13: 'EfiPalCode',
    14: 'EfiPersistentMemory',
    0: 'EfiReservedMemoryType',
    5: 'EfiRuntimeServicesCode',
    6: 'EfiRuntimeServicesData',
    8: 'EfiUnusableMemory',
}
EfiACPIMemoryNVS = 10
EfiACPIReclaimMemory = 9
EfiBootServicesCode = 3
EfiBootServicesData = 4
EfiConventionalMemory = 7
EfiLoaderCode = 1
EfiLoaderData = 2
EfiMaxMemoryType = 15
EfiMemoryMappedIO = 11
EfiMemoryMappedIOPortSpace = 12
EfiPalCode = 13
EfiPersistentMemory = 14
EfiReservedMemoryType = 0
EfiRuntimeServicesCode = 5
EfiRuntimeServicesData = 6
EfiUnusableMemory = 8
enum_16 = ctypes.c_int # enum

# values for enumeration 'enum_498'
enum_498__enumvalues = {
    0: 'EFI_NATIVE_INTERFACE',
}
EFI_NATIVE_INTERFACE = 0
enum_498 = ctypes.c_int # enum

# values for enumeration 'enum_500'
enum_500__enumvalues = {
    0: 'AllHandles',
    2: 'ByProtocol',
    1: 'ByRegisterNotify',
}
AllHandles = 0
ByProtocol = 2
ByRegisterNotify = 1
enum_500 = ctypes.c_int # enum
class struct_EFI_TABLE_HEADER(ctypes.Structure):
    _pack_ = True # source:False
    _functions_ = []
    _fields_ = [
    ('Signature', ctypes.c_uint64),
    ('Revision', ctypes.c_uint32),
    ('HeaderSize', ctypes.c_uint32),
    ('CRC32', ctypes.c_uint32),
    ('Reserved', ctypes.c_uint32),
     ]

struct__EFI_MM_SYSTEM_TABLE._pack_ = True # source:False
struct__EFI_MM_SYSTEM_TABLE._functions_ = []
struct__EFI_MM_SYSTEM_TABLE._fields_ = [
    ('Hdr', struct_EFI_TABLE_HEADER),
    ('MmFirmwareVendor', POINTER_T(ctypes.c_uint16)),
    ('MmFirmwareRevision', ctypes.c_uint32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('MmInstallConfigurationTable', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct__EFI_MM_SYSTEM_TABLE), POINTER_T(struct_GUID), POINTER_T(None), ctypes.c_uint64))),
    ('MmIo', EFI_MM_CPU_IO_PROTOCOL),
    ('MmAllocatePool', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, enum_16, ctypes.c_uint64, POINTER_T(POINTER_T(None))))),
    ('MmFreePool', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None)))),
    ('MmAllocatePages', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, enum_494, enum_16, ctypes.c_uint64, POINTER_T(ctypes.c_uint64)))),
    ('MmFreePages', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64))),
    ('MmStartupThisAp', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None))), ctypes.c_uint64, POINTER_T(None)))),
    ('CurrentlyExecutingCpu', ctypes.c_uint64),
    ('NumberOfCpus', ctypes.c_uint64),
    ('CpuSaveStateSize', POINTER_T(ctypes.c_uint64)),
    ('CpuSaveState', POINTER_T(POINTER_T(None))),
    ('NumberOfTableEntries', ctypes.c_uint64),
    ('MmConfigurationTable', POINTER_T(struct_EFI_CONFIGURATION_TABLE)),
    ('MmInstallProtocolInterface', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(POINTER_T(None)), POINTER_T(struct_GUID), enum_498, POINTER_T(None)))),
    ('MmUninstallProtocolInterface', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(struct_GUID), POINTER_T(None)))),
    ('MmHandleProtocol', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(struct_GUID), POINTER_T(POINTER_T(None))))),
    ('MmRegisterProtocolNotify', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(None))), POINTER_T(POINTER_T(None))))),
    ('MmLocateHandle', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, enum_500, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(ctypes.c_uint64), POINTER_T(POINTER_T(None))))),
    ('MmLocateProtocol', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(POINTER_T(None))))),
    ('MmiManage', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64)))),
    ('MmiHandlerRegister', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64))), POINTER_T(struct_GUID), POINTER_T(POINTER_T(None))))),
    ('MmiHandlerUnRegister', POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None)))),
]

struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmInstallConfigurationTable",['ctypes.c_uint64', 'POINTER_T(struct__EFI_MM_SYSTEM_TABLE)', 'POINTER_T(struct_GUID)', 'POINTER_T(None)', 'ctypes.c_uint64']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmAllocatePool",['ctypes.c_uint64', 'enum_16', 'ctypes.c_uint64', 'POINTER_T(POINTER_T(None))']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmFreePool",['ctypes.c_uint64', 'POINTER_T(None)']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmAllocatePages",['ctypes.c_uint64', 'enum_494', 'enum_16', 'ctypes.c_uint64', 'POINTER_T(ctypes.c_uint64)']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmFreePages",['ctypes.c_uint64', 'ctypes.c_uint64', 'ctypes.c_uint64']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmStartupThisAp",['ctypes.c_uint64', 'POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None)))', 'ctypes.c_uint64', 'POINTER_T(None)']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmInstallProtocolInterface",['ctypes.c_uint64', 'POINTER_T(POINTER_T(None))', 'POINTER_T(struct_GUID)', 'enum_498', 'POINTER_T(None)']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmUninstallProtocolInterface",['ctypes.c_uint64', 'POINTER_T(None)', 'POINTER_T(struct_GUID)', 'POINTER_T(None)']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmHandleProtocol",['ctypes.c_uint64', 'POINTER_T(None)', 'POINTER_T(struct_GUID)', 'POINTER_T(POINTER_T(None))']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmRegisterProtocolNotify",['ctypes.c_uint64', 'POINTER_T(struct_GUID)', 'POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(None)))', 'POINTER_T(POINTER_T(None))']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmLocateHandle",['ctypes.c_uint64', 'enum_500', 'POINTER_T(struct_GUID)', 'POINTER_T(None)', 'POINTER_T(ctypes.c_uint64)', 'POINTER_T(POINTER_T(None))']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmLocateProtocol",['ctypes.c_uint64', 'POINTER_T(struct_GUID)', 'POINTER_T(None)', 'POINTER_T(POINTER_T(None))']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmiManage",['ctypes.c_uint64', 'POINTER_T(struct_GUID)', 'POINTER_T(None)', 'POINTER_T(None)', 'POINTER_T(ctypes.c_uint64)']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmiHandlerRegister",['ctypes.c_uint64', 'POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64)))', 'POINTER_T(struct_GUID)', 'POINTER_T(POINTER_T(None))']))
struct__EFI_MM_SYSTEM_TABLE._functions_.append(("MmiHandlerUnRegister",['ctypes.c_uint64', 'POINTER_T(None)']))
_EFI_MM_SYSTEM_TABLE = struct__EFI_MM_SYSTEM_TABLE
P_EFI_MM_SYSTEM_TABLE = POINTER_T(struct__EFI_MM_SYSTEM_TABLE)
EFI_MM_SYSTEM_TABLE = struct__EFI_MM_SYSTEM_TABLE
EFI_TABLE_HEADER = struct_EFI_TABLE_HEADER
PEFI_TABLE_HEADER = POINTER_T(struct_EFI_TABLE_HEADER)
CHAR16 = ctypes.c_uint16
UINT32 = ctypes.c_uint32
UINT64 = ctypes.c_uint64
UINTN = ctypes.c_uint64
RETURN_STATUS = ctypes.c_uint64
EFI_STATUS = ctypes.c_uint64
GUID = struct_GUID
PGUID = POINTER_T(struct_GUID)
EFI_MM_INSTALL_CONFIGURATION_TABLE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct__EFI_MM_SYSTEM_TABLE), POINTER_T(struct_GUID), POINTER_T(None), ctypes.c_uint64))
_EFI_MM_CPU_IO_PROTOCOL = struct__EFI_MM_CPU_IO_PROTOCOL
P_EFI_MM_CPU_IO_PROTOCOL = POINTER_T(struct__EFI_MM_CPU_IO_PROTOCOL)
EFI_MEMORY_TYPE = enum_16
EFI_MEMORY_TYPE__enumvalues = enum_16__enumvalues
EFI_ALLOCATE_POOL = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, enum_16, ctypes.c_uint64, POINTER_T(POINTER_T(None))))
EFI_FREE_POOL = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None)))
EFI_ALLOCATE_TYPE = enum_494
EFI_ALLOCATE_TYPE__enumvalues = enum_494__enumvalues
EFI_PHYSICAL_ADDRESS = ctypes.c_uint64
EFI_ALLOCATE_PAGES = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, enum_494, enum_16, ctypes.c_uint64, POINTER_T(ctypes.c_uint64)))
EFI_FREE_PAGES = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64))
EFI_AP_PROCEDURE = POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None)))
EFI_MM_STARTUP_THIS_AP = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(ctypes.CFUNCTYPE(None, POINTER_T(None))), ctypes.c_uint64, POINTER_T(None)))
EFI_CONFIGURATION_TABLE = struct_EFI_CONFIGURATION_TABLE
PEFI_CONFIGURATION_TABLE = POINTER_T(struct_EFI_CONFIGURATION_TABLE)
EFI_HANDLE = POINTER_T(None)
EFI_INTERFACE_TYPE = enum_498
EFI_INTERFACE_TYPE__enumvalues = enum_498__enumvalues
EFI_INSTALL_PROTOCOL_INTERFACE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(POINTER_T(None)), POINTER_T(struct_GUID), enum_498, POINTER_T(None)))
EFI_UNINSTALL_PROTOCOL_INTERFACE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(struct_GUID), POINTER_T(None)))
EFI_HANDLE_PROTOCOL = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(struct_GUID), POINTER_T(POINTER_T(None))))
EFI_MM_NOTIFY_FN = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(None)))
EFI_MM_REGISTER_PROTOCOL_NOTIFY = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(None))), POINTER_T(POINTER_T(None))))
EFI_LOCATE_SEARCH_TYPE = enum_500
EFI_LOCATE_SEARCH_TYPE__enumvalues = enum_500__enumvalues
EFI_LOCATE_HANDLE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, enum_500, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(ctypes.c_uint64), POINTER_T(POINTER_T(None))))
EFI_LOCATE_PROTOCOL = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(POINTER_T(None))))
EFI_MM_INTERRUPT_MANAGE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_GUID), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64)))
EFI_MM_HANDLER_ENTRY_POINT = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64)))
EFI_MM_INTERRUPT_REGISTER = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64))), POINTER_T(struct_GUID), POINTER_T(POINTER_T(None))))
EFI_MM_INTERRUPT_UNREGISTER = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None)))
UINT16 = ctypes.c_uint16
UINT8 = ctypes.c_ubyte
EFI_MM_IO_ACCESS = struct_EFI_MM_IO_ACCESS
PEFI_MM_IO_ACCESS = POINTER_T(struct_EFI_MM_IO_ACCESS)
EFI_MM_IO_WIDTH = enum_859
EFI_MM_IO_WIDTH__enumvalues = enum_859__enumvalues
EFI_MM_CPU_IO = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct__EFI_MM_CPU_IO_PROTOCOL), enum_859, ctypes.c_uint64, ctypes.c_uint64, POINTER_T(None)))
__all__ = \
    ['AllHandles', 'AllocateAddress', 'AllocateAnyPages',
    'AllocateMaxAddress', 'ByProtocol', 'ByRegisterNotify', 'CHAR16',
    'EFI_ALLOCATE_PAGES', 'EFI_ALLOCATE_POOL', 'EFI_ALLOCATE_TYPE',
    'EFI_ALLOCATE_TYPE__enumvalues', 'EFI_AP_PROCEDURE',
    'EFI_CONFIGURATION_TABLE', 'EFI_FREE_PAGES', 'EFI_FREE_POOL',
    'EFI_GUID', 'EFI_HANDLE', 'EFI_HANDLE_PROTOCOL',
    'EFI_INSTALL_PROTOCOL_INTERFACE', 'EFI_INTERFACE_TYPE',
    'EFI_INTERFACE_TYPE__enumvalues', 'EFI_LOCATE_HANDLE',
    'EFI_LOCATE_PROTOCOL', 'EFI_LOCATE_SEARCH_TYPE',
    'EFI_LOCATE_SEARCH_TYPE__enumvalues', 'EFI_MEMORY_TYPE',
    'EFI_MEMORY_TYPE__enumvalues', 'EFI_MM_CPU_IO',
    'EFI_MM_CPU_IO_PROTOCOL', 'EFI_MM_HANDLER_ENTRY_POINT',
    'EFI_MM_INSTALL_CONFIGURATION_TABLE', 'EFI_MM_INTERRUPT_MANAGE',
    'EFI_MM_INTERRUPT_REGISTER', 'EFI_MM_INTERRUPT_UNREGISTER',
    'EFI_MM_IO_ACCESS', 'EFI_MM_IO_WIDTH',
    'EFI_MM_IO_WIDTH__enumvalues', 'EFI_MM_NOTIFY_FN',
    'EFI_MM_REGISTER_PROTOCOL_NOTIFY', 'EFI_MM_STARTUP_THIS_AP',
    'EFI_MM_SYSTEM_TABLE', 'EFI_NATIVE_INTERFACE',
    'EFI_PHYSICAL_ADDRESS', 'EFI_STATUS', 'EFI_TABLE_HEADER',
    'EFI_UNINSTALL_PROTOCOL_INTERFACE', 'EfiACPIMemoryNVS',
    'EfiACPIReclaimMemory', 'EfiBootServicesCode',
    'EfiBootServicesData', 'EfiConventionalMemory', 'EfiLoaderCode',
    'EfiLoaderData', 'EfiMaxMemoryType', 'EfiMemoryMappedIO',
    'EfiMemoryMappedIOPortSpace', 'EfiPalCode', 'EfiPersistentMemory',
    'EfiReservedMemoryType', 'EfiRuntimeServicesCode',
    'EfiRuntimeServicesData', 'EfiUnusableMemory', 'GUID',
    'ImageBaseOffset32', 'MM_IO_UINT16', 'MM_IO_UINT32',
    'MM_IO_UINT64', 'MM_IO_UINT8', 'MaxAllocateType',
    'PEFI_CONFIGURATION_TABLE', 'PEFI_MM_IO_ACCESS',
    'PEFI_TABLE_HEADER', 'PGUID', 'P_EFI_MM_CPU_IO_PROTOCOL',
    'P_EFI_MM_SYSTEM_TABLE', 'RETURN_STATUS', 'UINT16', 'UINT32',
    'UINT64', 'UINT8', 'UINTN', '_EFI_MM_CPU_IO_PROTOCOL',
    '_EFI_MM_SYSTEM_TABLE', 'byte', 'dword', 'enum_16', 'enum_494',
    'enum_498', 'enum_500', 'enum_859', 'longlong', 'qword',
    'struct_EFI_CONFIGURATION_TABLE', 'struct_EFI_MM_IO_ACCESS',
    'struct_EFI_TABLE_HEADER', 'struct_GUID',
    'struct__EFI_MM_CPU_IO_PROTOCOL', 'struct__EFI_MM_SYSTEM_TABLE',
    'uchar', 'uint', 'ulonglong', 'undefined', 'undefined1',
    'undefined2', 'undefined4', 'undefined8', 'ushort', 'word']
