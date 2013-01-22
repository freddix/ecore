Summary:	Enlightenment Foundation Library
Name:		ecore
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b408bf8e0feef59f7165c8184a5e459c
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	evas-devel
BuildRequires:	glib-devel
BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXcomposite-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXp-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ecore is a library of convenience functions.

%package devel
Summary:	Header files for eet library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for eet library.

%package modules
Summary:	Ecore modules
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description modules
Ecore modules.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir} -name *.la -exec rm {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libecore*.so.1
%attr(755,root,root) %{_libdir}/libecore*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore*.so
%{_includedir}/ecore-1
%{_pkgconfigdir}/ecore*.pc

%files modules
%defattr(644,root,root,755)
%dir %{_libdir}/ecore
%dir %{_libdir}/ecore/immodules
%attr(755,root,root) %{_libdir}/ecore/immodules/xim.so

