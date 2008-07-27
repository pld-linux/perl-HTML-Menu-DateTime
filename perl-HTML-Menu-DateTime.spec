#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Menu-DateTime
Summary:	HTML::Menu::DateTime - easily create HTML select menus
Summary(pl.UTF-8):	HTML::Menu::DateTime - łatwie tworzenie menu wyboru HTML
Name:		perl-HTML-Menu-DateTime
Version:	1.00
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3324f180bc41fcbdf4d649c1c31e683f
URL:		http://search.cpan.org/dist/HTML-Menu-DateTime/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Carp)
BuildRequires:	perl-DateTime-Locale
BuildRequires:	perl-HTML-Menu-Select
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates data structures suitable for populating HTML::Template or
Template::Toolkit templates with dropdown date and time menus.

Allows any number of dropdown menus to be displayed on a single page,
each independantly configurable.

%description -l pl.UTF-8
Tworzy struktury danych przydatne do wypełniania szablonów
HTML::Template lub Template::Toolkit rozwijalnymi menu daty i godziny.

Pozwala na wyświetlenie na stronie dowolnej liczby menu, każde
oddzielnie konfigurowalne.

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
%dir %{perl_vendorlib}/HTML/Menu
%{perl_vendorlib}/HTML/Menu/DateTime.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
