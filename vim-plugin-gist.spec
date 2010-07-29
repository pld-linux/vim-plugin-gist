Summary:	Vim plugin: Gist
Name:		vim-plugin-gist
Version:	3.8
Release:	1
License:	BSD
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php?src_id=13427#/gist-%{version}.vim
# Source0-md5:	8c51aff6a4c2a9cd3993ae9774f13a7b
URL:		http://www.vim.org/scripts/script.php?script_id=2423
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimplugindir	%{_datadir}/vim/plugin

%description
Vim plugin that allows to create, edit, delete and browse github
gists.

%prep
grep -q '^" Version: %{version}$' %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimplugindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimplugindir}/gist.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimplugindir}/gist.vim
