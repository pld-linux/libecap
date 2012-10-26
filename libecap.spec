Summary:	eCAP - the code in the middle
Name:		libecap
Version:	0.2.0
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.measurement-factory.com/tmp/ecap/%{name}-%{version}.tar.gz
# Source0-md5:	e65a855f4fbb0f3136af7fe28249e883
URL:		http://www.e-cap.org/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eCAP is a software interface that allows a network application, such
as an HTTP proxy or an ICAP server, to outsource content analysis and
adaptation to a loadable module. For each applicable protocol message
being processed, an eCAP-enabled application supplies the message
details to the adaptation module and gets back an adapted message or a
"not interested" response. These exchanges often include message
bodies.

If you are familiar with the ICAP protocol (RFC 3507), then you may
think of eCAP as an "embedded ICAP", where network interactions with
an ICAP server are replaced with function calls to an adaptation
module.

%package devel
Summary:	Header files for eCAP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki eCAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for eCAP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki eCAP.

%package static
Summary:	Static eCAP library
Summary(pl.UTF-8):	Statyczna biblioteka eCAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static eCAP library.

%description static -l pl.UTF-8
Statyczna biblioteka eCAP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libecap.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS NOTICE README
%attr(755,root,root) %{_libdir}/libecap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecap.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libecap.so
%{_includedir}/libecap
%{_pkgconfigdir}/libecap.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libecap.a
