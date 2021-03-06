/* Auto-generated by genmsg_cpp for file /home/mdesnoyer/src/reefbot/ros/objdetect_msgs/msg/DetectObject.msg */
#ifndef OBJDETECT_MSGS_MESSAGE_DETECTOBJECT_H
#define OBJDETECT_MSGS_MESSAGE_DETECTOBJECT_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "sensor_msgs/Image.h"
#include "sensor_msgs/RegionOfInterest.h"

namespace objdetect_msgs
{
template <class ContainerAllocator>
struct DetectObject_ {
  typedef DetectObject_<ContainerAllocator> Type;

  DetectObject_()
  : header()
  , image()
  , regions()
  {
  }

  DetectObject_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , image(_alloc)
  , regions(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_type;
   ::sensor_msgs::Image_<ContainerAllocator>  image;

  typedef std::vector< ::sensor_msgs::RegionOfInterest_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::sensor_msgs::RegionOfInterest_<ContainerAllocator> >::other >  _regions_type;
  std::vector< ::sensor_msgs::RegionOfInterest_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::sensor_msgs::RegionOfInterest_<ContainerAllocator> >::other >  regions;


  typedef boost::shared_ptr< ::objdetect_msgs::DetectObject_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::objdetect_msgs::DetectObject_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DetectObject
typedef  ::objdetect_msgs::DetectObject_<std::allocator<void> > DetectObject;

typedef boost::shared_ptr< ::objdetect_msgs::DetectObject> DetectObjectPtr;
typedef boost::shared_ptr< ::objdetect_msgs::DetectObject const> DetectObjectConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::objdetect_msgs::DetectObject_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::objdetect_msgs::DetectObject_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace objdetect_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObject_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObject_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::objdetect_msgs::DetectObject_<ContainerAllocator> > {
  static const char* value() 
  {
    return "58706fab49b7608f7f3527c1eeb855bc";
  }

  static const char* value(const  ::objdetect_msgs::DetectObject_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x58706fab49b7608fULL;
  static const uint64_t static_value2 = 0x7f3527c1eeb855bcULL;
};

template<class ContainerAllocator>
struct DataType< ::objdetect_msgs::DetectObject_<ContainerAllocator> > {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObject";
  }

  static const char* value(const  ::objdetect_msgs::DetectObject_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::objdetect_msgs::DetectObject_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
# The image to find objects in\n\
sensor_msgs/Image image\n\
\n\
# Regions of interest to look for the object. If it is empty, search\n\
# through the entire image\n\
sensor_msgs/RegionOfInterest[] regions\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: sensor_msgs/Image\n\
# This message contains an uncompressed image\n\
# (0, 0) is at top-left corner of image\n\
#\n\
\n\
Header header        # Header timestamp should be acquisition time of image\n\
                     # Header frame_id should be optical frame of camera\n\
                     # origin of frame should be optical center of cameara\n\
                     # +x should point to the right in the image\n\
                     # +y should point down in the image\n\
                     # +z should point into to plane of the image\n\
                     # If the frame_id here and the frame_id of the CameraInfo\n\
                     # message associated with the image conflict\n\
                     # the behavior is undefined\n\
\n\
uint32 height         # image height, that is, number of rows\n\
uint32 width          # image width, that is, number of columns\n\
\n\
# The legal values for encoding are in file src/image_encodings.cpp\n\
# If you want to standardize a new string format, join\n\
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n\
\n\
string encoding       # Encoding of pixels -- channel meaning, ordering, size\n\
                      # taken from the list of strings in src/image_encodings.cpp\n\
\n\
uint8 is_bigendian    # is this data bigendian?\n\
uint32 step           # Full row length in bytes\n\
uint8[] data          # actual matrix data, size is (step * rows)\n\
\n\
================================================================================\n\
MSG: sensor_msgs/RegionOfInterest\n\
# This message is used to specify a region of interest within an image.\n\
#\n\
# When used to specify the ROI setting of the camera when the image was\n\
# taken, the height and width fields should either match the height and\n\
# width fields for the associated image; or height = width = 0\n\
# indicates that the full resolution image was captured.\n\
\n\
uint32 x_offset  # Leftmost pixel of the ROI\n\
                 # (0 if the ROI includes the left edge of the image)\n\
uint32 y_offset  # Topmost pixel of the ROI\n\
                 # (0 if the ROI includes the top edge of the image)\n\
uint32 height    # Height of ROI\n\
uint32 width     # Width of ROI\n\
\n\
# True if a distinct rectified ROI should be calculated from the \"raw\"\n\
# ROI in this message. Typically this should be False if the full image\n\
# is captured (ROI not used), and True if a subwindow is captured (ROI\n\
# used).\n\
bool do_rectify\n\
\n\
";
  }

  static const char* value(const  ::objdetect_msgs::DetectObject_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::objdetect_msgs::DetectObject_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::objdetect_msgs::DetectObject_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::objdetect_msgs::DetectObject_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.image);
    stream.next(m.regions);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DetectObject_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::objdetect_msgs::DetectObject_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::objdetect_msgs::DetectObject_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "image: ";
s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.image);
    s << indent << "regions[]" << std::endl;
    for (size_t i = 0; i < v.regions.size(); ++i)
    {
      s << indent << "  regions[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::sensor_msgs::RegionOfInterest_<ContainerAllocator> >::stream(s, indent + "    ", v.regions[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // OBJDETECT_MSGS_MESSAGE_DETECTOBJECT_H

