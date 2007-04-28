%bcond_with    wizard

Name:           bibletime
Version:        1.6.4
Release:        %mkrel 1
Epoch:          0
Summary:        Easy to use Bible study tool for KDE
Icon:           bibletime.xpm
License:        GPL
Url:            http://www.bibletime.info/
Group:          Text tools
Source0:        http://umn.dl.sourceforge.net/sourceforge/bibletime/bibletime-%{version}.tar.bz2
BuildRequires:  kdelibs-devel
BuildRequires:  sword-devel
BuildRequires:  clucene-devel
Requires:       sword
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
BibleTime is a free and easy to use bible study tool for UNIX systems.

BibleTime provides easy handling of digitized texts (Bibles, commentaries 
and lexicons) and powerful features to work with these texts (search in 
texts, write own notes, save, print etc.). Bibletime is a frontend for 
the  SWORD Bible Framework.

%prep
%setup -q -n %{name}-%{version}%{letter}

%build
export QTDIR=%{_prefix}/lib/qt3
%{configure2_5x} --disable-rpath --disable-debug
%{make} kde_htmldir=%{_docdir}/HTML/

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} kde_htmldir=%{_docdir}/HTML/
%{__mkdir_p} %{buildroot}%{_menudir}
%{__mkdir_p} %{buildroot}%{_datadir}/config

%{__cat} > %{buildroot}%{_menudir}/%{name} << EOF
?package(bibletime):command="%{_bindir}/%{name}" \
icon="%{name}.png" \
needs="X11" \
section="More Applications/Editors" \
title="Bibletime" \
longtitle="An easy to use Bible study tool" \
xdg="true"
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bibletime
Comment=An easy to use Bible study tool
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Education-Literature;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_liconsdir}
%{__mkdir_p} %{buildroot}%{_iconsdir}
%{__mkdir_p} %{buildroot}%{_miconsdir}
%{__install} -m 644 bibletime/pics/48x48/hi48-app-bibletime.png %{buildroot}/%{_liconsdir}/%{name}.png
%{__install} -m 644 bibletime/pics/32x32/hi32-app-bibletime.png %{buildroot}/%{_iconsdir}/%{name}.png
%{__install} -m 644 bibletime/pics/16x16/hi16-app-bibletime.png %{buildroot}/%{_miconsdir}/%{name}.png

%if %with wizard
%{__cat} > %{buildroot}%{_menudir}/%{name}-setup << EOF
?package(bibletime):command="/usr/bin/btsetupwizard" \
icon="bibletime.png" \
needs="X11" \
section="Applications/Text tools" \
title="Bibletime Setup Wizard" \
longtitle="A setup tool for the easy to use Bible study tool" \
xdg="true"
EOF
%endif

%clean
%{__rm} -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE README
%if %with wizard
%{_bindir}/btsetupwizard
%endif
%{_bindir}/bibletime
%{_datadir}/apps/bibletime
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/applications/*.desktop
%{_docdir}/HTML
%exclude %{_includedir}
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


