FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/objdetect_msgs/msg"
  "../src/objdetect_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/objdetect_msgs/srv/__init__.py"
  "../src/objdetect_msgs/srv/_DetectObjectGridService.py"
  "../src/objdetect_msgs/srv/_DetectObjectService.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
