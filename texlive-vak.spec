# revision 23431
# category Package
# catalog-ctan /biblio/bibtex/contrib/vak
# catalog-date 2011-07-04 16:33:07 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-vak
Version:	20110704
Release:	7
Summary:	BibTeX style for Russian Theses, books, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/vak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vak.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vak.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file can be used to format the bibliographies of PhD
theses, books etc., according to the latest Russian standards:
GOST 7.82 - 2001 and GOST 7.1 - 2003. It introduces the minimum
number of new entries and styles to cover all frequently used
situations. The style file provides an easy way to perform a
semiautomatic, or a completely manual sort of the list of the
references. Processing bibliographies produced by the style
requires a 8-bit BibTeX system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/vak/vak.bst
%doc %{_texmfdistdir}/doc/bibtex/vak/README
%doc %{_texmfdistdir}/doc/bibtex/vak/test-key.zip
%doc %{_texmfdistdir}/doc/bibtex/vak/test.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110704-2
+ Revision: 757336
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110704-1
+ Revision: 719869
- texlive-vak
- texlive-vak
- texlive-vak

