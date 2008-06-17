%bcond_with    wizard

Name:           bibletime
Version:        1.6.5.1
Release:        %mkrel 1
Epoch:          0
Summary:        Easy to use Bible study tool for KDE
License:        GPLv2+
Url:            http://www.bibletime.info/
Group:          Text tools
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-i18n-1.6.5.tar.bz2
Patch0:		bibletime-1.6.5-fix-desktop.patch
BuildRequires:  kdelibs-devel
BuildRequires:  sword-devel
BuildRequires:  clucene-devel
Requires:       sword
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	bibletime-i18n
Obsoletes:	bibletime-i18n-af
Obsoletes:	bibletime-i18n-de
Obsoletes:	bibletime-i18n-fi
Obsoletes:	bibletime-i18n-it
Obsoletes:	bibletime-i18n-no
Obsoletes:	bibletime-i18n-ro
Obsoletes:	bibletime-i18n-ua
Obsoletes:	bibletime-i18n-bg
Obsoletes:	bibletime-i18n-en_GB
Obsoletes:	bibletime-i18n-fr
Obsoletes:	bibletime-i18n-ko
Obsoletes:	bibletime-i18n-pl
Obsoletes:	bibletime-i18n-ru
Obsoletes:	bibletime-i18n-cs
Obsoletes:	bibletime-i18n-es
Obsoletes:	bibletime-i18n-hu
Obsoletes:	bibletime-i18n-nl
Obsoletes:	bibletime-i18n-pt_br
Obsoletes:	bibletime-i18n-sk

%description
BibleTime is a free and easy to use bible study tool for UNIX systems.

BibleTime provides easy handling of digitized texts (Bibles, commentaries 
and lexicons) and powerful features to work with these texts (search in 
texts, write own notes, save, print etc.). Bibletime is a frontend for 
the SWORD Bible Framework.

%prep
%setup -q -a 1
#%patch0 -p0

%build
%configure_kde3
%make

cd bibletime-i18n-1.6.5
%configure_kde3
%make
cd -

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

cd bibletime-i18n-1.6.5
%makeinstall_std
cd -

rm -fr %buildroot%_kde3_includedir

%find_lang %name  --with-html

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE README
%if %with wizard
%{_kde3_bindir}/btsetupwizard
%endif
%{_kde3_bindir}/bibletime
%{_kde3_datadir}/apps/bibletime
%{_kde3_datadir}/icons/*/*/*/*.png
%{_kde3_datadir}/applications/*.desktop
