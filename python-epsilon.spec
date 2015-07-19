%define module  epsilon

Summary:	A small utility package

Name:		python-%{module}
Version:	0.7.0
Release:	6
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0:	https://pypi.python.org/packages/source/E/Epsilon/Epsilon-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-twisted
Provides:	python-Epsilon = %{version}
Provides:	Epsilon = %{version}
Requires:	python2-twisted

%description
A small utility package that depends on tools too recent for Twisted (like
datetime in python2.4) but performs generic enough functions that it can be
used in projects that don't want to share the large footprint of Divmod's 
other projects.

%prep
%setup -qn Epsilon-%{version}

%build
%__python2 setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp

rm -rf %{buildroot}%{py2_puresitedir}/build

%files
%doc README *.txt LICENSE
%{py2_puresitedir}/*
%{_bindir}/*

