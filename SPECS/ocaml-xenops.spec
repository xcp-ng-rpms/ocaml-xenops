%global debug_package %{nil}

Name:           ocaml-xenops
Version:        2.0.0
Release:        14%{?dist}
Summary:        Low-level xen control operations OCaml
License:        LGPL
URL:            https://github.com/xapi-project/xenops
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops/archive?at=v%{version}&format=tar.gz&prefix=xenops-%{version}#/xenops-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops/archive?at=v2.0.0&format=tar.gz&prefix=xenops-2.0.0#/xenops-2.0.0.tar.gz) = ad7cc22a2508ae540201da13f9e9894ed1593025
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  xs-opam-repo
BuildRequires:  xen-ocaml-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  xen-libs-devel
BuildRequires:  xen-dom0-libs-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Low-level xen control operations in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       xs-opam-repo
Requires:       xen-ocaml-devel
Requires:       ocaml-xcp-idl-devel
Requires:       ocaml-xen-api-libs-transitional-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        tools
Summary:        Debugging tools for %{name}
Requires:       xen-libs
Requires:       xen-dom0-libs

%description   tools
A set of debugging tools which showcase the features of %{name}-devel.

%global ocaml_dir    /usr/lib/opamroot/system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1 -n xenops-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{build_ocaml_libdir}
mkdir -p %{build_ocaml_docdir}
make install OPAM_PREFIX=%{build_ocaml_dir} OPAM_LIBDIR=%{build_ocaml_libdir} BINDIR=%{buildroot}%{_bindir}


# this is to make opam happy
mkdir -p %{build_ocaml_libdir}/xapi-xenops

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{ocaml_libdir}/xenops
%exclude %{ocaml_libdir}/xenops/*.a
%exclude %{ocaml_libdir}/xenops/*.cmxa
%exclude %{ocaml_libdir}/xenops/*.cmxs
%exclude %{ocaml_libdir}/xenops/*.cmx
%exclude %{ocaml_libdir}/xenops/*.cmt

%files devel
%{ocaml_libdir}/xenops/*.a
%{ocaml_libdir}/xenops/*.cmxa
%{ocaml_libdir}/xenops/*.cmxs
%{ocaml_libdir}/xenops/*.cmx
%{ocaml_libdir}/stublibs/dllxenops_stubs.so
%{ocaml_docdir}/xenops
%{ocaml_libdir}/xapi-xenops
%{ocaml_docdir}/xapi-xenops

%files tools
%{_bindir}/list_domains

%changelog
* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 2.0.0-6
- Update SPEC file to get rid of rpmbuild warnings

* Fri Dec 04 2017 Marcello Seri <marcello.seri@citrix.com> - 2.0.0-1
- Port to jbuilder (backward compatible)
- Removed unused code
- Removed cpuid_check (was broken)
- Cleaned up dependencies and fixed compilation warnings

* Fri Apr 07 2017 Christian Lindig <christian.lindig@citrix.com> - 1.0.1-4
- Remove xen-devel from dependencies (was requested by tools sub
  package)

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.1-3
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Wed Mar 01 2017 Christian Lindig <christian.lindig@citrix.com> - 1.0.1-2
- Use Opam repository for build dependencies, trim other dependencies

* Thu Jun 23 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.1-1
- Update to 1.0.1

* Wed Apr 27 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-1
- Update to 0.9.6

* Mon Jun  2 2014 Euan Harris <euan.harris@citrix.com> - 0.9.4-2
- Split files correctly between base and devel packages

* Thu May  8 2014 David Scott <dave.scott@citrix.com> - 0.9.4-1
- Update to 0.9.4, add list_domains binary

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

