Name:           perl-Sort-Versions
Version:        1.5
Release:        %mkrel 12
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5-11mdv2012.0
+ Revision: 765651
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5-10
+ Revision: 764157
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5-9
+ Revision: 676527
- rebuild

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.5-8
+ Revision: 658880
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5-7mdv2010.0
+ Revision: 430541
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.5-6mdv2009.0
+ Revision: 258356
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5-5mdv2009.0
+ Revision: 246417
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2008.1
+ Revision: 121760
- kill (multiple!) definitions of %%buildroot on Pixel's request


* Sat Jan 13 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5-3mdv2007.0
+ Revision: 108394
- rebuild
- Import perl-Sort-Versions

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.5-2mdk
- rebuild for new perl

* Wed Dec 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5-1mdk
- 1.5

