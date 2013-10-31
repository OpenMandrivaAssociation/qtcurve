%define libnamekde4 %{_lib}kde4-style-qtcurve
%define libnamegtk2 %{_lib}qtcurve-gtk2

Summary:	QtCurve Theme for Qt and GTK
Name:		qtcurve
Version:	1.8.17
Release:	3
Group:		Graphical desktop/Other
License:	GPLv2+
Url:		https://github.com/QtCurve/qtcurve/releases
Source0:	https://github.com/QtCurve/qtcurve/archive/%{name}-%{version}.tar.gz
Patch0:		qtcurve-1.8.17-kwin-frames.patch
Patch1:		qtcurve-1.8.17-l10n-fix.patch
Patch2:		qtcurve-1.8.17-l10n-desktop.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel

%description
QtCurve Theme for Qt and GTK.

#----------------------------------------------------------------------------

%package -n kde4-style-qtcurve
Summary:	QtCurve theme for KDE4
Group:		Graphical desktop/KDE
Requires:	%{libnamekde4} = %{EVRD}
Suggests:	qtcurve-gtk2
#added for test purpose by bedi
Suggests:	oxygen-gtk

%description -n kde4-style-qtcurve
QtCurve theme for KDE4.

%files -n kde4-style-qtcurve -f qtcurve.lang
%{_kde_appsdir}/QtCurve
%{_kde_appsdir}/color-schemes/
%{_kde_appsdir}/kstyle/
%{_kde_appsdir}/kwin/

#----------------------------------------------------------------------------

%package -n %{libnamekde4}
Summary:	KDE4 libraries for QtCurve
Group:		Graphical desktop/KDE
Provides:	libkde4-style-qtcurve = %{EVRD}

%description -n %{libnamekde4}
KDE4 libraries for QtCurve.

%files -n %{libnamekde4}
%{_kde_libdir}/kde4/kstyle_qtcurve_config.so
%{_kde_libdir}/kde4/kwin3_qtcurve.so
%{_kde_libdir}/kde4/kwin_qtcurve_config.so
%{_kde_libdir}/kde4/plugins/styles/qtcurve.so

#----------------------------------------------------------------------------

%package -n qtcurve-gtk2
Summary:	QtCurve Theme for GTK2
Group:		Graphical desktop/GNOME
Requires:	%{libnamegtk2} = %{EVRD}

%description -n qtcurve-gtk2
QtCurve Theme for GTK2.

%files -n qtcurve-gtk2
%{_datadir}/themes/QtCurve

#----------------------------------------------------------------------------

%package -n %{libnamegtk2}
Summary:	GTK2 libraries for QtCurve
Group:		Graphical desktop/GNOME
Provides:	libqtcurve-gtk2 = %{EVRD}

%description -n %{libnamegtk2}
GTK2 libraries for QtCurve.

%files -n %{libnamegtk2}
%{_libdir}/gtk-2.0/*/engines/libqtcurve.so

#----------------------------------------------------------------------------

%define major 0
%define libqtcurveutils %mklibname qtcurve-utils %{major}

%package -n %{libqtcurveutils}
Summary:	Shared library for QtCurve
Group:		System/Libraries

%description -n %{libqtcurveutils}
Shared library for QtCurve.

%files -n %{libqtcurveutils}
%{_libdir}/libqtcurve-utils.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake_kde4 \
	-DENABLE_QT4:BOOL=ON \
	-DQTC_QT4_ENABLE_KDE:BOOL=ON \
	-DENABLE_QT5:BOOL=OFF \
	-DENABLE_GTK2:BOOL=ON
%make

%install
%makeinstall_std -C build

# We don't have devel package so we don't need it
rm %{buildroot}%{_libdir}/libqtcurve-utils.so

%find_lang qtcurve

