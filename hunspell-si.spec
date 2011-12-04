Name: hunspell-si
Summary: Sinhala hunspell dictionaries
Version: 0.2.1
Release: 2%{?dist}
Source: http://www.sandaru1.com/wp-content/uploads/2009/08/si-LK.tar.gz
Group: Applications/Text
URL: http://www.sandaru1.com/2009/08/29/sinhala-spell-checker-for-firefox/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
Requires: hunspell

%description
Sinhala hunspell dictionaries.

%prep
%setup -q -c -n hunspell-si

%build
#nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/si-LK.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/si_LK.aff
cp -p dictionaries/si-LK.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/si_LK.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_datadir}/myspell/*

%changelog
* Thu Feb 25 2010 Parag Nemade <pnemade AT redhat.com> - 0.2.1-2
- Resolves: rh#567895: Fix license tag in spec file with new upstream release
- Removed CREDITS file as upstream provides now README and LICENSE files.

* Wed Feb 24 2010 Parag Nemade <pnemade AT redhat.com> - 0.2.1-1
- Resolves: rh#567895: Fix license tag in spec file with new upstream release

* Wed Jan 27 2010 Parag Nemade <pnemade AT redhat.com> - 0.2-1.1
- Resolves: rh#543948: Rebuilt for RHEL-6

* Wed Nov 25 2009 Caolan McNamara <caolanm@redhat.com> - 0.2-1
- initial version
