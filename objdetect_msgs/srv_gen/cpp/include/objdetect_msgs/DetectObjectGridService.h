/* Auto-generated by genmsg_cpp for file /home/mdesnoyer/src/reefbot/ros/objdetect_msgs/srv/DetectObjectGridService.srv */
#ifndef OBJDETECT_MSGS_SERVICE_DETECTOBJECTGRIDSERVICE_H
#define OBJDETECT_MSGS_SERVICE_DETECTOBJECTGRIDSERVICE_H
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

#include "ros/service_traits.h"

#include "objdetect_msgs/DetectObjectGrid.h"


#include "objdetect_msgs/DetectGridScores.h"

namespace objdetect_msgs
{
template <class ContainerAllocator>
struct DetectObjectGridServiceRequest_ {
  typedef DetectObjectGridServiceRequest_<ContainerAllocator> Type;

  DetectObjectGridServiceRequest_()
  : request_msg()
  {
  }

  DetectObjectGridServiceRequest_(const ContainerAllocator& _alloc)
  : request_msg(_alloc)
  {
  }

  typedef  ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator>  _request_msg_type;
   ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator>  request_msg;


  typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DetectObjectGridServiceRequest
typedef  ::objdetect_msgs::DetectObjectGridServiceRequest_<std::allocator<void> > DetectObjectGridServiceRequest;

typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceRequest> DetectObjectGridServiceRequestPtr;
typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceRequest const> DetectObjectGridServiceRequestConstPtr;


template <class ContainerAllocator>
struct DetectObjectGridServiceResponse_ {
  typedef DetectObjectGridServiceResponse_<ContainerAllocator> Type;

  DetectObjectGridServiceResponse_()
  : scores()
  {
  }

  DetectObjectGridServiceResponse_(const ContainerAllocator& _alloc)
  : scores(_alloc)
  {
  }

  typedef  ::objdetect_msgs::DetectGridScores_<ContainerAllocator>  _scores_type;
   ::objdetect_msgs::DetectGridScores_<ContainerAllocator>  scores;


  typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DetectObjectGridServiceResponse
typedef  ::objdetect_msgs::DetectObjectGridServiceResponse_<std::allocator<void> > DetectObjectGridServiceResponse;

typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceResponse> DetectObjectGridServiceResponsePtr;
typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGridServiceResponse const> DetectObjectGridServiceResponseConstPtr;

struct DetectObjectGridService
{

typedef DetectObjectGridServiceRequest Request;
typedef DetectObjectGridServiceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct DetectObjectGridService
} // namespace objdetect_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "355207a78269e9b7a5e2cc2db0546ba5";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x355207a78269e9b7ULL;
  static const uint64_t static_value2 = 0xa5e2cc2db0546ba5ULL;
};

template<class ContainerAllocator>
struct DataType< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObjectGridServiceRequest";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "DetectObjectGrid request_msg\n\
\n\
================================================================================\n\
MSG: objdetect_msgs/DetectObjectGrid\n\
# To detect an object on a w,h,x,y grid. It is more compressed than listing all of the boxes we care about\n\
\n\
Header header\n\
\n\
# The image to find objects in\n\
sensor_msgs/Image image\n\
\n\
# The (w,h,x,y) grid to search on\n\
Grid grid\n\
\n\
# An optional binary mask that is 4 dimensional (w,h,x,y) and\n\
# specifies which entries we actually want to search in\n\
sensor_msgs/MatND mask\n\
\n\
\n\
\n\
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
MSG: objdetect_msgs/Grid\n\
# Specifies a  w,h,x,y dense grid\n\
# The starting points for the location search\n\
uint32 minX\n\
uint32 minY\n\
\n\
# The strides in the location space\n\
uint32 strideX\n\
uint32 strideY\n\
\n\
# The starting points for the scaling\n\
uint32 minW\n\
uint32 minH\n\
\n\
# The strides in the w, h space. In this case, we step by growing by a\n\
# fraction, so that width_i is round(minWidth*strideW^i)\n\
float64 strideW\n\
float64 strideH\n\
\n\
# True if the width and height should be a consistent aspect ratio that are \n\
# defined by minW and minH. This reduces the grid to (s,x,y)\n\
bool fixAspect\n\
================================================================================\n\
MSG: sensor_msgs/MatND\n\
# A message that contains an uncompressed n dimensional\n\
# matrix. Designed to be compatible with the opencv n-dimensional\n\
# matrix.\n\
Header header\n\
\n\
int32[] sizes # The size of each dimension in the matrix\n\
\n\
string encoding # The data type see src/image_encodings.cpp\n\
\n\
bool is_bigendian # Is the data bigendian?\n\
\n\
uint8[] data # The actual data\n\
\n\
";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "10d41d63f25679f70d16a37d38a4ce09";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x10d41d63f25679f7ULL;
  static const uint64_t static_value2 = 0x0d16a37d38a4ce09ULL;
};

template<class ContainerAllocator>
struct DataType< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObjectGridServiceResponse";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "DetectGridScores scores\n\
\n\
================================================================================\n\
MSG: objdetect_msgs/DetectGridScores\n\
# Specifies socres on a detection grid that runs (x,y,w,h). If the aspect ratio is fixed, this will change to (x,y,s)\n\
\n\
Header header\n\
\n\
# The (w,h,x,y) grid that has a response\n\
Grid grid\n\
\n\
# A grid of scores across the space that are based on an evaluation\n\
# for each box.\n\
sensor_msgs/MatND scores\n\
\n\
# An optional binary mask that is 4 dimensional (w,h,x,y) and\n\
# specifies which entries have valid values\n\
sensor_msgs/MatND mask\n\
\n\
# The processing time to calculate the detection\n\
std_msgs/Duration processing_time\n\
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
MSG: objdetect_msgs/Grid\n\
# Specifies a  w,h,x,y dense grid\n\
# The starting points for the location search\n\
uint32 minX\n\
uint32 minY\n\
\n\
# The strides in the location space\n\
uint32 strideX\n\
uint32 strideY\n\
\n\
# The starting points for the scaling\n\
uint32 minW\n\
uint32 minH\n\
\n\
# The strides in the w, h space. In this case, we step by growing by a\n\
# fraction, so that width_i is round(minWidth*strideW^i)\n\
float64 strideW\n\
float64 strideH\n\
\n\
# True if the width and height should be a consistent aspect ratio that are \n\
# defined by minW and minH. This reduces the grid to (s,x,y)\n\
bool fixAspect\n\
================================================================================\n\
MSG: sensor_msgs/MatND\n\
# A message that contains an uncompressed n dimensional\n\
# matrix. Designed to be compatible with the opencv n-dimensional\n\
# matrix.\n\
Header header\n\
\n\
int32[] sizes # The size of each dimension in the matrix\n\
\n\
string encoding # The data type see src/image_encodings.cpp\n\
\n\
bool is_bigendian # Is the data bigendian?\n\
\n\
uint8[] data # The actual data\n\
\n\
================================================================================\n\
MSG: std_msgs/Duration\n\
duration data\n\
\n\
";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.request_msg);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DetectObjectGridServiceRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.scores);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DetectObjectGridServiceResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<objdetect_msgs::DetectObjectGridService> {
  static const char* value() 
  {
    return "e387077e439fcb0349b2190bd0852bae";
  }

  static const char* value(const objdetect_msgs::DetectObjectGridService&) { return value(); } 
};

template<>
struct DataType<objdetect_msgs::DetectObjectGridService> {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObjectGridService";
  }

  static const char* value(const objdetect_msgs::DetectObjectGridService&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e387077e439fcb0349b2190bd0852bae";
  }

  static const char* value(const objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObjectGridService";
  }

  static const char* value(const objdetect_msgs::DetectObjectGridServiceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e387077e439fcb0349b2190bd0852bae";
  }

  static const char* value(const objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObjectGridService";
  }

  static const char* value(const objdetect_msgs::DetectObjectGridServiceResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // OBJDETECT_MSGS_SERVICE_DETECTOBJECTGRIDSERVICE_H

