%define module  epsilon
%define name    python-%{module}
%define version 0.6.0
%define release 5

Name: 		%{name}
Summary: 	A small utility package
Version: 	%{version}
Release: 	%{release}
Group: 		Development/Python 
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0: 	Epsilon-%{version}.tar.gz
License: 	BSD
Provides: 	python-Epsilon = %{version}
Provides: 	Epsilon = %version
Requires:	python-twisted
BuildRequires:	python-devel python-twisted
BuildArch:	noarch

%description
A small utility package that depends on tools too recent for Twisted (like
datetime in python2.4) but performs generic enough functions that it can be
used in projects that don't want to share the large footprint of Divmod's 
other projects.

%prep
%setup -q -n Epsilon-%version

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp
%__grep -v %{py_sitedir}/build INSTALLED_FILES.tmp > INSTALLED_FILES

%__rm -rf %{buildroot}%{py_sitedir}/build

%clean
%__rm -rf %buildroot

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README *.txt LICENSE


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2011.0
+ Revision: 667931
- mass rebuild

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 592308
- update to 0.6.0
- replace the obsolete %%py_requires macro with BR python-devel

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.11-3mdv2010.1
+ Revision: 523765
- rebuilt for 2010.1

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 0.5.11-2mdv2009.1
+ Revision: 319238
- rebuild for new python

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.11-1mdv2009.1
+ Revision: 318716
- rebuild for python 2.6
- new release 0.5.11

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.5.9-2mdv2009.0
+ Revision: 265541
- rebuild early 2009.0 package (before pixel changes)

* Wed Mar 19 2008 Lev Givon <lev@mandriva.org> 0.5.9-1mdv2009.0
+ Revision: 188906
- Update to 0.5.9.
  Don't install build files.
- Build as noarch package.
  Include license.

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - fix description-line-too-long

* Mon Jan 28 2008 Erwan Velu <erwan@mandriva.org> 0.5.8-1mdv2008.1
+ Revision: 159481
- Fixing missing buildrequires
- Fixing typo
- 0.5.8
- 0.5.8 (needed by python-axiom)

* Sun Jan 27 2008 Helio Chissini de Castro <helio@mandriva.com> 0.2.1-1mdv2008.1
+ Revision: 158802
- Fix the mess on provides and description
- import python-epsilon


* Sun Jan 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1.1-1mdv2008.1
- First release for Mandriva.

