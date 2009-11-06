%define 	module	iwscan
Summary:	A Python extension for iwscan access
Name:		python-%{module}
Version:	20090609
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://mirror.leaseweb.com/archlinux/other/python-iwscan/python-iwscan-%{version}.tar.gz
# Source0-md5:	30fbe8ad3b07e67c1c35db2de16077d8
URL:		http://projects.otaku42.de/browser/python-iwscan
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python
Requires:	python-modules
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to iwlist, using the iwlib library This module
makes the iwlib (Linux Wireless Extensions) functions available in
Python for wireless network scanning.

%prep
%setup -q -n %{name}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/iwscan-*.egg-info
%endif
