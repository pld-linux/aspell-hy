Summary:	Armenian dictionary for aspell
Summary(pl):	S³ownik armeñski dla aspella
Name:		aspell-hy
Version:	0.0.2
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/hy/aspell6-hy-%{version}-%{subv}.tar.bz2
# Source0-md5:	eeca157be8f6dd7aa5145b295c08040a
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Armenian dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik armeñski (lista s³ów) dla aspella.

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
