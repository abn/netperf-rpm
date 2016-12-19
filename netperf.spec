Summary:       Network Performance Testing Tool
Name:          netperf
Version:       2.7.0
Release:       1

Group:         System Environment/Base
License:       Unknown
URL:           http://www.netperf.org/
Source:        ftp://ftp.netperf.org/netperf/%{name}-%{version}.tar.bz2

BuildRequires: gcc texinfo, texinfo-tex
BuildRequires: libsmbios-devel 
BuildRequires: lksctp-tools-devel

%description
Many different network benchmarking tools are collected in this package,
maintained by Rick Jones of HP.

%prep
%setup -q

%build
# gcc 4.4 users may want to disable the strict aliasing warnings
# CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"
%configure --enable-sctp
make  %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}

# Convert the main netperf document to other formats
cd doc
make %{name}.txt %{name}.html %{name}.xml pdf
cd ..

# We don't want to package the Makefile files in the examples directory
rm -f doc/examples/Makefile*

# Info
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

# %post

%files
%doc README AUTHORS COPYING Release_Notes
%doc doc/netperf.{html,pdf,txt,xml}
%doc doc/examples
%{_mandir}/man1/*
%{_infodir}/*
%{_bindir}/netperf
%{_bindir}/netserver


%changelog
* Mon Dec 19 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 2.7.0-1
- upgrade to v2.7.0

* Mon Sep  7 2009 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.4.5-1
- Specfile cleanup.

* Sat Jun 17 2006 Martin A. Brown <martin@linux-ip.net> - 2.4.2-1
- initial contributed specfile for netperf package (v2.4.2)
