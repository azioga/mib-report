Summary:	A tool to generate packages reports for Rosa, MDV and MGA repos
Name:		mib-report
Version:	0.11
Release:	2
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://mib.pianetalinux.org/mib-report/
Source0:	http://mib.pianetalinux.org/mib-report/%{name}-%{version}.tar.bz2
# bash-completion
Source1:	%{name}
Patch0:		mib-report-0.9-rpm4.patch
# Qt5 is also supported
BuildRequires:	qt4-devel
BuildRequires:	rpm-devel
Requires:	lynx
Requires:	curl

%description
A tool to generate packages reports and check package versions.

Since 0.9 it supports 6 report modes:
1) mga-mdv - report for packages in Mageia repositories that may be interesting
for Mandriva packagers
2) mdv-mga - like mga-mdv but for Mageia packagers (by request)
3) mdv-rosa
4) rosa-mdv
5) mga-rosa
6) rosa-mga

It produces a table with packages and shows if there are newer versions of
these packages in other distros. It also gives quick links for source packages
and programs' homepages.

Since 0.4 new mode "--search package" was added. It searches for package in all
reference repositories and displays results in Repository, Version, URL format.

Version %{version} supports reference repositories:
-Rosa 2014.1
-MDV Cooker
-Mageia Cauldron
-Fedora Rawhide (+RpmFusion)
-PCLinuxOS
-Alt Linux Sisyphus
-OpenSUSE Factory
-PLD Linux 3.0
-Gentoo
-Debian
-Ubuntu
-Upstream Tracker

%files
%doc COPYING AUTHORS ChangeLog
%{_bindir}/%{name}
%{_bindir}/urls-fetcher
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/urls.txt
%{_datadir}/%{name}/blacklist.txt
%{_datadir}/bash-completion/completions/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q
%if %{mdvver} < 201100
%patch0 -p1
%endif

%build
# Can be built with Qt5 if needed
%qmake_qt4
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 755 urls-fetcher %{buildroot}%{_bindir}/urls-fetcher
mkdir -p %{buildroot}%{_datadir}/%{name}
install -D -m 644 urls.txt %{buildroot}%{_datadir}/%{name}/urls.txt
install -D -m 644 blacklist.txt %{buildroot}%{_datadir}/%{name}/blacklist.txt

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%changelog
* Mon May 26 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.11-2
- Add bash-completion

* Sun May 25 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.11-1
- Switch from Rosa 2012.1 to 2014.1 which is now current branch
- Add PLD Linux to reference repositories
- Fix encoding issues with Qt4
- Update urls.txt

* Thu Jul 25 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.10-1
- Add support for Upsteam Tracker repository
- Fix URL for PCLinuxOS repository
- Fix build with Qt5
- Fix urls-fetcher utility
- Drop no longer needed mdv-locate utility
- Update urls.txt

* Tue Jan 08 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.9-1
- Add Rosa vs MGA and MGA vs Rosa reports
- Update URLs for Cooker repositories (as Cooker moved to ABF)
- Fix URLs for Fedora's RPM Fusion repositories
- Update urls.txt

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
