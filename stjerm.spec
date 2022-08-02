Summary:	A GTK+-based drop-down terminal emulator
Name:		stjerm
Version:	0.18
Release:	1
Group:		Terminals	
License:	GPLv2
URL:		http://code.google.com/p/stjerm-terminal-emulator/
Source0:	https://github.com/stjerm/stjerm/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(vte)

%description
Stjerm is a GTK+-based drop-down terminal emulator similar to the consoles used
in PC games such as Quake and Half-Life2. Stjerm sets itself apart from similar
programs by providing a minimalistic interface combined with a small file size,
lightweight memory usage and easy integration with composite window managers
such as Compiz.

%prep
%setup -q

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%{_bindir}/%{name}
%{_mandir}/man8/stjerm.8*



%changelog
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.14-1
+ Revision: 800453
- imported package stjerm

