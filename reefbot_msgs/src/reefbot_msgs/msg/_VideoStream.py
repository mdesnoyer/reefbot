"""autogenerated by genpy from reefbot_msgs/VideoStream.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class VideoStream(genpy.Message):
  _md5sum = "cd586f51ec0610ad4479871c38166fc8"
  _type = "reefbot_msgs/VideoStream"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message specifies the url that the video stream is being
# broadcast at. This allows us to change the video settings on the fly
# by sending this message.
#
# Author: Mark Desnoyer (markd@cmu.edu)
# Date: July 2010

std_msgs/String url
================================================================================
MSG: std_msgs/String
string data

"""
  __slots__ = ['url']
  _slot_types = ['std_msgs/String']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       url

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VideoStream, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.url is None:
        self.url = std_msgs.msg.String()
    else:
      self.url = std_msgs.msg.String()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.url.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.url is None:
        self.url = std_msgs.msg.String()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.url.data = str[start:end].decode('utf-8')
      else:
        self.url.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.url.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.url is None:
        self.url = std_msgs.msg.String()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.url.data = str[start:end].decode('utf-8')
      else:
        self.url.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
