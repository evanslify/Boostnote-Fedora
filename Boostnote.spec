Name:		Boostnote
Version:	0.8.17	
Release:	1%{?dist}
Summary:	An open source note-taking app for programmers.
License:	GPLv3	
URL:		https://boostnote.io	
Source0:	https://github.com/BoostIO/%{name}/archive/v%{version}.tar.gz
Source1:    %{name}.desktop
Patch0:		boostnote-warning-fix.patch

BuildRequires:	nodejs, git
Requires:	electron, nodejs

%description
An open source note-taking app for programmers.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version}
# %patch0
# cp -p %SOURCE1 .
# cp -p %SOURCE2


%build
sudo npm install -g grunt-cli
npm install --no-optional
grunt compile
rm -r node_modules/
npm install --production --no-optional

%install
appdir=/opt/%{name}
install -dm755 %{buildroot}${appdir}
cp -a * %{buildroot}${appdir}
%files
%doc readme.md
%license LICENSE
/opt/%{name}/*


%changelog

