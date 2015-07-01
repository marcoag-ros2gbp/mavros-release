Name:           ros-indigo-mavros-extras
Version:        0.12.0
Release:        0%{?dist}
Summary:        ROS mavros_extras package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       python
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-mavlink
Requires:       ros-indigo-mavros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-mavlink
BuildRequires:  ros-indigo-mavros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
Extra nodes and plugins for mavros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jul 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.12.0-0
- Autogenerated by Bloom

* Sun Apr 26 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue Mar 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.0-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.1-0
- Autogenerated by Bloom

* Sat Jan 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.0-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.9.4-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.9.3-0
- Autogenerated by Bloom

