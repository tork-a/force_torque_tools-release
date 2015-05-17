Name:           ros-jade-force-torque-sensor-calib
Version:        1.0.1
Release:        0%{?dist}
Summary:        ROS force_torque_sensor_calib package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/force_torque_sensor_calib
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-cmake-modules
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-moveit-core
Requires:       ros-jade-moveit-ros-planning
Requires:       ros-jade-moveit-ros-planning-interface
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-moveit-core
BuildRequires:  ros-jade-moveit-ros-planning
BuildRequires:  ros-jade-moveit-ros-planning-interface
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions

%description
Calibrates the offsets of F/T sensors and the mass and position of the COM of
gripper attached to the F/T sensor. Uses readings from an accelerometer that has
been calibrated to the robot frame.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun May 17 2015 Francisco Vina <fevb@kth.se> - 1.0.1-0
- Autogenerated by Bloom

