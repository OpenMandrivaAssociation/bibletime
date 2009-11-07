#define betaver beta3

Name:           bibletime
Version:        2.3
Release:        %mkrel 1
Epoch:          0
Summary:        Easy to use Bible study tool for KDE
License:        GPLv2+
Url:            http://www.bibletime.info/
Group:          Text tools
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  kdelibs4-devel
BuildRequires:	boost-devel
BuildRequires:  sword-devel >= 1.5.9
BuildRequires:  clucene-devel >= 0.9.16a
BuildRequires:	desktop-file-utils
Requires:       sword >= 1.5.9
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
%setup -q

%build
%cmake_kde4
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} -C build

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-key='MimeType' \
	--remove-key='SwallowExec' \
	--remove-key='SwallowTitle' \
	--remove-key='TerminalOptions' \
	--remove-key='X-KDE-Username' \
	--remove-category="QT" \
	--add-category="Qt" \
	%buildroot%_datadir/applications/*.desktop

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

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{_kde_bindir}/bibletime
%{_kde_datadir}/bibletime
%{_kde_datadir}/icons/*
%{_kde_datadir}/applications/*.desktop
