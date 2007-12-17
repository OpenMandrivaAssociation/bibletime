%bcond_with    wizard

Name:           bibletime
Version:        1.6.5
Release:        %mkrel 1
Epoch:          0
Summary:        Easy to use Bible study tool for KDE
License:        GPLv2+
Url:            http://www.bibletime.info/
Group:          Text tools
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-i18n-%{version}.tar.bz2
Patch0:		bibletime-1.6.5-fix-desktop.patch
BuildRequires:  kdelibs-devel
BuildRequires:  sword-devel
BuildRequires:  clucene-devel
Requires:       sword
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
%patch0 -p0

%build
export QTDIR=%{_prefix}/lib/qt3
%{configure2_5x} --disable-rpath --disable-debug
make kde_htmldir=%{_docdir}/HTML/

cd bibletime-i18n-%version
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} kde_htmldir=%{_docdir}/HTML/

cd bibletime-i18n-%version
%makeinstall_std
cd -

rm -fr %buildroot%_includedir

%{__mkdir_p} %{buildroot}%{_liconsdir}
%{__mkdir_p} %{buildroot}%{_iconsdir}
%{__mkdir_p} %{buildroot}%{_miconsdir}
%{__install} -m 644 bibletime/pics/48x48/hi48-app-bibletime.png %{buildroot}/%{_liconsdir}/%{name}.png
%{__install} -m 644 bibletime/pics/32x32/hi32-app-bibletime.png %{buildroot}/%{_iconsdir}/%{name}.png
%{__install} -m 644 bibletime/pics/16x16/hi16-app-bibletime.png %{buildroot}/%{_miconsdir}/%{name}.png

%find_lang %name  --with-html

%clean
%{__rm} -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE README
%if %with wizard
%{_bindir}/btsetupwizard
%endif
%{_bindir}/bibletime
%{_datadir}/apps/bibletime
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/applications/*.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
