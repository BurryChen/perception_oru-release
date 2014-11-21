Name:           ros-hydro-ndt-registration
Version:        1.0.22
Release:        0%{?dist}
Summary:        ROS ndt_registration package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ndt_registration
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl-devel
Requires:       ros-hydro-ndt-map
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-tf
Requires:       ros-hydro-tf-conversions
BuildRequires:  pcl-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-ndt-map
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf-conversions

%description
Contains a new implementation of 3D NDT registration. Used to find the relative
positions of two point clouds.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Nov 21 2014 Todor Stoyanov <todor.stoyanov@oru.se> - 1.0.22-0
- Autogenerated by Bloom

