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
import airavata.model.commons.ttypes

from thrift.transport import TTransport


class DMType(object):
    COMPUTE_RESOURCE = 0
    STORAGE_RESOURCE = 1

    _VALUES_TO_NAMES = {
        0: "COMPUTE_RESOURCE",
        1: "STORAGE_RESOURCE",
    }

    _NAMES_TO_VALUES = {
        "COMPUTE_RESOURCE": 0,
        "STORAGE_RESOURCE": 1,
    }


class SecurityProtocol(object):
    """
    Enumeration of security sshKeyAuthentication and authorization mechanisms supported by Airavata. This enumeration just
     describes the supported mechanism. The corresponding security credentials are registered with Airavata Credential
     store.

    USERNAME_PASSWORD:
     A User Name.

    SSH_KEYS:
     SSH Keys

    FIXME: Change GSI to a more precise generic security protocol - X509

    """
    USERNAME_PASSWORD = 0
    SSH_KEYS = 1
    GSI = 2
    KERBEROS = 3
    OAUTH = 4
    LOCAL = 5

    _VALUES_TO_NAMES = {
        0: "USERNAME_PASSWORD",
        1: "SSH_KEYS",
        2: "GSI",
        3: "KERBEROS",
        4: "OAUTH",
        5: "LOCAL",
    }

    _NAMES_TO_VALUES = {
        "USERNAME_PASSWORD": 0,
        "SSH_KEYS": 1,
        "GSI": 2,
        "KERBEROS": 3,
        "OAUTH": 4,
        "LOCAL": 5,
    }


class DataMovementProtocol(object):
    """
    Enumeration of data movement supported by Airavata

    SCP:
     Job manager supporting the Portal Batch System (PBS) protocol. Some examples include TORQUE, PBSPro, Grid Engine.

    SFTP:
     The Simple Linux Utility for Resource Management is a open source workload manager.

    GridFTP:
     Globus File Transfer Protocol

    UNICORE_STORAGE_SERVICE:
     Storage Service Provided by Unicore

    """
    LOCAL = 0
    SCP = 1
    SFTP = 2
    GridFTP = 3
    UNICORE_STORAGE_SERVICE = 4

    _VALUES_TO_NAMES = {
        0: "LOCAL",
        1: "SCP",
        2: "SFTP",
        3: "GridFTP",
        4: "UNICORE_STORAGE_SERVICE",
    }

    _NAMES_TO_VALUES = {
        "LOCAL": 0,
        "SCP": 1,
        "SFTP": 2,
        "GridFTP": 3,
        "UNICORE_STORAGE_SERVICE": 4,
    }


class SCPDataMovement(object):
    """
    Data Movement through Secured Copy

    alternativeSCPHostName:
     If the login to scp is different than the hostname itself, specify it here

    sshPort:
     If a non-default port needs to used, specify it.

    Attributes:
     - dataMovementInterfaceId
     - securityProtocol
     - alternativeSCPHostName
     - sshPort
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'dataMovementInterfaceId', 'UTF8', "DO_NOT_SET_AT_CLIENTS", ),  # 1
        (2, TType.I32, 'securityProtocol', None, None, ),  # 2
        (3, TType.STRING, 'alternativeSCPHostName', 'UTF8', None, ),  # 3
        (4, TType.I32, 'sshPort', None, 22, ),  # 4
    )

    def __init__(self, dataMovementInterfaceId=thrift_spec[1][4], securityProtocol=None, alternativeSCPHostName=None, sshPort=thrift_spec[4][4],):
        self.dataMovementInterfaceId = dataMovementInterfaceId
        self.securityProtocol = securityProtocol
        self.alternativeSCPHostName = alternativeSCPHostName
        self.sshPort = sshPort

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
                    self.dataMovementInterfaceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.securityProtocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.alternativeSCPHostName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.sshPort = iprot.readI32()
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
        oprot.writeStructBegin('SCPDataMovement')
        if self.dataMovementInterfaceId is not None:
            oprot.writeFieldBegin('dataMovementInterfaceId', TType.STRING, 1)
            oprot.writeString(self.dataMovementInterfaceId.encode('utf-8') if sys.version_info[0] == 2 else self.dataMovementInterfaceId)
            oprot.writeFieldEnd()
        if self.securityProtocol is not None:
            oprot.writeFieldBegin('securityProtocol', TType.I32, 2)
            oprot.writeI32(self.securityProtocol)
            oprot.writeFieldEnd()
        if self.alternativeSCPHostName is not None:
            oprot.writeFieldBegin('alternativeSCPHostName', TType.STRING, 3)
            oprot.writeString(self.alternativeSCPHostName.encode('utf-8') if sys.version_info[0] == 2 else self.alternativeSCPHostName)
            oprot.writeFieldEnd()
        if self.sshPort is not None:
            oprot.writeFieldBegin('sshPort', TType.I32, 4)
            oprot.writeI32(self.sshPort)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.dataMovementInterfaceId is None:
            raise TProtocolException(message='Required field dataMovementInterfaceId is unset!')
        if self.securityProtocol is None:
            raise TProtocolException(message='Required field securityProtocol is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GridFTPDataMovement(object):
    """
    Data Movement through GridFTP

    alternativeSCPHostName:
     If the login to scp is different than the hostname itself, specify it here

    sshPort:
     If a non-default port needs to used, specify it.

    Attributes:
     - dataMovementInterfaceId
     - securityProtocol
     - gridFTPEndPoints
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'dataMovementInterfaceId', 'UTF8', "DO_NOT_SET_AT_CLIENTS", ),  # 1
        (2, TType.I32, 'securityProtocol', None, None, ),  # 2
        (3, TType.LIST, 'gridFTPEndPoints', (TType.STRING, 'UTF8', False), None, ),  # 3
    )

    def __init__(self, dataMovementInterfaceId=thrift_spec[1][4], securityProtocol=None, gridFTPEndPoints=None,):
        self.dataMovementInterfaceId = dataMovementInterfaceId
        self.securityProtocol = securityProtocol
        self.gridFTPEndPoints = gridFTPEndPoints

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
                    self.dataMovementInterfaceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.securityProtocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.gridFTPEndPoints = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.gridFTPEndPoints.append(_elem5)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('GridFTPDataMovement')
        if self.dataMovementInterfaceId is not None:
            oprot.writeFieldBegin('dataMovementInterfaceId', TType.STRING, 1)
            oprot.writeString(self.dataMovementInterfaceId.encode('utf-8') if sys.version_info[0] == 2 else self.dataMovementInterfaceId)
            oprot.writeFieldEnd()
        if self.securityProtocol is not None:
            oprot.writeFieldBegin('securityProtocol', TType.I32, 2)
            oprot.writeI32(self.securityProtocol)
            oprot.writeFieldEnd()
        if self.gridFTPEndPoints is not None:
            oprot.writeFieldBegin('gridFTPEndPoints', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.gridFTPEndPoints))
            for iter6 in self.gridFTPEndPoints:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.dataMovementInterfaceId is None:
            raise TProtocolException(message='Required field dataMovementInterfaceId is unset!')
        if self.securityProtocol is None:
            raise TProtocolException(message='Required field securityProtocol is unset!')
        if self.gridFTPEndPoints is None:
            raise TProtocolException(message='Required field gridFTPEndPoints is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UnicoreDataMovement(object):
    """
    Data Movement through UnicoreStorage

    unicoreEndPointURL:
     unicoreGateway End Point. The provider will query this service to fetch required service end points.

    Attributes:
     - dataMovementInterfaceId
     - securityProtocol
     - unicoreEndPointURL
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'dataMovementInterfaceId', 'UTF8', "DO_NOT_SET_AT_CLIENTS", ),  # 1
        (2, TType.I32, 'securityProtocol', None, None, ),  # 2
        (3, TType.STRING, 'unicoreEndPointURL', 'UTF8', None, ),  # 3
    )

    def __init__(self, dataMovementInterfaceId=thrift_spec[1][4], securityProtocol=None, unicoreEndPointURL=None,):
        self.dataMovementInterfaceId = dataMovementInterfaceId
        self.securityProtocol = securityProtocol
        self.unicoreEndPointURL = unicoreEndPointURL

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
                    self.dataMovementInterfaceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.securityProtocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.unicoreEndPointURL = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('UnicoreDataMovement')
        if self.dataMovementInterfaceId is not None:
            oprot.writeFieldBegin('dataMovementInterfaceId', TType.STRING, 1)
            oprot.writeString(self.dataMovementInterfaceId.encode('utf-8') if sys.version_info[0] == 2 else self.dataMovementInterfaceId)
            oprot.writeFieldEnd()
        if self.securityProtocol is not None:
            oprot.writeFieldBegin('securityProtocol', TType.I32, 2)
            oprot.writeI32(self.securityProtocol)
            oprot.writeFieldEnd()
        if self.unicoreEndPointURL is not None:
            oprot.writeFieldBegin('unicoreEndPointURL', TType.STRING, 3)
            oprot.writeString(self.unicoreEndPointURL.encode('utf-8') if sys.version_info[0] == 2 else self.unicoreEndPointURL)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.dataMovementInterfaceId is None:
            raise TProtocolException(message='Required field dataMovementInterfaceId is unset!')
        if self.securityProtocol is None:
            raise TProtocolException(message='Required field securityProtocol is unset!')
        if self.unicoreEndPointURL is None:
            raise TProtocolException(message='Required field unicoreEndPointURL is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LOCALDataMovement(object):
    """
    LOCAL

    alternativeSCPHostName:
     If the login to scp is different than the hostname itself, specify it here

    sshPort:
     If a non-defualt port needs to used, specify it.

    Attributes:
     - dataMovementInterfaceId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'dataMovementInterfaceId', 'UTF8', "DO_NOT_SET_AT_CLIENTS", ),  # 1
    )

    def __init__(self, dataMovementInterfaceId=thrift_spec[1][4],):
        self.dataMovementInterfaceId = dataMovementInterfaceId

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
                    self.dataMovementInterfaceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('LOCALDataMovement')
        if self.dataMovementInterfaceId is not None:
            oprot.writeFieldBegin('dataMovementInterfaceId', TType.STRING, 1)
            oprot.writeString(self.dataMovementInterfaceId.encode('utf-8') if sys.version_info[0] == 2 else self.dataMovementInterfaceId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.dataMovementInterfaceId is None:
            raise TProtocolException(message='Required field dataMovementInterfaceId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DataMovementInterface(object):
    """
    Data Movement Interfaces

    dataMovementInterfaceId: The Data Movement Interface has to be previously registered and referenced here.

    priorityOrder:
     For resources with multiple interfaces, the priority order should be selected.
      Lower the numerical number, higher the priority


    Attributes:
     - dataMovementInterfaceId
     - dataMovementProtocol
     - priorityOrder
     - creationTime
     - updateTime
     - storageResourceId
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'dataMovementInterfaceId', 'UTF8', None, ),  # 1
        (2, TType.I32, 'dataMovementProtocol', None, None, ),  # 2
        (3, TType.I32, 'priorityOrder', None, 0, ),  # 3
        (4, TType.I64, 'creationTime', None, None, ),  # 4
        (5, TType.I64, 'updateTime', None, None, ),  # 5
        (6, TType.STRING, 'storageResourceId', 'UTF8', None, ),  # 6
    )

    def __init__(self, dataMovementInterfaceId=None, dataMovementProtocol=None, priorityOrder=thrift_spec[3][4], creationTime=None, updateTime=None, storageResourceId=None,):
        self.dataMovementInterfaceId = dataMovementInterfaceId
        self.dataMovementProtocol = dataMovementProtocol
        self.priorityOrder = priorityOrder
        self.creationTime = creationTime
        self.updateTime = updateTime
        self.storageResourceId = storageResourceId

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
                    self.dataMovementInterfaceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.dataMovementProtocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.priorityOrder = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.creationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.updateTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.storageResourceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('DataMovementInterface')
        if self.dataMovementInterfaceId is not None:
            oprot.writeFieldBegin('dataMovementInterfaceId', TType.STRING, 1)
            oprot.writeString(self.dataMovementInterfaceId.encode('utf-8') if sys.version_info[0] == 2 else self.dataMovementInterfaceId)
            oprot.writeFieldEnd()
        if self.dataMovementProtocol is not None:
            oprot.writeFieldBegin('dataMovementProtocol', TType.I32, 2)
            oprot.writeI32(self.dataMovementProtocol)
            oprot.writeFieldEnd()
        if self.priorityOrder is not None:
            oprot.writeFieldBegin('priorityOrder', TType.I32, 3)
            oprot.writeI32(self.priorityOrder)
            oprot.writeFieldEnd()
        if self.creationTime is not None:
            oprot.writeFieldBegin('creationTime', TType.I64, 4)
            oprot.writeI64(self.creationTime)
            oprot.writeFieldEnd()
        if self.updateTime is not None:
            oprot.writeFieldBegin('updateTime', TType.I64, 5)
            oprot.writeI64(self.updateTime)
            oprot.writeFieldEnd()
        if self.storageResourceId is not None:
            oprot.writeFieldBegin('storageResourceId', TType.STRING, 6)
            oprot.writeString(self.storageResourceId.encode('utf-8') if sys.version_info[0] == 2 else self.storageResourceId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.dataMovementInterfaceId is None:
            raise TProtocolException(message='Required field dataMovementInterfaceId is unset!')
        if self.dataMovementProtocol is None:
            raise TProtocolException(message='Required field dataMovementProtocol is unset!')
        if self.priorityOrder is None:
            raise TProtocolException(message='Required field priorityOrder is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
