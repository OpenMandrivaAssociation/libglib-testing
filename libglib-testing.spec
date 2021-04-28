%define api		0
%define major		0
%define gi_major	0.0
%define libname		%mklibname glib-testing %major
%define develname	%mklibname -d glib-testing

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		libglib-testing
Version:	0.1.0
Release:	1
Summary:	Library providing test harnesses and mock classes
Group:		System/Libraries
License:	LGPLv2+
URL:		https://gitlab.freedesktop.org/pwithnall/%{name}
Source0:	https://gitlab.gnome.org/pwithnall/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0) >= 2.17.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.19.0
BuildRequires:	pkgconfig(gthread-2.0)

%description
%{name} is a test library providing test harnesses and mock classes which
complement the classes provided by GLib. It is intended to be used by any
project which uses GLib and which wants to write internal unit tests.

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
%{name} is a test library providing test harnesses and mock classes which
complement the classes provided by GLib. It is intended to be used by any
project which uses GLib and which wants to write internal unit tests.


%package -n %develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	glib-testing-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Dinstalled_tests=false
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/%{name}-%api.so.%{major}{,.*}

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/libglib-testing/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/glib-testing-%{api}.pc
