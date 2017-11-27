Name:		Boostnote
Version:	0.8.17	
Release:	1%{?dist}
Summary:	An open source note-taking app for programmers.
License:	GPLv3	
URL:		https://boostnote.io	
Source0:	https://github.com/BoostIO/%{name}/archive/v%{version}.tar.gz
Source1:    %{name}.desktop
Source2:    %{name}.js
Patch0:		boostnote-warning-fix.patch
Patch1:		boostnote-remove-analytics.patch     

BuildRequires:	gcc-c++, make, git
Requires:	electron, nodejs

%description
An open source note-taking app for programmers.

%prep
%autosetup -n %{name}-%{version}
%patch0
%patch1
cp -p %SOURCE1
cp -p %SOURCE2


%build
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
dnf install -y nodejs npm
npm install -g grunt-cli
cd %{name}-%{version}
npm install --no-optional
grunt compile
rm -r node_modules/
npm install --production --no-optional

%install
cd %{name}-%{version}
appdir=/opt/%{name}
install -dm755 %{buildroot}${appdir}
cp -a * %{buildroot}${appdir}
%files
%doc



%changelog

