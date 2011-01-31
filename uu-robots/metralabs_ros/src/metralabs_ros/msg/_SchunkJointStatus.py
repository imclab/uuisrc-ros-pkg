"""autogenerated by genmsg_py from SchunkJointStatus.msg. Do not edit."""
import roslib.message
import struct


class SchunkJointStatus(roslib.message.Message):
  _md5sum = "02b6a38cdad0883cadc61b1ddb8b7bb3"
  _type = "metralabs_ros/SchunkJointStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string  jointName
float32 current
uint8 errorCode
bool referenced
bool moving
bool progMode
bool warning
bool error 
bool brake
bool moveEnd
bool posReached

"""
  __slots__ = ['jointName','current','errorCode','referenced','moving','progMode','warning','error','brake','moveEnd','posReached']
  _slot_types = ['string','float32','uint8','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       jointName,current,errorCode,referenced,moving,progMode,warning,error,brake,moveEnd,posReached
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(SchunkJointStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.jointName is None:
        self.jointName = ''
      if self.current is None:
        self.current = 0.
      if self.errorCode is None:
        self.errorCode = 0
      if self.referenced is None:
        self.referenced = False
      if self.moving is None:
        self.moving = False
      if self.progMode is None:
        self.progMode = False
      if self.warning is None:
        self.warning = False
      if self.error is None:
        self.error = False
      if self.brake is None:
        self.brake = False
      if self.moveEnd is None:
        self.moveEnd = False
      if self.posReached is None:
        self.posReached = False
    else:
      self.jointName = ''
      self.current = 0.
      self.errorCode = 0
      self.referenced = False
      self.moving = False
      self.progMode = False
      self.warning = False
      self.error = False
      self.brake = False
      self.moveEnd = False
      self.posReached = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self.jointName
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_f9B.pack(_x.current, _x.errorCode, _x.referenced, _x.moving, _x.progMode, _x.warning, _x.error, _x.brake, _x.moveEnd, _x.posReached))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.jointName = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.current, _x.errorCode, _x.referenced, _x.moving, _x.progMode, _x.warning, _x.error, _x.brake, _x.moveEnd, _x.posReached,) = _struct_f9B.unpack(str[start:end])
      self.referenced = bool(self.referenced)
      self.moving = bool(self.moving)
      self.progMode = bool(self.progMode)
      self.warning = bool(self.warning)
      self.error = bool(self.error)
      self.brake = bool(self.brake)
      self.moveEnd = bool(self.moveEnd)
      self.posReached = bool(self.posReached)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self.jointName
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_f9B.pack(_x.current, _x.errorCode, _x.referenced, _x.moving, _x.progMode, _x.warning, _x.error, _x.brake, _x.moveEnd, _x.posReached))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.jointName = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.current, _x.errorCode, _x.referenced, _x.moving, _x.progMode, _x.warning, _x.error, _x.brake, _x.moveEnd, _x.posReached,) = _struct_f9B.unpack(str[start:end])
      self.referenced = bool(self.referenced)
      self.moving = bool(self.moving)
      self.progMode = bool(self.progMode)
      self.warning = bool(self.warning)
      self.error = bool(self.error)
      self.brake = bool(self.brake)
      self.moveEnd = bool(self.moveEnd)
      self.posReached = bool(self.posReached)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_f9B = struct.Struct("<f9B")