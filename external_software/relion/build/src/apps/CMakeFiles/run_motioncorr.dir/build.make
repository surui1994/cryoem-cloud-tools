# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


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
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /usr/local/relion

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr/local/relion/build

# Include any dependencies generated for this target.
include src/apps/CMakeFiles/run_motioncorr.dir/depend.make

# Include the progress variables for this target.
include src/apps/CMakeFiles/run_motioncorr.dir/progress.make

# Include the compile flags for this target's objects.
include src/apps/CMakeFiles/run_motioncorr.dir/flags.make

src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o: src/apps/CMakeFiles/run_motioncorr.dir/flags.make
src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o: ../src/apps/run_motioncorr.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/usr/local/relion/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o"
	cd /usr/local/relion/build/src/apps && /usr/local/bin/mpicxx  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o -c /usr/local/relion/src/apps/run_motioncorr.cpp

src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.i"
	cd /usr/local/relion/build/src/apps && /usr/local/bin/mpicxx $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /usr/local/relion/src/apps/run_motioncorr.cpp > CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.i

src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.s"
	cd /usr/local/relion/build/src/apps && /usr/local/bin/mpicxx $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /usr/local/relion/src/apps/run_motioncorr.cpp -o CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.s

src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.requires:

.PHONY : src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.requires

src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.provides: src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.requires
	$(MAKE) -f src/apps/CMakeFiles/run_motioncorr.dir/build.make src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.provides.build
.PHONY : src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.provides

src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.provides.build: src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o


# Object files for target run_motioncorr
run_motioncorr_OBJECTS = \
"CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o"

# External object files for target run_motioncorr
run_motioncorr_EXTERNAL_OBJECTS =

bin/relion_run_motioncorr: src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o
bin/relion_run_motioncorr: src/apps/CMakeFiles/run_motioncorr.dir/build.make
bin/relion_run_motioncorr: lib/librelion_lib.dylib
bin/relion_run_motioncorr: ../external/fftw/lib/libfftw3.dylib
bin/relion_run_motioncorr: /usr/local/lib/libmpi.dylib
bin/relion_run_motioncorr: ../external/fltk/lib/libfltk.dylib
bin/relion_run_motioncorr: src/apps/CMakeFiles/run_motioncorr.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/usr/local/relion/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/relion_run_motioncorr"
	cd /usr/local/relion/build/src/apps && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/run_motioncorr.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/apps/CMakeFiles/run_motioncorr.dir/build: bin/relion_run_motioncorr

.PHONY : src/apps/CMakeFiles/run_motioncorr.dir/build

src/apps/CMakeFiles/run_motioncorr.dir/requires: src/apps/CMakeFiles/run_motioncorr.dir/run_motioncorr.cpp.o.requires

.PHONY : src/apps/CMakeFiles/run_motioncorr.dir/requires

src/apps/CMakeFiles/run_motioncorr.dir/clean:
	cd /usr/local/relion/build/src/apps && $(CMAKE_COMMAND) -P CMakeFiles/run_motioncorr.dir/cmake_clean.cmake
.PHONY : src/apps/CMakeFiles/run_motioncorr.dir/clean

src/apps/CMakeFiles/run_motioncorr.dir/depend:
	cd /usr/local/relion/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/local/relion /usr/local/relion/src/apps /usr/local/relion/build /usr/local/relion/build/src/apps /usr/local/relion/build/src/apps/CMakeFiles/run_motioncorr.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/apps/CMakeFiles/run_motioncorr.dir/depend
