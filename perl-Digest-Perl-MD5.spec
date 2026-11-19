#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Digest
%define		pnam	Perl-MD5
Summary:	Digest::Perl::MD5 - Perl implementation of Rivest's MD5 algorithm
Summary(pl.UTF-8):	Digest::Perl::MD5 - implementacja algorytmu MD5 Rivesta w Perlu
Name:		perl-Digest-Perl-MD5
Version:	1.91
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/D/DE/DELTA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55072a25a11589bc10c808ab85b71edd
URL:		https://metacpan.org/dist/Digest-Perl-MD5
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::Perl::MD5 is a Perl implementation of the MD5 algorithm,
compatible with Digest::MD5 interface. It does not need a C compiler.

%description -l pl.UTF-8
Digest::Perl::MD5 to implementacja algorytmu MD5 w czystym Perlu,
zgodna z interfejsem Digest::MD5. Nie wymaga kompilatora C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.md
%{perl_vendorlib}/Digest/Perl
%{_mandir}/man3/Digest::Perl::MD5.3pm*
