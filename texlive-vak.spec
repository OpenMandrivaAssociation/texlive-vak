%global tl_name vak
%global tl_revision 75878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibTeX style for Russian Theses, books, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/vak
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vak.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vak.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The file can be used to format the bibliographies of PhD theses, books
etc., according to the latest Russian standards: GOST 7.82 - 2001 and
GOST 7.1 - 2003. It introduces the minimum number of new entries and
styles to cover all frequently used situations. The style file provides
an easy way to perform a semiautomatic, or a completely manual sort of
the list of the references. Processing bibliographies produced by the
style requires a 8-bit BibTeX system.

