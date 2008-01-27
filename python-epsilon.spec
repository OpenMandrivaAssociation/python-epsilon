Name: python-epsilon
Summary: A small utility package
Version: 0.2.1
Release: %mkrel 1
Group: Development/Python 
URL: http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0: Epsilon-%{version}.tar.gz
License: BSD
Provides: python-Epsilon = %version
Provides: Epsilon = %version
%py_requires -d

%description
A small utility package that depends on tools too recent for Twisted (like datetime in python2.4) but performs generic enough functions that it can be used in projects that don't want to share Divmod's other projects' large footprint. 
'
%files
%defattr(-,root,root)
%py_platsitedir/*

#------------------------------------------------------------

%prep
%setup -q -n Epsilon-%version

%build
python setup.py build

%install
rm -rf %buildroot

python setup.py install --root=%buildroot --install-lib=%py_platsitedir

%clean
rm -rf %buildroot

