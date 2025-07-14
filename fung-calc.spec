Summary:	Fung-Calc is a graphing calculator
Summary(pl.UTF-8):	Fung-calc to kalkulator rysujący wykresy
Name:		fung-calc
Version:	1.3.2b
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/fung-calc/%{name}-%{version}.tar.gz
# Source0-md5:	bae7a2d39fd6658d4aa181ddc73bd5d5
Patch0:		%{name}-desktop.patch
URL:		http://fung-calc.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Fung-Calc is a free, open source advanced, yet easy to use, graphing
calculator for Linux using Qt. It plots several types of 2D and 3D
graphs. It combines the use of advanced mathematical features and ease
of use all in one package.

%description -l pl.UTF-8
Fung-Cals to łatwy w użyciu kalkulator rysujący wykresy, korzystający
z Qt. Rysuje kilka typów wykresów 2D i 3D. Łączy w sobie wykorzystanie
zaawansowanych możliwości matematycznych i łatwość użycia.

%package devel
Summary:	Header files for fung-calc libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek fung-calc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel

%description devel
Header files for fung-calc libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek fung-calc.

%prep
%setup -q
%patch -P0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_appsdir="%{_desktopdir}"; export kde_appsdir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_desktopdir}/Applications/* $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libfungcalc*.so.*.*.*
%dir %{_datadir}/%{name}
# needed here (incl. GPL COPYING)???
%{_datadir}/%{name}/[ACRT]*
%{_datadir}/%{name}/samplegraphs.fgc
%dir %{_datadir}/%{name}/translations
%lang(es) %{_datadir}/%{name}/translations/fung-calc.es.qm
%{_desktopdir}/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/fung_calc.png
%{_datadir}/mimelnk/application/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfungcalc*.so
%{_libdir}/libfungcalc*.la
%{_includedir}/%{name}
