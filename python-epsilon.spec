%define module  epsilon
%define name    python-%{module}
%define version 0.6.0
%define release %mkrel 1

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
