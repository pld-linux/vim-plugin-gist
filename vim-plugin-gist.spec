# TODO:
# - What to do with .vimup file?
%define		rel 0.1
Summary:	Vim plugin: Gist
Name:		vim-plugin-gist
Version:	3.7
Release:	%{rel}
License:	BSD
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php%3Fsrc_id%3D13105#gist.vim
# Source0-md5:	4c7c6cbe627d3bd474a9bd3c5efb659e
URL:		http://www.vim.org/scripts/script.php%3Dscript_id%3F2423
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimplugindir	%{_datadir}/vim/plugin

%description
Vim plugin that allows to create, edit, delete and browse github
gists.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimplugindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimplugindir}/gist.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimplugindir}/gist.vim
