#define debug_package %{nil}
%define Werror_cflags %nil
Name:		bibletime
Version:		3.0.3
Release:		1
Summary:		Easy to use Bible study tool
License:		GPLv2+
Url:		http://www.bibletime.info/
Group:		Text tools
Source0:	https://github.com/bibletime/bibletime/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5PrintSupport) cmake(Qt5WebChannel) cmake(Qt5WebEngine) cmake(Qt5WebEngineCore) cmake(Qt5WebEngineWidgets) cmake(Qt5QuickWidgets) cmake(Qt5Widgets) cmake(Qt5Xml) cmake(Qt5Svg) cmake(Qt5Network) cmake(Qt5Test)
BuildRequires:	pkgconfig(sword) >= 1.6.0
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libclucene-core) >= 0.9.16a
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	po4a
BuildRequires:	xsltproc
Requires:	sword >= 1.6.0
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
BibleTime is a free and easy to use bible study tool built with QT4.

BibleTime provides easy handling of digitized texts (Bibles, commentaries 
and lexicons) and powerful features to work with these texts (search in 
texts, write own notes, save, print etc.). Bibletime is a frontend for 
the SWORD Bible Framework.

%prep
%setup -qn %{name}-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category="Office" \
	%{buildroot}%{_datadir}/applications/*.desktop


%files
%doc ChangeLog LICENSE README.md
%{_bindir}/bibletime
%{_datadir}/bibletime
%{_datadir}/icons/hicolor/scalable/apps/bibletime.svg
%{_datadir}/applications/*.desktop




