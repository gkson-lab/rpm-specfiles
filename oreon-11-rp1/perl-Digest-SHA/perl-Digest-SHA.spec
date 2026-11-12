# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ee91f8f7db894ee7c6ee003daac10a99056c4948a674ef46acdbb63c81a4abeb
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: perl-Digest-SHA
Version: 6.04
Release: 1%{?dist}
Summary: Perl interface to SHA-1/224/256/384/512
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/Digest-SHA
Source0: https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: perl-interpreter
Requires: perl-interpreter
Provides: perl(Digest::SHA) = %{version}

%description
Perl module for SHA digests.

%prep
%oreon_sha256
%autosetup -n Digest-SHA-%{version}

%build

%install
mkdir -p %{buildroot}%{perl_vendorlib}/Digest
install -p -m 0644 lib/Digest/SHA.pm %{buildroot}%{perl_vendorlib}/Digest/SHA.pm

%check
perl -Ilib -MDigest::SHA -e 'Digest::SHA->new(256)->add("oreon")->hexdigest'

%files
%license LICENSE
%{perl_vendorlib}/Digest/SHA.pm
