%define libnamekde4 %{_lib}kde4-style-qtcurve
%define libnamegtk2 %{_lib}qtcurve-gtk2
%define _disable_ld_no_undefined 1
%define _disable_lto 1

Summary:	QtCurve Theme for Qt and GTK
Name:		qtcurve
Version:	1.9
Release:	4
License:	LGPLv2.1
Group:		Graphical desktop/Other
Url:		https://github.com/KDE/QtCurve
Source0:	https://download.kde.org/stable/qtcurve/%{name}-%{version}.tar.xz
# Mirror:
#Source0:	https://github.com/KDE/QtCurve/archive/%{name}-%{version}.tar.gz

Patch0:		0037-utils-gtkprops-Remove-unnecessary-constexpr-this-is-.patch
Patch1:		qtcurve-1.9-missing-include-openmandriva.patch

BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:  cmake(KF5FrameworkIntegration)

BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	gettext

Requires:	plasma-style-qtcurve = %{version}-%{release}
Requires:	qt5-style-qtcurve = %{version}-%{release}
Requires:	qtcurve-gtk2 = %{version}-%{release}

%description
QtCurve Theme for Qt and GTK.

%files
%{_datadir}/locale/*/LC_MESSAGES/qtcurve.mo
#----------------------------------------------------------------------------

%package -n plasma-style-qtcurve
Summary:	QtCurve style for Plasma 5
Group:		Graphical desktop/KDE
Requires:	qt5-style-qtcurve

%description -n plasma-style-qtcurve
QtCurve style for Plasma 5.

%files -n plasma-style-qtcurve
%{_datadir}/kstyle/themes/qtcurve.themerc
%{_libdir}/qt5/plugins/kstyle_qtcurve5_config.so
%{_datadir}/kxmlgui5/QtCurve/QtCurveui.rc

#----------------------------------------------------------------------------

%package -n qt5-style-qtcurve
Summary:	QtCurve style for Qt5
Group:		Graphical desktop/KDE

%description -n qt5-style-qtcurve
QtCurve style for Qt5.

%files -n qt5-style-qtcurve
%{_libdir}/qt5/plugins/styles/qtcurve.so

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

%define cairo_major 1
%define libqtcurvecairo %mklibname qtcurve-cairo %{cairo_major}

%package -n %{libqtcurvecairo}
Summary:	Shared library for QtCurve
Group:		System/Libraries

%description -n %{libqtcurvecairo}
Shared library for QtCurve.

%files -n %{libqtcurvecairo}
%{_libdir}/libqtcurve-cairo.so.%{cairo_major}*

#----------------------------------------------------------------------------

%define utils_major 2
%define libqtcurveutils %mklibname qtcurve-utils %{utils_major}

%package -n %{libqtcurveutils}
Summary:	Shared library for QtCurve
Group:		System/Libraries

%description -n %{libqtcurveutils}
Shared library for QtCurve.

%files -n %{libqtcurveutils}
%{_libdir}/libqtcurve-utils.so.%{utils_major}*
#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}
%autopatch -p1

%build
#export CC=gcc
#export CXX=g++
%cmake \
	-DENABLE_QT4=OFF \
	-DENABLE_QT5:BOOL=ON \
	-DQTC_QT5_ENABLE_KDE:BOOL=ON \
	-DQTC_QT5_ENABLE_QTQUICK2:BOOL=ON \
	-DENABLE_GTK2:BOOL=ON
%make_build

%install
%make_install -C build

# Not needed files.
rm -fv %{buildroot}%{_libdir}/libqtcurve-{cairo,utils}.so
