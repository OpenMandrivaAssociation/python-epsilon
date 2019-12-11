%define module  epsilon

Summary:	A small utility package

Name:		python-%{module}
Version:	0.7.3
Release:	8
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0:	https://files.pythonhosted.org/packages/de/5b/7dde11d1462bd0780e518f885d32f9b13c8a8f2046a4c9f63e5c4243b9e9/Epsilon-0.7.3.tar.gz
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
%setup -qn Epsilon-%{version}

%build
find . -name "*.py" -exec 2to3 -w {} \;
%py_build

%install
%py_install

rm -rf %{buildroot}%{py2_puresitedir}/build

%files
%{py_puresitedir}/*
%{_bindir}/*

