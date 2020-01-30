#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class IOType(object):
    FILE = 0
    PROPERTY = 1

    _VALUES_TO_NAMES = {
        0: "FILE",
        1: "PROPERTY",
    }

    _NAMES_TO_VALUES = {
        "FILE": 0,
        "PROPERTY": 1,
    }


class ParserInput(object):
    """
    Attributes:
     - id
     - name
     - requiredInput
     - parserId
     - type
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
        (3, TType.BOOL, 'requiredInput', None, None, ),  # 3
        (4, TType.STRING, 'parserId', 'UTF8', None, ),  # 4
        (5, TType.I32, 'type', None, None, ),  # 5
    )

    def __init__(self, id=None, name=None, requiredInput=None, parserId=None, type=None,):
        self.id = id
        self.name = name
        self.requiredInput = requiredInput
        self.parserId = parserId
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.requiredInput = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.parserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ParserInput')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.requiredInput is not None:
            oprot.writeFieldBegin('requiredInput', TType.BOOL, 3)
            oprot.writeBool(self.requiredInput)
            oprot.writeFieldEnd()
        if self.parserId is not None:
            oprot.writeFieldBegin('parserId', TType.STRING, 4)
            oprot.writeString(self.parserId.encode('utf-8') if sys.version_info[0] == 2 else self.parserId)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 5)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        if self.requiredInput is None:
            raise TProtocolException(message='Required field requiredInput is unset!')
        if self.parserId is None:
            raise TProtocolException(message='Required field parserId is unset!')
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ParserOutput(object):
    """
    Attributes:
     - id
     - name
     - requiredOutput
     - parserId
     - type
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
        (3, TType.BOOL, 'requiredOutput', None, None, ),  # 3
        (4, TType.STRING, 'parserId', 'UTF8', None, ),  # 4
        (5, TType.I32, 'type', None, None, ),  # 5
    )

    def __init__(self, id=None, name=None, requiredOutput=None, parserId=None, type=None,):
        self.id = id
        self.name = name
        self.requiredOutput = requiredOutput
        self.parserId = parserId
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.requiredOutput = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.parserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ParserOutput')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.requiredOutput is not None:
            oprot.writeFieldBegin('requiredOutput', TType.BOOL, 3)
            oprot.writeBool(self.requiredOutput)
            oprot.writeFieldEnd()
        if self.parserId is not None:
            oprot.writeFieldBegin('parserId', TType.STRING, 4)
            oprot.writeString(self.parserId.encode('utf-8') if sys.version_info[0] == 2 else self.parserId)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 5)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        if self.requiredOutput is None:
            raise TProtocolException(message='Required field requiredOutput is unset!')
        if self.parserId is None:
            raise TProtocolException(message='Required field parserId is unset!')
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Parser(object):
    """
    Attributes:
     - id
     - imageName
     - outputDirPath
     - inputDirPath
     - executionCommand
     - inputFiles
     - outputFiles
     - gatewayId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'imageName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'outputDirPath', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'inputDirPath', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'executionCommand', 'UTF8', None, ),  # 5
        (6, TType.LIST, 'inputFiles', (TType.STRUCT, (ParserInput, ParserInput.thrift_spec), False), None, ),  # 6
        (7, TType.LIST, 'outputFiles', (TType.STRUCT, (ParserOutput, ParserOutput.thrift_spec), False), None, ),  # 7
        (8, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 8
    )

    def __init__(self, id=None, imageName=None, outputDirPath=None, inputDirPath=None, executionCommand=None, inputFiles=None, outputFiles=None, gatewayId=None,):
        self.id = id
        self.imageName = imageName
        self.outputDirPath = outputDirPath
        self.inputDirPath = inputDirPath
        self.executionCommand = executionCommand
        self.inputFiles = inputFiles
        self.outputFiles = outputFiles
        self.gatewayId = gatewayId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.imageName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.outputDirPath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.inputDirPath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.executionCommand = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.inputFiles = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = ParserInput()
                        _elem5.read(iprot)
                        self.inputFiles.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.outputFiles = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = ParserOutput()
                        _elem11.read(iprot)
                        self.outputFiles.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Parser')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.imageName is not None:
            oprot.writeFieldBegin('imageName', TType.STRING, 2)
            oprot.writeString(self.imageName.encode('utf-8') if sys.version_info[0] == 2 else self.imageName)
            oprot.writeFieldEnd()
        if self.outputDirPath is not None:
            oprot.writeFieldBegin('outputDirPath', TType.STRING, 3)
            oprot.writeString(self.outputDirPath.encode('utf-8') if sys.version_info[0] == 2 else self.outputDirPath)
            oprot.writeFieldEnd()
        if self.inputDirPath is not None:
            oprot.writeFieldBegin('inputDirPath', TType.STRING, 4)
            oprot.writeString(self.inputDirPath.encode('utf-8') if sys.version_info[0] == 2 else self.inputDirPath)
            oprot.writeFieldEnd()
        if self.executionCommand is not None:
            oprot.writeFieldBegin('executionCommand', TType.STRING, 5)
            oprot.writeString(self.executionCommand.encode('utf-8') if sys.version_info[0] == 2 else self.executionCommand)
            oprot.writeFieldEnd()
        if self.inputFiles is not None:
            oprot.writeFieldBegin('inputFiles', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.inputFiles))
            for iter12 in self.inputFiles:
                iter12.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.outputFiles is not None:
            oprot.writeFieldBegin('outputFiles', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.outputFiles))
            for iter13 in self.outputFiles:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 8)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.imageName is None:
            raise TProtocolException(message='Required field imageName is unset!')
        if self.outputDirPath is None:
            raise TProtocolException(message='Required field outputDirPath is unset!')
        if self.inputDirPath is None:
            raise TProtocolException(message='Required field inputDirPath is unset!')
        if self.executionCommand is None:
            raise TProtocolException(message='Required field executionCommand is unset!')
        if self.inputFiles is None:
            raise TProtocolException(message='Required field inputFiles is unset!')
        if self.outputFiles is None:
            raise TProtocolException(message='Required field outputFiles is unset!')
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ParserConnectorInput(object):
    """
    Attributes:
     - id
     - inputId
     - parentOutputId
     - value
     - parserConnectorId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'inputId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'parentOutputId', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'value', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'parserConnectorId', 'UTF8', None, ),  # 5
    )

    def __init__(self, id=None, inputId=None, parentOutputId=None, value=None, parserConnectorId=None,):
        self.id = id
        self.inputId = inputId
        self.parentOutputId = parentOutputId
        self.value = value
        self.parserConnectorId = parserConnectorId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.inputId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.parentOutputId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.value = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.parserConnectorId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ParserConnectorInput')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.inputId is not None:
            oprot.writeFieldBegin('inputId', TType.STRING, 2)
            oprot.writeString(self.inputId.encode('utf-8') if sys.version_info[0] == 2 else self.inputId)
            oprot.writeFieldEnd()
        if self.parentOutputId is not None:
            oprot.writeFieldBegin('parentOutputId', TType.STRING, 3)
            oprot.writeString(self.parentOutputId.encode('utf-8') if sys.version_info[0] == 2 else self.parentOutputId)
            oprot.writeFieldEnd()
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.STRING, 4)
            oprot.writeString(self.value.encode('utf-8') if sys.version_info[0] == 2 else self.value)
            oprot.writeFieldEnd()
        if self.parserConnectorId is not None:
            oprot.writeFieldBegin('parserConnectorId', TType.STRING, 5)
            oprot.writeString(self.parserConnectorId.encode('utf-8') if sys.version_info[0] == 2 else self.parserConnectorId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.inputId is None:
            raise TProtocolException(message='Required field inputId is unset!')
        if self.parserConnectorId is None:
            raise TProtocolException(message='Required field parserConnectorId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ParserConnector(object):
    """
    Attributes:
     - id
     - parentParserId
     - childParserId
     - connectorInputs
     - parsingTemplateId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'parentParserId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'childParserId', 'UTF8', None, ),  # 3
        (4, TType.LIST, 'connectorInputs', (TType.STRUCT, (ParserConnectorInput, ParserConnectorInput.thrift_spec), False), None, ),  # 4
        (5, TType.STRING, 'parsingTemplateId', 'UTF8', None, ),  # 5
    )

    def __init__(self, id=None, parentParserId=None, childParserId=None, connectorInputs=None, parsingTemplateId=None,):
        self.id = id
        self.parentParserId = parentParserId
        self.childParserId = childParserId
        self.connectorInputs = connectorInputs
        self.parsingTemplateId = parsingTemplateId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.parentParserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.childParserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.connectorInputs = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = ParserConnectorInput()
                        _elem19.read(iprot)
                        self.connectorInputs.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.parsingTemplateId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ParserConnector')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.parentParserId is not None:
            oprot.writeFieldBegin('parentParserId', TType.STRING, 2)
            oprot.writeString(self.parentParserId.encode('utf-8') if sys.version_info[0] == 2 else self.parentParserId)
            oprot.writeFieldEnd()
        if self.childParserId is not None:
            oprot.writeFieldBegin('childParserId', TType.STRING, 3)
            oprot.writeString(self.childParserId.encode('utf-8') if sys.version_info[0] == 2 else self.childParserId)
            oprot.writeFieldEnd()
        if self.connectorInputs is not None:
            oprot.writeFieldBegin('connectorInputs', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.connectorInputs))
            for iter20 in self.connectorInputs:
                iter20.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.parsingTemplateId is not None:
            oprot.writeFieldBegin('parsingTemplateId', TType.STRING, 5)
            oprot.writeString(self.parsingTemplateId.encode('utf-8') if sys.version_info[0] == 2 else self.parsingTemplateId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.parentParserId is None:
            raise TProtocolException(message='Required field parentParserId is unset!')
        if self.childParserId is None:
            raise TProtocolException(message='Required field childParserId is unset!')
        if self.connectorInputs is None:
            raise TProtocolException(message='Required field connectorInputs is unset!')
        if self.parsingTemplateId is None:
            raise TProtocolException(message='Required field parsingTemplateId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ParsingTemplateInput(object):
    """
    Attributes:
     - id
     - targetInputId
     - applicationOutputName
     - value
     - parsingTemplateId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'targetInputId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'applicationOutputName', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'value', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'parsingTemplateId', 'UTF8', None, ),  # 5
    )

    def __init__(self, id=None, targetInputId=None, applicationOutputName=None, value=None, parsingTemplateId=None,):
        self.id = id
        self.targetInputId = targetInputId
        self.applicationOutputName = applicationOutputName
        self.value = value
        self.parsingTemplateId = parsingTemplateId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.targetInputId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.applicationOutputName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.value = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.parsingTemplateId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ParsingTemplateInput')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.targetInputId is not None:
            oprot.writeFieldBegin('targetInputId', TType.STRING, 2)
            oprot.writeString(self.targetInputId.encode('utf-8') if sys.version_info[0] == 2 else self.targetInputId)
            oprot.writeFieldEnd()
        if self.applicationOutputName is not None:
            oprot.writeFieldBegin('applicationOutputName', TType.STRING, 3)
            oprot.writeString(self.applicationOutputName.encode('utf-8') if sys.version_info[0] == 2 else self.applicationOutputName)
            oprot.writeFieldEnd()
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.STRING, 4)
            oprot.writeString(self.value.encode('utf-8') if sys.version_info[0] == 2 else self.value)
            oprot.writeFieldEnd()
        if self.parsingTemplateId is not None:
            oprot.writeFieldBegin('parsingTemplateId', TType.STRING, 5)
            oprot.writeString(self.parsingTemplateId.encode('utf-8') if sys.version_info[0] == 2 else self.parsingTemplateId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.targetInputId is None:
            raise TProtocolException(message='Required field targetInputId is unset!')
        if self.parsingTemplateId is None:
            raise TProtocolException(message='Required field parsingTemplateId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ParsingTemplate(object):
    """
    Attributes:
     - id
     - applicationInterface
     - initialInputs
     - parserConnections
     - gatewayId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'applicationInterface', 'UTF8', None, ),  # 2
        (3, TType.LIST, 'initialInputs', (TType.STRUCT, (ParsingTemplateInput, ParsingTemplateInput.thrift_spec), False), None, ),  # 3
        (4, TType.LIST, 'parserConnections', (TType.STRUCT, (ParserConnector, ParserConnector.thrift_spec), False), None, ),  # 4
        (5, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 5
    )

    def __init__(self, id=None, applicationInterface=None, initialInputs=None, parserConnections=None, gatewayId=None,):
        self.id = id
        self.applicationInterface = applicationInterface
        self.initialInputs = initialInputs
        self.parserConnections = parserConnections
        self.gatewayId = gatewayId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.applicationInterface = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.initialInputs = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = ParsingTemplateInput()
                        _elem26.read(iprot)
                        self.initialInputs.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.parserConnections = []
                    (_etype30, _size27) = iprot.readListBegin()
                    for _i31 in range(_size27):
                        _elem32 = ParserConnector()
                        _elem32.read(iprot)
                        self.parserConnections.append(_elem32)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ParsingTemplate')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.applicationInterface is not None:
            oprot.writeFieldBegin('applicationInterface', TType.STRING, 2)
            oprot.writeString(self.applicationInterface.encode('utf-8') if sys.version_info[0] == 2 else self.applicationInterface)
            oprot.writeFieldEnd()
        if self.initialInputs is not None:
            oprot.writeFieldBegin('initialInputs', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.initialInputs))
            for iter33 in self.initialInputs:
                iter33.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.parserConnections is not None:
            oprot.writeFieldBegin('parserConnections', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.parserConnections))
            for iter34 in self.parserConnections:
                iter34.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 5)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.applicationInterface is None:
            raise TProtocolException(message='Required field applicationInterface is unset!')
        if self.initialInputs is None:
            raise TProtocolException(message='Required field initialInputs is unset!')
        if self.parserConnections is None:
            raise TProtocolException(message='Required field parserConnections is unset!')
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
