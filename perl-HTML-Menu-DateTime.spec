#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Menu-DateTime
Summary:	HTML::Menu::DateTime - easily create HTML select menus
Summary(pl):	HTML::Menu::DateTime - ³atwie tworzenie menu wyboru HTML
Name:		perl-HTML-Menu-DateTime
Version:	0.93
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27344ff995ac3f6cd21ba9126b9cf441
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Carp)
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates data structures suitable for populating HTML::Template or
Template::Toolkit templates with dropdown date and time menus.

Allows any number of dropdown menus to be displayed on a single page,
each independantly configurable.
   
%description -l pl
Tworzy struktury danych przydatne do wype³aniania szablonów
HTML::Template lub Template::Toolkit rozwijalnymi menu daty i godziny.

Pozwala na wy¶wietlenie na stronie dowolnej liczby menu, ka¿de
oddzielnie konfigurowywalne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/Menu/DateTime.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
