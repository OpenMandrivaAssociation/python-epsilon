%define module  epsilon

Summary:	A small utility package

Name:		python-%{module}
Version:	0.7.0
Release:	3
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0:	https://pypi.python.org/packages/source/E/Epsilon/Epsilon-%{version}.tar.gz
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
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp

rm -rf %{buildroot}%{py_puresitedir}/build

%files
%doc README *.txt LICENSE
%{py_puresitedir}/*
%{_bindir}/*

