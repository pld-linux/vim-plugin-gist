# TODO:
# - What to do with .vimup file?
%define		subver 34
%define		rel 0.1
Summary:	Vim plugin: Gist
Name:		vim-plugin-gist
Version:	3.0
Release:	%{subver}.%{rel}
License:	BSD
Group:		Applications/Editors/Vim
Source0:	http://github.com/mattn/gist-vim/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	86e4ec33cf3ee0d4c98158c2702a90e3
URL:		http://github.com/mattn/gist-vim
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Vim plugin that allows to create, edit, delete and browse github
gists.

%prep
%setup -qc
mv mattn-gist-vim-*/* .
rm -rf mattn-gist-vim-*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a . $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/*
