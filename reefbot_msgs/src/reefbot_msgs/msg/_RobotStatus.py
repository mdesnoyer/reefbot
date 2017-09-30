"""autogenerated by genpy from reefbot_msgs/RobotStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class RobotStatus(genpy.Message):
  _md5sum = "cb292a55b3deef4985b50365294fba83"
  _type = "reefbot_msgs/RobotStatus"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This message specifies the physical status of the robot as known by
# the RobotController. This will be used to display the status to the
# user.
#
# Author: Mark Desnoyer (markd@cmu.edu)
# Date: July 2010

Header header

# Speeds of all the thursters. Positive is forward or up
# TODO(mdesnoyer, furlong) define the units (RPM maybe?)
float32 left_speed
float32 right_speed
float32 vertical_speed

# Depth of the robot in meters according to the depth sensor
float32 depth

# Compass heading in degrees where 0 is N, 90 is E, 180 is S and 270 is W
float32 heading
float32 roll
float32 pitch

float32 internal_humidity
float32 water_temp

float32 spin_count

float32 internal_temp
float32 total_power
float32 voltage_drop
float32 tether_voltage
float32 bus_voltage
float32 bus_current
float32 comm_error_count


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
  __slots__ = ['header','left_speed','right_speed','vertical_speed','depth','heading','roll','pitch','internal_humidity','water_temp','spin_count','internal_temp','total_power','voltage_drop','tether_voltage','bus_voltage','bus_current','comm_error_count']
  _slot_types = ['std_msgs/Header','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,left_speed,right_speed,vertical_speed,depth,heading,roll,pitch,internal_humidity,water_temp,spin_count,internal_temp,total_power,voltage_drop,tether_voltage,bus_voltage,bus_current,comm_error_count

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RobotStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.left_speed is None:
        self.left_speed = 0.
      if self.right_speed is None:
        self.right_speed = 0.
      if self.vertical_speed is None:
        self.vertical_speed = 0.
      if self.depth is None:
        self.depth = 0.
      if self.heading is None:
        self.heading = 0.
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.internal_humidity is None:
        self.internal_humidity = 0.
      if self.water_temp is None:
        self.water_temp = 0.
      if self.spin_count is None:
        self.spin_count = 0.
      if self.internal_temp is None:
        self.internal_temp = 0.
      if self.total_power is None:
        self.total_power = 0.
      if self.voltage_drop is None:
        self.voltage_drop = 0.
      if self.tether_voltage is None:
        self.tether_voltage = 0.
      if self.bus_voltage is None:
        self.bus_voltage = 0.
      if self.bus_current is None:
        self.bus_current = 0.
      if self.comm_error_count is None:
        self.comm_error_count = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.left_speed = 0.
      self.right_speed = 0.
      self.vertical_speed = 0.
      self.depth = 0.
      self.heading = 0.
      self.roll = 0.
      self.pitch = 0.
      self.internal_humidity = 0.
      self.water_temp = 0.
      self.spin_count = 0.
      self.internal_temp = 0.
      self.total_power = 0.
      self.voltage_drop = 0.
      self.tether_voltage = 0.
      self.bus_voltage = 0.
      self.bus_current = 0.
      self.comm_error_count = 0.

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
      buff.write(_struct_17f.pack(_x.left_speed, _x.right_speed, _x.vertical_speed, _x.depth, _x.heading, _x.roll, _x.pitch, _x.internal_humidity, _x.water_temp, _x.spin_count, _x.internal_temp, _x.total_power, _x.voltage_drop, _x.tether_voltage, _x.bus_voltage, _x.bus_current, _x.comm_error_count))
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
      end += 68
      (_x.left_speed, _x.right_speed, _x.vertical_speed, _x.depth, _x.heading, _x.roll, _x.pitch, _x.internal_humidity, _x.water_temp, _x.spin_count, _x.internal_temp, _x.total_power, _x.voltage_drop, _x.tether_voltage, _x.bus_voltage, _x.bus_current, _x.comm_error_count,) = _struct_17f.unpack(str[start:end])
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
      buff.write(_struct_17f.pack(_x.left_speed, _x.right_speed, _x.vertical_speed, _x.depth, _x.heading, _x.roll, _x.pitch, _x.internal_humidity, _x.water_temp, _x.spin_count, _x.internal_temp, _x.total_power, _x.voltage_drop, _x.tether_voltage, _x.bus_voltage, _x.bus_current, _x.comm_error_count))
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
      end += 68
      (_x.left_speed, _x.right_speed, _x.vertical_speed, _x.depth, _x.heading, _x.roll, _x.pitch, _x.internal_humidity, _x.water_temp, _x.spin_count, _x.internal_temp, _x.total_power, _x.voltage_drop, _x.tether_voltage, _x.bus_voltage, _x.bus_current, _x.comm_error_count,) = _struct_17f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_17f = struct.Struct("<17f")
_struct_3I = struct.Struct("<3I")