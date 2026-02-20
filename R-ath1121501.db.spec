%define		packname	ath1121501.db

Summary:	Affymetrix Arabidopsis ATH1 Genome Array annotation data (chip ath1121501)
Name:		R-%{packname}
Version:	2.10.1
Release:	2
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	f43914f47b734878f6b5b97df065c433
URL:		http://www.bioconductor.org/packages/release/data/annotation/html/ath1121501.db.html
BuildRequires:	R-AnnotationDbi
BuildRequires:	R-org.At.tair.db >= 2.10.0
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-AnnotationDbi
Requires:	R-org.At.tair.db >= 2.10.0
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Affymetrix Arabidopsis ATH1 Genome Array annotation data
(chip ath1121501) assembled using data from public repositories

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/extdata
