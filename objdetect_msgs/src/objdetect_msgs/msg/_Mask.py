"""autogenerated by genpy from objdetect_msgs/Mask.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import sensor_msgs.msg

class Mask(genpy.Message):
  _md5sum = "ecbf10b456dc7d2982ac745b3ea8ef9c"
  _type = "objdetect_msgs/Mask"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# this message is used to mark where an object is present in an image
# this can be done either by a roi region on the image (less precise)
# or a mask (more precise)

sensor_msgs/RegionOfInterest roi

# in the case when mask is used, 'roi' specifies the image region and 'mask'
# (which should be of the same size) a binary mask in that region
sensor_msgs/Image mask
================================================================================
MSG: sensor_msgs/RegionOfInterest
# This message is used to specify a region of interest within an image.
#
# When used to specify the ROI setting of the camera when the image was
# taken, the height and width fields should either match the height and
# width fields for the associated image; or height = width = 0
# indicates that the full resolution image was captured.

uint32 x_offset  # Leftmost pixel of the ROI
                 # (0 if the ROI includes the left edge of the image)
uint32 y_offset  # Topmost pixel of the ROI
                 # (0 if the ROI includes the top edge of the image)
uint32 height    # Height of ROI
uint32 width     # Width of ROI

# True if a distinct rectified ROI should be calculated from the "raw"
# ROI in this message. Typically this should be False if the full image
# is captured (ROI not used), and True if a subwindow is captured (ROI
# used).
bool do_rectify

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in src/image_encodings.cpp

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

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

"""
  __slots__ = ['roi','mask']
  _slot_types = ['sensor_msgs/RegionOfInterest','sensor_msgs/Image']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       roi,mask

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Mask, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.roi is None:
        self.roi = sensor_msgs.msg.RegionOfInterest()
      if self.mask is None:
        self.mask = sensor_msgs.msg.Image()
    else:
      self.roi = sensor_msgs.msg.RegionOfInterest()
      self.mask = sensor_msgs.msg.Image()

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
      buff.write(_struct_4IB3I.pack(_x.roi.x_offset, _x.roi.y_offset, _x.roi.height, _x.roi.width, _x.roi.do_rectify, _x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs))
      _x = self.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.mask.height, _x.mask.width))
      _x = self.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_BI.pack(_x.mask.is_bigendian, _x.mask.step))
      _x = self.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.roi is None:
        self.roi = sensor_msgs.msg.RegionOfInterest()
      if self.mask is None:
        self.mask = sensor_msgs.msg.Image()
      end = 0
      _x = self
      start = end
      end += 29
      (_x.roi.x_offset, _x.roi.y_offset, _x.roi.height, _x.roi.width, _x.roi.do_rectify, _x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs,) = _struct_4IB3I.unpack(str[start:end])
      self.roi.do_rectify = bool(self.roi.do_rectify)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.mask.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.mask.height, _x.mask.width,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.mask.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.mask.is_bigendian, _x.mask.step,) = _struct_BI.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.data = str[start:end].decode('utf-8')
      else:
        self.mask.data = str[start:end]
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
      buff.write(_struct_4IB3I.pack(_x.roi.x_offset, _x.roi.y_offset, _x.roi.height, _x.roi.width, _x.roi.do_rectify, _x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs))
      _x = self.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.mask.height, _x.mask.width))
      _x = self.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_BI.pack(_x.mask.is_bigendian, _x.mask.step))
      _x = self.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
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
      if self.roi is None:
        self.roi = sensor_msgs.msg.RegionOfInterest()
      if self.mask is None:
        self.mask = sensor_msgs.msg.Image()
      end = 0
      _x = self
      start = end
      end += 29
      (_x.roi.x_offset, _x.roi.y_offset, _x.roi.height, _x.roi.width, _x.roi.do_rectify, _x.mask.header.seq, _x.mask.header.stamp.secs, _x.mask.header.stamp.nsecs,) = _struct_4IB3I.unpack(str[start:end])
      self.roi.do_rectify = bool(self.roi.do_rectify)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.mask.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.mask.height, _x.mask.width,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.mask.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.mask.is_bigendian, _x.mask.step,) = _struct_BI.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mask.data = str[start:end].decode('utf-8')
      else:
        self.mask.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4IB3I = struct.Struct("<4IB3I")
_struct_2I = struct.Struct("<2I")
_struct_BI = struct.Struct("<BI")
