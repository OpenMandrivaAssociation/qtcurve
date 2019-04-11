%define libnamekde4 %{_lib}kde4-style-qtcurve
%define libnamegtk2 %{_lib}qtcurve-gtk2
%define _disable_ld_no_undefined 1

# %define gitdate 20180913

%bcond_without qt5

Summary:	QtCurve Theme for Qt and GTK
Name:		qtcurve
Version:	1.9.0
Release:	1.%{gitdate}.1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://github.com/KDE/QtCurve
#Source0:	https://github.com/KDE/qtcurve/releases/%{name}-%{version}.tar.gz
# git archive --prefix=qtcurve-1.9.0-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../qtcurve-1.9.0-$(date +%Y%m%d).tar.gz
Source0:	%{name}-%{version}.tar.gz
#Source0:	https://github.com/KDE/QtCurve/archive/%{name}-%{version}.tar.gz
Patch0:		qtcurve-1.8.18-kwin-frames.patch
Patch1:		qtcurve-1.8.17-l10n-fix.patch
Patch2:		qtcurve-1.8.18-enable-translations.patch
#Patch3:		qtcurve-1.8.18-qt5.3.patch
BuildRequires:	cmake
BuildRequires:	kdelibs-devel
BuildRequires:	kde-workspace-devel
%if %{with qt5}
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
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5DBus)
%endif

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)

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
%package -n plasma-style-qtcurve
Summary:	QtCurve style for Plasma 5
Group:		Graphical desktop/KDE
Requires:	qt5-style-qtcurve

%description -n plasma-style-qtcurve
QtCurve style for Plasma 5.

%files -n plasma-style-qtcurve
%{_kde_datadir}/kstyle/themes/qtcurve.themerc
%{_qt5_plugindir}/kstyle_qtcurve5_config.so
%{_kde_datadir}/kxmlgui5/QtCurve/QtCurveui.rc

#----------------------------------------------------------------------------

%package -n qt5-style-qtcurve
Summary:	QtCurve style for Qt5
Group:		Graphical desktop/KDE

%description -n qt5-style-qtcurve
QtCurve style for Qt5.

%files -n qt5-style-qtcurve
%{_qt5_plugindir}/styles/qtcurve.so

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
%setup -qn %{name}-%{version}-%{gitdate}
%apply_patches

%build
%cmake_kde4 \
	-DENABLE_QT4:BOOL=ON \
	-DQTC_QT4_ENABLE_KDE:BOOL=ON \
%if %{with qt5}
	-DENABLE_QT5:BOOL=ON \
	-DQTC_QT5_ENABLE_KDE:BOOL=ON \
	-DQTC_QT5_ENABLE_QTQUICK2:BOOL=ON \
%else
	-DENABLE_QT5:BOOL=OFF \
	-DQTC_QT5_ENABLE_KDE:BOOL=OFF \
%endif
	-DENABLE_GTK2:BOOL=ON
%make

%install
%makeinstall_std -C build

# We don't have devel package so we don't need it
rm %{buildroot}%{_libdir}/libqtcurve-cairo.so
rm %{buildroot}%{_libdir}/libqtcurve-utils.so

%find_lang qtcurve
