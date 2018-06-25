Name:		texlive-tikzorbital
Version:	20180303
Release:	1
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
%{_texmfdistdir}/tex/latex/tikzorbital
%doc %{_texmfdistdir}/doc/latex/tikzorbital

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
