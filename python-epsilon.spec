%define module  epsilon

Summary:	A small utility package

Name:		python-%{module}
Version:	0.8.0
Release:	4
Group:		Development/Python 
License:	BSD
Url:		https://www.divmod.org/trac/wiki/DivmodEpsilon
Source0:	https://pypi.python.org/packages/source/e/epsilon/epsilon-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-twisted
BuildRequires:	python-pip
Provides:	python-Epsilon = %{version}
Provides:	Epsilon = %{version}
Requires:	python-twisted

%description
A small utility package that depends on tools too recent for Twisted (like
datetime in python2.4) but performs generic enough functions that it can be
used in projects that don't want to share the large footprint of Divmod's 
other projects.

%prep
%autosetup -p1 -n epsilon-%{version}
find . -name "*.py" -exec 2to3 -w {} \;

%build
%py_build

%install
%py_install

rm -rf %{buildroot}%{py_puresitedir}/build

%files
%{py_puresitedir}/*
%{_bindir}/*
