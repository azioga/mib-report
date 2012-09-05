Name:		mib-report
Version:	0.8
Release:	%mkrel 1
Summary:	A tool to generate packages reports for Rosa, MDV and MGA repos
License:	GPLv2
Group:		System/Configuration/Packaging
Url:		http://mib.pianetalinux.org/mib-report/
Source:		http://mib.pianetalinux.org/mib-report/%{name}-%{version}.tar.bz2
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

