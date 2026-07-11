%global tl_name tikzorbital
%global tl_revision 36439

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Atomic and molecular orbitals using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzorbital
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzorbital.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzorbital.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Atomic s, p and d orbitals may be drawn, as well as molecular orbital
diagrams.

