# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 49030d92d2575da735791b496dc322f3ce5cff9494779ba8cc28c7f46c5deb32
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: apr
Version: 1.7.6
Release: 1%{?dist}
Summary: Apache Portable Runtime library
License: Apache-2.0
URL: https://apr.apache.org/
Source0: https://archive.apache.org/dist/apr/apr-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: libuuid-devel

%description
Apache Portable Runtime library.

%package devel
Summary: Development files for apr
Requires: apr%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for building against apr.

%prep
%oreon_sha256
%autosetup -n apr-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libapr-1.la
%oreon_filelist_devel

%check
make check

%files -f %{_builddir}/%{name}.files
%files devel -f %{_builddir}/%{name}-devel.files
