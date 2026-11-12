# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a0d403f3122aae24d34d2682665e505925bba7a6d3246da482b7a2a9cdcea8fe
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-fastbencode
Version: 0.3.12
Release: 1%{?dist}
Summary: Implementation of bencode with optional fast Rust extensions
License: MIT
URL: https://pypi.org/project/fastbencode/
Source0: https://files.pythonhosted.org/packages/ac/be/21ea2218a70d634a32cd1c8be2c11624cfcfeaeec14016f04187a394f6b1/fastbencode-0.3.12.tar.gz

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
Implementation of bencode with optional fast Rust extensions

%prep
%oreon_sha256
%autosetup -n fastbencode-0.3.12

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import fastbencode'

%files -f %{_builddir}/%{name}.files
