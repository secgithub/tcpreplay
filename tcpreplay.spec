Summary: A tool to replay captured network traffic.
Name: tcpreplay
Version: 1.3-beta4
Release: 1
Copyright: BSD
Group: Applications/Internet
Source0: http://prdownloads.sf.net/tcpreplay/tcpreplay-%{version}.tar.gz
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-root
Packager: Aaron Turner <aturner@pobox.com>
Requires: libnet >= 1.0.2
BuildPreReq: libnet >= 1.0.2
URL: http://tcpreplay.sf.net/

# set to 1 to enable debugging
%define enable_debug 0

%description
Tcpreplay is a tool to replay captured network traffic.  Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats.  Also included, is tcpprep
a tool to pre-process capture files to allow increased performance under
certain conditions as well as capinfo which provides basic information about
capture files.

%prep
%setup -q

%build
%if %{enable_debug}
./configure --with-debug
%else
./configure
%endif
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m755 tcpreplay $RPM_BUILD_ROOT%{_sbindir} 
install -m755 tcpprep $RPM_BUILD_ROOT%{_bindir} 
install -m755 capinfo $RPM_BUILD_ROOT%{_bindir}
install -m644 tcpreplay.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m644 tcpprep.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m644 capinfo.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc	CHANGELOG LICENSE tcpprep.FAQ README
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man8/*
%{_mandir}/man1/*


%changelog
* Fri Jun 28 2002 Aaron Turner <aturner@pobox.com>
- Initial packaging
