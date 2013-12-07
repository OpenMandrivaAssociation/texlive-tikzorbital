# revision 28561
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzorbital
# catalog-date 2012-12-17 20:44:22 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-tikzorbital
Version:	20121217
Release:	2
Summary:	Atomic and molecular orbitals using TiKZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzorbital
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzorbital.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzorbital.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Atomic s, p and d orbitals may be drawn, as well as molecular
orbital diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzorbital/tikzorbital.sty
%doc %{_texmfdistdir}/doc/latex/tikzorbital/tikzorbital.pdf
%doc %{_texmfdistdir}/doc/latex/tikzorbital/tikzorbital.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
