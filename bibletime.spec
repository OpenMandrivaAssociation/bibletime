#define debug_package %{nil}
%define Werror_cflags %nil
Name:		bibletime
Version:		3.1.1
Release:		1
Summary:		Easy to use Bible study tool
License:		GPLv2+
Url:		https://www.bibletime.info/
Group:		Text tools
Source0:	https://github.com/bibletime/bibletime/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6PrintSupport) cmake(Qt6WebChannel) cmake(Qt6WebEngineCore) cmake(Qt6WebEngineWidgets) cmake(Qt6QuickWidgets) cmake(Qt6Widgets) cmake(Qt6Xml) cmake(Qt6Svg) cmake(Qt6Network) cmake(Qt6Test) cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(sword) >= 1.6.0
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libclucene-core) >= 0.9.16a
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	po4a
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildSystem:	cmake
BuildOption:	-DUSE_QT6:BOOL=ON
BuildOption:	-DBUILD_HANDBOOK_PDF:BOOL=OFF
BuildOption:	-DBUILD_HOWTO_PDF:BOOL=OFF
BuildOption:	-DBUILD_HANDBOOK_HTML:BOOL=OFF
Requires:	sword >= 1.6.0

%description
BibleTime is a free and easy to use bible study tool built with QT4.

BibleTime provides easy handling of digitized texts (Bibles, commentaries 
and lexicons) and powerful features to work with these texts (search in 
texts, write own notes, save, print etc.). Bibletime is a frontend for 
the SWORD Bible Framework.

%install -a
desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category="Office" \
	%{buildroot}%{_datadir}/applications/*.desktop

%files
%doc LICENSE README.md
%doc %{_datadir}/doc/bibletime/howto/html*
%{_bindir}/bibletime
%{_datadir}/bibletime
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/info.bibletime.BibleTime.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/info.bibletime.BibleTime.svg




