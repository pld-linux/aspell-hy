Summary:	Armenian dictionary for aspell
Summary(pl.UTF-8):	Słownik armeński dla aspella
Name:		aspell-hy
Version:	0.10.0
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/hy/aspell6-hy-%{version}-%{subv}.tar.bz2
# Source0-md5:	41af00aed5078bb4755728c7dec834a2
URL:		http://aspell.net/
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
