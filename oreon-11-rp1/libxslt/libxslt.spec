# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5a3d6b383ca5afc235b171118e90f5ff6aa27e9fea3303065231a6d403f0183a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libxslt
Version: 1.1.43
Release: 1%{?dist}
Summary: Library for transforming XML with XSLT
License: MIT
URL: https://gitlab.gnome.org/GNOME/libxslt
Source0: https://download.gnome.org/sources/libxslt/1.1/libxslt-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(libxml-2.0)

%description
libxslt applies XSLT stylesheets to XML documents. xsltproc is the command line tool.

%package devel
Summary: Development files for libxslt
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libxml2-devel%{?_isa}

%description devel
Headers and pkgconfig files for libxslt.

%prep
%oreon_sha256
%autosetup -n libxslt-%{version}

%build
%configure --disable-static --without-python --without-crypto
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -name '*.a' -delete

%check
%make_build check

%files
%license Copyright
%{_bindir}/xsltproc
%{_libdir}/libxslt.so.1*
%{_libdir}/libexslt.so.0*
%{_libdir}/libxslt-plugins
%{_mandir}/man1/xsltproc.1*

%files devel
%{_includedir}/libxslt/
%{_includedir}/libexslt/
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_mandir}/man3/*
