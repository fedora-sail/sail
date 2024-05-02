Name:           sail
Version:        0.17.1
Release:        %autorelease
Summary:        Sail architecture definition language

License:        Sail
URL:            https://github.com/rems-project/%{name}
Source0:        https://github.com/rems-project/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  dnf
BuildRequires:  git
BuildRequires:  gmp-devel
BuildRequires:  zlib-devel
BuildRequires:  linksem-devel
BuildRequires:  ott
BuildRequires:  opam
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune-site-devel
BuildRequires:  ocaml-bisect-ppx-devel
BuildRequires:  ocaml-lem-devel
BuildRequires:  ocaml-yojson-devel
BuildRequires:  ocaml-pprint-devel
BuildRequires:  ocaml-odoc-devel
BuildRequires:  ocaml-base64-devel
BuildRequires:  ocaml-omd-devel
BuildRequires:  ocaml-linenoise-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib

%description
Sail is a language for describing the instruction-set architecture (ISA) semantics of processors. Sail aims to provide a engineer-friendly, vendor-pseudocode-like language for describing instruction semantics. It is essentially a first-order imperative language, but with lightweight dependent typing for numeric types and bitvector lengths, which are automatically checked using Z3. It has been used for several papers, available from http://www.cl.cam.ac.uk/~pes20/sail/.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
export LEMLIB=/usr/share/lem/library
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md CHANGELOG.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
