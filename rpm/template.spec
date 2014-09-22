Name:           ros-indigo-mavros
Version:        0.8.0
Release:        0%{?dist}
Summary:        ROS mavros package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-angles
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mavlink
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mavlink
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf

%description
MAVROS -- MAVLink extendable communication node for ROS with UDP proxy for
Ground Control Station.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 22 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.8.0-0
- Autogenerated by Bloom

* Tue Aug 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.7.0-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.7.1-0
- Autogenerated by Bloom

