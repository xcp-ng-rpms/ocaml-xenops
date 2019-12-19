%global debug_package %{nil}

Name:           ocaml-xenops
Version:        2.6.0
Release:        2%{?dist}
Summary:        Low-level xen control operations OCaml
License:        LGPL
URL:            https://github.com/xapi-project/xenops

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops/archive?at=v2.6.0&format=tar.gz&prefix=ocaml-xenops-2.6.0#/xenops-2.6.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops/archive?at=v2.6.0&format=tar.gz&prefix=ocaml-xenops-2.6.0#/xenops-2.6.0.tar.gz) = 8ca1e2ac7072e105f4b74f64efbdf4ab504273f1

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
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops/archive?at=v2.6.0&format=tar.gz&prefix=ocaml-xenops-2.6.0#/xenops-2.6.0.tar.gz) = 8ca1e2ac7072e105f4b74f64efbdf4ab504273f1
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
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops/archive?at=v2.6.0&format=tar.gz&prefix=ocaml-xenops-2.6.0#/xenops-2.6.0.tar.gz) = 8ca1e2ac7072e105f4b74f64efbdf4ab504273f1
Summary:        Debugging tools for %{name}
Requires:       xen-libs
Requires:       xen-dom0-libs

%description   tools
A set of debugging tools which showcase the features of %{name}-devel.

%global ocaml_dir    %{_opamroot}/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1

%build
make

%install
make DESTDIR=%{buildroot} BINDIR=%{_bindir} install

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
* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 2.6.0-2
- bump packages after xs-opam update

* Wed Aug 07 2019 Christian Lindig <christian.lindig@citrix.com> - 2.6.0-1
- CP-30366 Use dune in xenops.opam

* Tue Jun 11 2019 Christian Lindig <christian.lindig@citrix.com> - 2.5.0-1
- Update Travis configuration
- Remove obsolete xenstore_watch module
- Remove obsolete .hg_archival.txt

* Wed Jan 23 2019 Christian Lindig <christian.lindig@citrix.com> - 2.4.0-1
- Prepare for Dune 1.6
- Use Ocaml 4.07 in Travis

* Tue Dec 04 2018 Christian Lindig <christian.lindig@citrix.com> - 2.3.0-1
- Moved from jbuilder to dune and deprecated xcp in favour of xapi-idl.

* Tue Nov 06 2018 Christian Lindig <christian.lindig@citrix.com> - 2.2.0-1
- Update opam files for Opam 2, update Travis configuration

* Fri Sep 07 2018 Christian Lindig <christian.lindig@citrix.com> - 2.1.0-1
- CA-289145: Close socket if error occurs when connecting
- src/io: make safe-string compliant

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

