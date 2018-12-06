#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Exporter-Progressive
Version  : 0.001013
Release  : 10
URL      : http://search.cpan.org/CPAN/authors/id/F/FR/FREW/Sub-Exporter-Progressive-0.001013.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/F/FR/FREW/Sub-Exporter-Progressive-0.001013.tar.gz
Summary  : 'Only use Sub::Exporter if you need it'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Exporter-Progressive-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
SYNOPSIS
package Syntax::Keyword::Gather;

use Sub::Exporter::Progressive -setup => {
exports => [qw( break gather gathered take )],
groups => {
default => [qw( break gather gathered take )],
},
};

# elsewhere

# uses Exporter for speed
use Syntax::Keyword::Gather;

# somewhere else

# uses Sub::Exporter for features
use Syntax::Keyword::Gather 'gather', take => { -as => 'grab' };

%package dev
Summary: dev components for the perl-Sub-Exporter-Progressive package.
Group: Development
Provides: perl-Sub-Exporter-Progressive-devel = %{version}-%{release}

%description dev
dev components for the perl-Sub-Exporter-Progressive package.


%package license
Summary: license components for the perl-Sub-Exporter-Progressive package.
Group: Default

%description license
license components for the perl-Sub-Exporter-Progressive package.


%prep
%setup -q -n Sub-Exporter-Progressive-0.001013

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter-Progressive
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter-Progressive/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Sub/Exporter/Progressive.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Exporter::Progressive.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Exporter-Progressive/LICENSE
