# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bfeca9984ba88fd36745b64e1271a52b407a2919ecdd6aee850d0374a16e3457
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-patiencediff
Version: 1.0.2
Release: 1%{?dist}
Summary: Python implementation of the patiencediff algorithm
License: MIT
URL: https://pypi.org/project/patiencediff/
Source0: https://files.pythonhosted.org/packages/bd/ca/7d530d7bf5e3094f86a67b9698045ccb86fc122f2ed024472ee9f6dc55c6/patiencediff-1.0.2.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust
BuildRequires: rust
BuildRequires: cargo
BuildRequires: gcc
Requires: python3

%description
Python implementation of the patiencediff algorithm

%prep
%oreon_sha256
%autosetup -n patiencediff-1.0.2

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import patiencediff'

%files -f %{_builddir}/%{name}.files
