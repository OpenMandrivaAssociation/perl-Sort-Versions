%define upstream_version 1.61
%define upstream_name    Sort-Versions

Name:           perl-Sort-Versions
Version:        %perl_convert_version %{upstream_version}
Release:        2
License:        GPL or Artistic

Group:          Development/Perl
Summary:        A perl 5 module for sorting of revision-like numbers


Source0:        ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Sort/%{upstream_name}-%{upstream_version}.tar.gz
Url:            http://www.cpan.org
BuildRequires:  perl-devel
BuildArch:      noarch

%description 
Sort::Versions allows easy sorting of mixed non-numeric and
numeric strings, like the "version numbers" that many
shared library systems and revision control packages use.
This is quite useful if you are trying to deal with shared
libraries. It can also be applied to applications that
intersperse variable-width numeric fields within text.
Other applications can undoubtedly be found.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%clean

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*
