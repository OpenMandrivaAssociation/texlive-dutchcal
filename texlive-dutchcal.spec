# revision 23448
# category Package
# catalog-ctan /fonts/dutchcal
# catalog-date 2011-06-24 10:20:36 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-dutchcal
Version:	1.0
Release:	3
Summary:	A reworking of ESSTIX13, adding a bold version
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dutchcal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dutchcal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dutchcal.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package reworks the mathematical calligraphic font
ESSTIX13, adding a bold version. LaTeX support files are
included. The new fonts may also be accessed from the most
recent version of mathalfa. The fonts themselves are subject to
the SIL OPEN FONT LICENSE, version 1.1.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/dutchcal/DutchCalBold.afm
%{_texmfdistdir}/fonts/afm/public/dutchcal/DutchCalReg.afm
%{_texmfdistdir}/fonts/map/dvips/dutchcal/dutchcal.map
%{_texmfdistdir}/fonts/tfm/public/dutchcal/dutchcal-b.tfm
%{_texmfdistdir}/fonts/tfm/public/dutchcal/dutchcal-r.tfm
%{_texmfdistdir}/fonts/tfm/public/dutchcal/rdutchcalb.tfm
%{_texmfdistdir}/fonts/tfm/public/dutchcal/rdutchcalr.tfm
%{_texmfdistdir}/fonts/type1/public/dutchcal/DutchCalBold.pfb
%{_texmfdistdir}/fonts/type1/public/dutchcal/DutchCalReg.pfb
%{_texmfdistdir}/fonts/vf/public/dutchcal/dutchcal-b.vf
%{_texmfdistdir}/fonts/vf/public/dutchcal/dutchcal-r.vf
%{_texmfdistdir}/tex/latex/dutchcal/dutchcal.sty
%{_texmfdistdir}/tex/latex/dutchcal/udutchcal.fd
%doc %{_texmfdistdir}/doc/fonts/dutchcal/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751157
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718273
- texlive-dutchcal
- texlive-dutchcal
- texlive-dutchcal
- texlive-dutchcal

