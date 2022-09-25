%define module  epsilon

Summary:	A small utility package

Name:		python-%{module}
Version:	0.8.0
Release:	1
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0:	https://pypi.python.org/packages/source/e/epsilon/epsilon-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-twisted
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

%build
find . -name "*.py" -exec 2to3 -w {} \;
%py_build

%install
%py_install

rm -rf %{buildroot}%{py_puresitedir}/build

%files
%{py_puresitedir}/*
%{_bindir}/*
