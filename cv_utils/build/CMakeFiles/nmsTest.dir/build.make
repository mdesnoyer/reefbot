# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mdesnoyer/src/reefbot/ros/cv_utils

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mdesnoyer/src/reefbot/ros/cv_utils/build

# Include any dependencies generated for this target.
include CMakeFiles/nmsTest.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/nmsTest.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/nmsTest.dir/flags.make

CMakeFiles/nmsTest.dir/test/nmsTest.o: CMakeFiles/nmsTest.dir/flags.make
CMakeFiles/nmsTest.dir/test/nmsTest.o: ../test/nmsTest.cc
CMakeFiles/nmsTest.dir/test/nmsTest.o: ../manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /opt/ros/fuerte/share/roslang/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /opt/ros/fuerte/share/roscpp/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /opt/ros/fuerte/share/rosbag/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /opt/ros/fuerte/share/std_msgs/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /opt/ros/fuerte/share/rosconsole/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /home/mdesnoyer/src/reefbot/ros/sensor_msgs/manifest.xml
CMakeFiles/nmsTest.dir/test/nmsTest.o: /home/mdesnoyer/src/reefbot/ros/sensor_msgs/msg_gen/generated
CMakeFiles/nmsTest.dir/test/nmsTest.o: /home/mdesnoyer/src/reefbot/ros/sensor_msgs/srv_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/mdesnoyer/src/reefbot/ros/cv_utils/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/nmsTest.dir/test/nmsTest.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -W -Wall -Wno-unused-parameter -fno-strict-aliasing -pthread -o CMakeFiles/nmsTest.dir/test/nmsTest.o -c /home/mdesnoyer/src/reefbot/ros/cv_utils/test/nmsTest.cc

CMakeFiles/nmsTest.dir/test/nmsTest.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/nmsTest.dir/test/nmsTest.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -W -Wall -Wno-unused-parameter -fno-strict-aliasing -pthread -E /home/mdesnoyer/src/reefbot/ros/cv_utils/test/nmsTest.cc > CMakeFiles/nmsTest.dir/test/nmsTest.i

CMakeFiles/nmsTest.dir/test/nmsTest.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/nmsTest.dir/test/nmsTest.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -W -Wall -Wno-unused-parameter -fno-strict-aliasing -pthread -S /home/mdesnoyer/src/reefbot/ros/cv_utils/test/nmsTest.cc -o CMakeFiles/nmsTest.dir/test/nmsTest.s

CMakeFiles/nmsTest.dir/test/nmsTest.o.requires:
.PHONY : CMakeFiles/nmsTest.dir/test/nmsTest.o.requires

CMakeFiles/nmsTest.dir/test/nmsTest.o.provides: CMakeFiles/nmsTest.dir/test/nmsTest.o.requires
	$(MAKE) -f CMakeFiles/nmsTest.dir/build.make CMakeFiles/nmsTest.dir/test/nmsTest.o.provides.build
.PHONY : CMakeFiles/nmsTest.dir/test/nmsTest.o.provides

CMakeFiles/nmsTest.dir/test/nmsTest.o.provides.build: CMakeFiles/nmsTest.dir/test/nmsTest.o

# Object files for target nmsTest
nmsTest_OBJECTS = \
"CMakeFiles/nmsTest.dir/test/nmsTest.o"

# External object files for target nmsTest
nmsTest_EXTERNAL_OBJECTS =

../bin/nmsTest: CMakeFiles/nmsTest.dir/test/nmsTest.o
../bin/nmsTest: ../lib/libcv_utils.so
../bin/nmsTest: CMakeFiles/nmsTest.dir/build.make
../bin/nmsTest: CMakeFiles/nmsTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ../bin/nmsTest"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/nmsTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/nmsTest.dir/build: ../bin/nmsTest
.PHONY : CMakeFiles/nmsTest.dir/build

CMakeFiles/nmsTest.dir/requires: CMakeFiles/nmsTest.dir/test/nmsTest.o.requires
.PHONY : CMakeFiles/nmsTest.dir/requires

CMakeFiles/nmsTest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/nmsTest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/nmsTest.dir/clean

CMakeFiles/nmsTest.dir/depend:
	cd /home/mdesnoyer/src/reefbot/ros/cv_utils/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mdesnoyer/src/reefbot/ros/cv_utils /home/mdesnoyer/src/reefbot/ros/cv_utils /home/mdesnoyer/src/reefbot/ros/cv_utils/build /home/mdesnoyer/src/reefbot/ros/cv_utils/build /home/mdesnoyer/src/reefbot/ros/cv_utils/build/CMakeFiles/nmsTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/nmsTest.dir/depend
