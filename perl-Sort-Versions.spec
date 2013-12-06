%define modname	Sort-Versions

Summary:	A perl 5 module for sorting of revision-like numbers
Name:		perl-%{modname}
Version:	1.5
Release:	13
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sort/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description 
Sort::Versions allows easy sorting of mixed non-numeric and
numeric strings, like the "version numbers" that many
shared library systems and revision control packages use.
This is quite useful if you are trying to deal with shared
libraries. It can also be applied to applications that
intersperse variable-width numeric fields within text.
Other applications can undoubtedly be found.

%prep
%setup -qn %{modname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

