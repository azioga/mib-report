Name:		mib-report
Version:	0.8
Release:	%mkrel 2
Summary:	A tool to generate packages reports for Rosa, MDV and MGA repos
License:	GPLv2
Group:		System/Configuration/Packaging
Url:		http://mib.pianetalinux.org/mib-report/
Source:		http://mib.pianetalinux.org/mib-report/%{name}-%{version}.tar.bz2
Patch0:		mib-report-0.8-rpm5.patch
BuildRequires:	qt4-devel
BuildRequires:	rpm-devel
Requires:	lynx
Requires:	curl

%description
A tool to generate packages reports and check package versions.

Since 0.8 it supports 4 report modes:
1) mga-mdv - report for packages in Mageia repositories that may be interesting
for Mandriva packagers
2) mdv-mga - like mga-mdv but for Mageia packagers (by request)
3) mdv-rosa
4) rosa-mdv

It produces a table with packages and shows if there are newer versions of
these packages in other distros. It also gives quick links for source packages
and programs' homepages.

Since 0.4 new mode "--search package" was added. It searches for package in all
reference repositories and displays results in Repository, Version, URL format.

Version %{version} supports reference repositories:
-Rosa 2012.1
-MDV Cooker
-Mageia Cauldron
-PCLinuxOS
-OpenSUSE Factory
-Alt Linux Sisyphus
-Fedora Rawhide (+RpmFusion)
-Debian
-Ubuntu
-Gentoo

%prep
%setup -q
%if %{mdvver} >= 201100
%patch0 -p1
%endif

%build
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
%__install -D -m 755 mdv-locate %{buildroot}%{_bindir}/mdv-locate
%__install -D -m 755 urls-fetcher %{buildroot}%{_bindir}/urls-fetcher
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__install -D -m 644 urls.txt %{buildroot}%{_datadir}/%{name}/urls.txt
%__install -D -m 644 blacklist.txt %{buildroot}%{_datadir}/%{name}/blacklist.txt

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING AUTHORS ChangeLog
%{_bindir}/%{name}
%{_bindir}/mdv-locate
%{_bindir}/urls-fetcher
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/urls.txt
%{_datadir}/%{name}/blacklist.txt



%changelog
* Sat Sep 08 2012 Andrey Bondrov <abondrov@mandriva.org> 0.8-2mdv2012.0
+ Revision: 816558
- Just rebuild
- Add patch to fix build with RPM5
- Add rpm-devel to BuildRequires and fix summary
- Fix group once again
- New version 0.8 with support for Rosa 2012.1 repositories and MDV vs ROSA reports, drop support for old community repositories and reports

* Thu Feb 02 2012 Andrey Bondrov <abondrov@mandriva.org> 0.7-1
+ Revision: 770665
- imported package mib-report


* Thu Feb 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.7-1mib2010.2
- New report mode - MDV vs MGA (by Mageia ppl request)
- Fix Fedora packages list fetching (Rawhide repository structure changed)
- Show package's homepage URL in search mode
- Add urls-fetcher utility that generates up to date urls.txt file
- Update blacklist.txt

* Thu Nov 24 2011 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.6-69.1mib2010.2
- Add MRB 2010.2 and 2011 to reference repositories
- Add EduMandriva 2010.2 and 2011 to reference repositories
- Add Ubuntu to reference repositories
- New mdv-locate utility to check package versions in the official repositories

* Sun Oct 02 2011 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.5-69.1mib2010.2
- Package names in reports are now links to package homepages
- New report mode - MGA vs MDV
- Change usage (--report table mode)
- Downloading repositories data speedup (about 2 times less traffic)
- Add RpmFusion to Fedora's repositories
- Add PCLinuxOS Main repository (useful in --search mode)

* Thu Sep 22 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.4-69.2mib2010.2
- Use better mirror for MDV Cooker

* Thu Sep 22 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.4-69.1mib2010.2
- New version
- Drop PLF repository support, use Restricted instead
- Change usage (add --report, --version, --help, --search options)
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Sat Sep 03 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.3-69.1mib2010.2
- New version
- New MIB repo supported in 0.3: 2011.0
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Fri Jul 15 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.2-69.1mib2010.2
- New version
- New reference distributions supported in 0.2: PCLinuxOS, Mageia, OpenSUSE
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Wed Jul 13 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.1-69.2mib2010.2
- Change Gentoo mirror
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Wed May 25 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.1-69.1mib2010.2
- First release
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/
