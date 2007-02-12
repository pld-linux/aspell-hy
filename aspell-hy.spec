Summary:	Armenian dictionary for aspell
Summary(pl.UTF-8):	Słownik armeński dla aspella
Name:		aspell-hy
Version:	0.0.3
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/hy/aspell6-hy-%{version}-%{subv}.tar.bz2
# Source0-md5:	05fa8d83c081e262e648764659703587
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Armenian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik armeński (lista słów) dla aspella.

%prep
%setup -q -n aspell6-hy-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/ChangeLog
%{_libdir}/aspell/*
%{_datadir}/aspell/*
