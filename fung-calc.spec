Summary:	Fung-Calc is a graphing calculator
Summary(pl):	Fung-calc to kalkulator rysuj±cy wykresy
Name:		fung-calc
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/fung-calc/%{name}-%{version}.tar.gz
# Source0-md5:	8178d3c53be1b927e6d94bb6426de941
URL:		http://fung-calc.sourceforge.net/
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fung-Calc is a free, open source advanced, yet easy to use, graphing
calculator for Linux using Qt. It plots several types of 2D and 3D
graphs. It combines the use of advanced mathematical features and ease
of use all in one package.

%description -l pl
Fung-Cals to ³atwy w u¼yciu kalkulator rysuj±cy wykresy korzystaj±cy z
QT. Rysuje kilka typów wykresów 2D i 3D.
%prep
%setup -q

%build
%define         _htmldir        %{_datadir}/doc/kde/HTML
kde_htmldir="%{_htmldir}"; export kde_htmldir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_htmldir}/en/%{name}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libfungcalc*
%{_datadir}/%{name}

%{_includedir}/%{name}/*.h
