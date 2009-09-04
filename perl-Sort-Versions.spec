Name:           perl-Sort-Versions
Version:        1.5
Release:        %mkrel 7
License:        GPL or Artistic

%define realname        Sort-Versions
Group:          Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:        A perl 5 module for sorting of revision-like numbers
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sort/%{realname}-%{version}.tar.bz2
Url:            http://www.cpan.org
Prefix:         %{_prefix}
BuildRequires:  perl-devel
Requires:       perl >= 5.002
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
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*


