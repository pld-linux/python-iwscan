%define 	module	iwscan
%define		snap	20090609
%define		rel	5
Summary:	A Python extension for iwscan access
Name:		python-%{module}
Version:	0.7.0
Release:	0.%{snap}.%{rel}
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://mirror.leaseweb.com/archlinux/other/python-iwscan/%{name}-%{snap}.tar.gz
# Source0-md5:	30fbe8ad3b07e67c1c35db2de16077d8
Patch0:		missing-def.patch
URL:		http://projects.otaku42.de/browser/python-iwscan
BuildRequires:	libiw-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to iwlist, using the iwlib library.

This module makes the iwlib (Linux Wireless Extensions) functions
available in Python for wireless network scanning.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc iwlist.py
%attr(755,root,root) %{py_sitedir}/%{module}.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
