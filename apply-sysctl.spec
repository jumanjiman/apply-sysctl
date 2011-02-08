Name:		apply-sysctl
Version:	0.1
Release:	1%{?dist}
Summary:	Apply kernel tunables from files other than sysctl.conf

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/jumanjiman/apply-sysctl
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	util-linux
Requires:	grep

%description
Provides a script and sample config file for setting
kernel tunables outside of /etc/sysctl.conf.

Use case: package "foo" provides /etc/foo/sysctl.conf
and an init script that calls "apply-sysctl /etc/foo/sysctl.conf"
at boot-time. This keeps sysctl.conf clean while
keeping the output of "rpm -V foo" clean.


%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{_sbindir}
%{__install} -pm 755 src/apply-sysctl %{buildroot}/%{_sbindir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.GPLv3
%doc src/sample-sysctl.conf
%{_sbindir}/apply-sysctl



%changelog

