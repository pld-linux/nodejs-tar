%define		pkg	tar
Summary:	tar for node
Name:		nodejs-%{pkg}
Version:	0.1.12
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/tar
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	21028d3fe9f30f6a671fdf11b046fa7a
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-block-stream
Requires:	nodejs-fstream
Requires:	nodejs-inherits
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tar for node.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
