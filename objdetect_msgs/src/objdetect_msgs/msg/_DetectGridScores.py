"""autogenerated by genpy from objdetect_msgs/DetectGridScores.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import genpy
import objdetect_msgs.msg
import std_msgs.msg

class DetectGridScores(genpy.Message):
  _md5sum = "177d931fe6488b6b75f16e4d7b7caf56"
  _type = "objdetect_msgs/DetectGridScores"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Specifies socres on a detection grid that runs (x,y,w,h). If the aspect ratio is fixed, this will change to (x,y,s)

Header header

# The (w,h,x,y) grid that has a response
Grid grid

# A grid of scores across the space that are based on an evaluation
# for each box.
sensor_msgs/MatND scores

# An optional binary mask that is 4 dimensional (w,h,x,y) and
# specifies which entries have valid values
sensor_msgs/MatND mask

# The processing time to calculate the detection
std_msgs/Duration processing_time
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: objdetect_msgs/Grid
# Specifies a  w,h,x,y dense grid
# The starting points for the location search
uint32 minX
uint32 minY

# The strides in the location space
uint32 strideX
uint32 strideY

# The starting points for the scaling
uint32 minW
uint32 minH

# The strides in the w, h space. In this case, we step by growing by a
# fraction, so that width_i is round(minWidth*strideW^i)
float64 strideW
float64 strideH

# True if the width and height should be a consistent aspect ratio that are 
# defined by minW and minH. This reduces the grid to (s,x,y)
bool fixAspect
================================================================================
MSG: sensor_msgs/MatND
# A message that contains an uncompressed n dimensional
# matrix. Designed to be compatible with the opencv n-dimensional
# matrix.
Header header

int32[] sizes # The size of each dimension in the matrix

string encoding # The data type see src/image_encodings.cpp

bool is_bigendian # Is the data bigendian?

uint8[] data # The actual data

================================================================================
MSG: std_msgs/Duration
duration data

"""
  __slots__ = ['header','grid','scores','mask','processing_time']
  _slot_types = ['std_msgs/Header','objdetect_msgs/Grid','sensor_msgs/MatND','sensor_msgs/MatND','std_msgs/Duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,grid,scores,mask,processing_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DetectGridScores, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.grid is None:
        self.grid = objdetect_msgs.msg.Grid()
      if self.scores is None:
        self.scores = sensor_msgs.msg.MatND()
      if self.mask is None:
        self.mask = sensor_msgs.msg.MatND()
      if self.processing_time is None:
        self.processing_time = std_msgs.msg.Duration()
    else:
      self.header = std_msgs.msg.Header()
      self.grid = objdetect_msgs.msg.Grid()
      self.scores = sensor_msgs.msg.MatND()
      self.mask = sensor_msgs.msg.MatND()
      self.processing_time = std_msgs.msg.Duration()

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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6I2dB3I.pack(_x.grid.minX, _x.grid.minY, _x.grid.strideX, _x.grid.strideY, _x.grid.minW, _x.grid.minH, _x.grid.strideW, _x.grid.strideH, _x.grid.fixAspect, _x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs))
      _x = self.scores.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.scores.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.scores.sizes))
      _x = self.scores.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.scores.is_bigendian))
      _x = self.scores.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs))
      _x = self.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.mask.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.mask.sizes))
      _x = self.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.mask.is_bigendian))
      _x = self.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.processing_time.data.secs, _x.processing_time.data.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.grid is None:
        self.grid = objdetect_msgs.msg.Grid()
      if self.scores is None:
        self.scores = sensor_msgs.msg.MatND()
      if self.mask is None:
        self.mask = sensor_msgs.msg.MatND()
      if self.processing_time is None:
        self.processing_time = std_msgs.msg.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 53
      (_x.grid.minX, _x.grid.minY, _x.grid.strideX, _x.grid.strideY, _x.grid.minW, _x.grid.minH, _x.grid.strideW, _x.grid.strideH, _x.grid.fixAspect, _x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs,) = _struct_6I2dB3I.unpack(str[start:end])
      self.grid.fixAspect = bool(self.grid.fixAspect)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.scores.sizes = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.encoding = str[start:end].decode('utf-8')
      else:
        self.scores.encoding = str[start:end]
      start = end
      end += 1
      (self.scores.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.scores.is_bigendian = bool(self.scores.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.data = str[start:end].decode('utf-8')
      else:
        self.scores.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.mask.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.mask.sizes = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.mask.encoding = str[start:end]
      start = end
      end += 1
      (self.mask.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.mask.is_bigendian = bool(self.mask.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.data = str[start:end].decode('utf-8')
      else:
        self.mask.data = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.processing_time.data.secs, _x.processing_time.data.nsecs,) = _struct_2i.unpack(str[start:end])
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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6I2dB3I.pack(_x.grid.minX, _x.grid.minY, _x.grid.strideX, _x.grid.strideY, _x.grid.minW, _x.grid.minH, _x.grid.strideW, _x.grid.strideH, _x.grid.fixAspect, _x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs))
      _x = self.scores.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.scores.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.scores.sizes.tostring())
      _x = self.scores.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.scores.is_bigendian))
      _x = self.scores.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs))
      _x = self.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.mask.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.mask.sizes.tostring())
      _x = self.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.mask.is_bigendian))
      _x = self.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.processing_time.data.secs, _x.processing_time.data.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.grid is None:
        self.grid = objdetect_msgs.msg.Grid()
      if self.scores is None:
        self.scores = sensor_msgs.msg.MatND()
      if self.mask is None:
        self.mask = sensor_msgs.msg.MatND()
      if self.processing_time is None:
        self.processing_time = std_msgs.msg.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 53
      (_x.grid.minX, _x.grid.minY, _x.grid.strideX, _x.grid.strideY, _x.grid.minW, _x.grid.minH, _x.grid.strideW, _x.grid.strideH, _x.grid.fixAspect, _x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs,) = _struct_6I2dB3I.unpack(str[start:end])
      self.grid.fixAspect = bool(self.grid.fixAspect)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.scores.sizes = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.encoding = str[start:end].decode('utf-8')
      else:
        self.scores.encoding = str[start:end]
      start = end
      end += 1
      (self.scores.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.scores.is_bigendian = bool(self.scores.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.data = str[start:end].decode('utf-8')
      else:
        self.scores.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.mask.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.mask.sizes = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.mask.encoding = str[start:end]
      start = end
      end += 1
      (self.mask.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.mask.is_bigendian = bool(self.mask.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.data = str[start:end].decode('utf-8')
      else:
        self.mask.data = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.processing_time.data.secs, _x.processing_time.data.nsecs,) = _struct_2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_6I2dB3I = struct.Struct("<6I2dB3I")
_struct_2i = struct.Struct("<2i")
