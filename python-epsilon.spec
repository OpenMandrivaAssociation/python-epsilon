%define module  epsilon

Summary:	A small utility package

Name:		python-%{module}
Version:	0.8.0
Release:	5
Group:		Development/Python 
License:	MIT
Url:		https://www.divmod.org/trac/wiki/DivmodEpsilon
Source0:	https://pypi.python.org/packages/source/e/epsilon/epsilon-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-twisted
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
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
# Python 3.15 has no 2to3. The library is already Python 3; rewrite the
# few calls 2to3 used to fix.
sed -i 's/unicode(/str(/' epsilon/caseless.py
sed -i 's/\.iteritems()/.items()/' epsilon/spewer.py epsilon/hotfixes/delayedcall_seconds.py
sed -i "s/d.has_key('statinfo')/'statinfo' in d/" epsilon/hotfixes/filepath_copyTo.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_build

%install
%py_install

rm -rf %{buildroot}%{py_puresitedir}/build

%files
%{py_puresitedir}/*
%{_bindir}/*
