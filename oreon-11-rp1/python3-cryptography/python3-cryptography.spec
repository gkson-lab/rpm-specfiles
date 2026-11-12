# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b46165bb56eb4704e2eaaf86f3c940d19154535d9b0ca7d6d590b04060e00d5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-cryptography
Version: 50.0.2
Release: 1%{?dist}
Summary: Cryptographic recipes and primitives
License: Apache-2.0
URL: https://pypi.org/project/cryptography/
Source0: https://files.pythonhosted.org/packages/9d/af/182eb91b0df3fe75c4d9f26fe70684569566745f6ba7e5c9c73a862c5252/cryptography-50.0.2.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-maturin
BuildRequires: python3-cffi
BuildRequires: openssl-devel
BuildRequires: gcc
BuildRequires: rust
BuildRequires: cargo
Requires: python3
Requires: python3-cffi

%description
Cryptographic recipes and primitives

%prep
%oreon_sha256
%autosetup -n cryptography-50.0.2

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import cryptography'

%files -f %{_builddir}/%{name}.files
