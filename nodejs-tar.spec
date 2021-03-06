%define		pkg	tar
Summary:	tar for node
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	c53f4ecca854ba617b00b9eaef2b26c5
URL:		https://github.com/isaacs/tar
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-block-stream
Requires:	nodejs-fstream < 2
Requires:	nodejs-fstream >= 1.0.2
Requires:	nodejs-inherits < 3
Requires:	nodejs-inherits >= 2
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
