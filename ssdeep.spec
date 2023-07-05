Summary:	Compute context triggered piecewise hashes
Name:		ssdeep
Version:	2.14.1
Release:	1
License:	GPL v2+
URL:		https://ssdeep-project.github.io/ssdeep/
Source0:	https://github.com/ssdeep-project/ssdeep/releases/download/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ed4f374e20ffec72e679f56c32218581
BuildRequires:	libstdc++-devel
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
ssdeep is a program for computing context triggered piecewise hashes
(CTPH). Also called fuzzy hashes, CTPH can match inputs that have
homologies. Such inputs have sequences of identical bytes in the same
order, although bytes in between these sequences may be different in
both content and length.

%package devel
Summary:	Development files for libfuzzy
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains library and header files for
developing applications that use libfuzzy.

%package libs
Summary:	Runtime libfuzzy library

%description libs
The %{name}-libs package contains libraries needed by applications
that use libfuzzy.


%prep
%setup -q

%build
%configure \
   --disable-auto-search \
   --disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/libfuzzy.la

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files devel
%defattr(644,root,root,755)
%doc FILEFORMAT NEWS README TODO
%{_includedir}/fuzzy.h
%{_includedir}/edit_dist.h
%attr(755,root,root) %{_libdir}/libfuzzy.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfuzzy.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libfuzzy.so.2
