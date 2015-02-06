%define		_class		Net
%define		_subclass	Whois
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.5
Release:	4
Summary:	PEAR::Net_Whois class
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Whois/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The PEAR::Net_Whois looks up records in the databases maintained by
several Network Information Centers (NICs).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2012.0
+ Revision: 742170
- fix major breakage by careless packager

* Fri Aug 12 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-1
+ Revision: 694279
- 1.0.5

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 679549
- mass rebuild

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 569600
- update to new version 1.0.4

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 489155
- update to new version 1.0.2

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-3mdv2010.1
+ Revision: 468728
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 441497
- rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1.0.1-1mdv2009.1
+ Revision: 324524
- update to new version 1.0.1

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2009.1
+ Revision: 322506
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2009.0
+ Revision: 237021
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2007.0
+ Revision: 82444
- Import php-pear-Net_Whois

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package (PLD import)

