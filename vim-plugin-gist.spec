# TODO:
# - What to do with .vimup file?
%define		gitver 34
Summary:	Vim plugin: Gist
Name:		vim-plugin-gist
Version:	3.0
Release:	%{gitver}.0.1
License:	vim
Group:		Applications/Editors/Vim
Source0:	http://download.github.com/mattn-gist-vim-3.0-34-gd31d0e2.tar.gz
# Source0-md5:	1d27e6268e9091dda73420a359987beb
URL:		http://vim-latex.sourceforge.net/
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Vim plugin that allows to create, edit, delete and browse github gists.

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
