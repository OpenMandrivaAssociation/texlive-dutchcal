%global tl_name dutchcal
%global tl_revision 77682
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A reworking of ESSTIX13, adding a bold version
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dutchcal
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dutchcal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dutchcal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package reworks the mathematical calligraphic font ESSTIX13, adding
a bold version. LaTeX support files are included. The new fonts may also
be accessed from the most recent version of mathalpha. The fonts
themselves are subject to the SIL OPEN FONT LICENSE, version 1.1.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from dutchcal:
Map dutchcal.map
TL_DROPIN_EOF
