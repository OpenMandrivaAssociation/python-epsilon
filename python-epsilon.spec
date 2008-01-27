Name: python-epsilon
Summary: A small utility package
Version: 0.2.1
Release: %mkrel 1
Group: Development/Python 
URL: http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0: Epsilon-%{version}.tar.gz
License: BSD
Provides: python-ConfigObj = %version
Provides: ConfigObj = %version
%py_requires

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file round tripper. Its main feature is that it is very easy to use, with a straightforward programmer's interface and a simple syntax for config files. 

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

