Summary:	Graphical front-end for FREE CIVilization clone
Summary(es):	GTK front-end por Clon del juego Civilization
Summary(pl):	Graficzny frontend dla serwera freeciv
Name:		gcivserv
Version:	0.1b
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://www.hoeyer.de/projects/gcivserv/src/gCivServ-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pl_lang.patch
Patch1:		%{name}-enviroment.patch
URL:		http://www.freeciv.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel > 1.2.1
Requires:	freeciv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK front-end for server of freeciv - clone of Sid Meiers
Civilization.

%description -l es
GTK front-end por Clon del juego Civilization.

%description -l pl
Graficzny frontend dla serwera freeciv - klonu Civilization Sida
Meiersa.

%prep
%setup -q -n gCivServ-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure2_13 \
	--with-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_applnkdir}/Games/Strategy,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/Strategy/*
%{_pixmapsdir}/*
