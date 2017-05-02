#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Exporter-Progressive
Version  : 0.001013
Release  : 3
URL      : http://search.cpan.org/CPAN/authors/id/F/FR/FREW/Sub-Exporter-Progressive-0.001013.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/F/FR/FREW/Sub-Exporter-Progressive-0.001013.tar.gz
Summary  : 'Only use Sub::Exporter if you need it'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Exporter-Progressive-doc

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

%package doc
Summary: doc components for the perl-Sub-Exporter-Progressive package.
Group: Documentation

%description doc
doc components for the perl-Sub-Exporter-Progressive package.


%prep
%setup -q -n Sub-Exporter-Progressive-0.001013

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Sub/Exporter/Progressive.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
