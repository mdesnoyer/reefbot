FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/reefbot_msgs/msg"
  "../src/reefbot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/rosbuild_premsgsrvgen"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rosbuild_premsgsrvgen.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
