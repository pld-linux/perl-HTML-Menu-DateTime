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
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce7fefe58c9238b6cfb6d81eef4324d9
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
%{perl_vendorlib}/HTML/Menu/DateTime.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
