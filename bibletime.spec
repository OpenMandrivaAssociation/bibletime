#define debug_package %{nil}
%define Werror_cflags %nil
Name:		bibletime
Version:		2.9.2
Release:		2
Summary:		Easy to use Bible study tool
License:		GPLv2+
Url:		http://www.bibletime.info/
Group:		Text tools
Source0:		https://sourceforge.net/projects/bibletime/files/BibleTime%202/BibleTime%202%20source%20code/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(sword) >= 1.6.0
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libclucene-core) >= 0.9.16a
BuildRequires:	desktop-file-utils
BuildRequires:	kdelibs4-devel
BuildRequires:	cmake
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
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category="Office" \
	%{buildroot}%{_datadir}/applications/*.desktop


%files
%doc ChangeLog LICENSE README
%{_bindir}/bibletime
%{_datadir}/bibletime
%{_datadir}/icons/bibletime.svg
%{_datadir}/applications/*.desktop




