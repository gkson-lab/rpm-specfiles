# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash db2100058c50784c3d24984920ceefe61b951e915cb483ffafa116fdfc18cea2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-vcsgraph
Version: 0.3.3
Release: 1%{?dist}
Summary: Graph algorithms for version control systems
License: MIT
URL: https://pypi.org/project/vcsgraph/
Source0: https://files.pythonhosted.org/packages/ee/03/5cdc1f74eff7a8532c1f28a789dddfa0984f5f392c08d67e96608c557639/vcsgraph-0.3.3.tar.gz

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
Graph algorithms for version control systems

%prep
%oreon_sha256
%autosetup -n vcsgraph-0.3.3

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import vcsgraph'

%files -f %{_builddir}/%{name}.files
