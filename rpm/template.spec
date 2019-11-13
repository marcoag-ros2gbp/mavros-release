%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-mavros-extras
Version:        0.33.3
Release:        1%{?dist}
Summary:        ROS mavros_extras package

License:        GPLv3
URL:            http://wiki.ros.org/mavros_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-mavros
Requires:       ros-melodic-mavros-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf2-eigen
Requires:       ros-melodic-urdf
Requires:       ros-melodic-visualization-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-mavros
BuildRequires:  ros-melodic-mavros-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf2-eigen
BuildRequires:  ros-melodic-urdf
BuildRequires:  ros-melodic-visualization-msgs

%description
Extra nodes and plugins for MAVROS.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Wed Nov 13 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.33.3-1
- Autogenerated by Bloom

* Mon Nov 11 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.33.1-1
- Autogenerated by Bloom

* Thu Oct 10 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.33.0-1
- Autogenerated by Bloom

* Mon Sep 09 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.32.2-1
- Autogenerated by Bloom

* Thu Aug 08 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.32.1-1
- Autogenerated by Bloom

* Sat Jul 06 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.32.0-1
- Autogenerated by Bloom

* Fri Jun 07 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.31.0-1
- Autogenerated by Bloom

* Mon May 20 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.30.0-1
- Autogenerated by Bloom

* Wed Mar 06 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.29.2-0
- Autogenerated by Bloom

* Sun Mar 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.29.1-0
- Autogenerated by Bloom

* Sat Feb 02 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.29.0-0
- Autogenerated by Bloom

* Thu Jan 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 0.28.0-0
- Autogenerated by Bloom

* Mon Nov 12 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.27.0-0
- Autogenerated by Bloom

* Sat Nov 10 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.3-1
- Autogenerated by Bloom

* Tue Aug 21 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.3-0
- Autogenerated by Bloom

* Wed Aug 08 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.2-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.1-0
- Autogenerated by Bloom

* Wed Jun 06 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.26.0-0
- Autogenerated by Bloom

* Mon May 14 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.1-0
- Autogenerated by Bloom

* Fri May 11 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.25.0-0
- Autogenerated by Bloom

* Mon May 07 2018 Vladimir Ermakov <vooon341@gmail.com> - 0.24.0-0
- Autogenerated by Bloom

