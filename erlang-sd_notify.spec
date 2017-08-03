%global realname sd_notify
%global upstream lemenkov


Name:		erlang-%{realname}
Version:	0.1
Release:	%mkrel 10
Summary:	Erlang interface to systemd notify subsystem
Group:		Development/Other
License:	MIT
URL:		https://github.com/%{upstream}/erlang-%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
Source1:	erlang-sd_notify-rebar.config
BuildRequires:	erlang-rebar
BuildRequires:	systemd-devel
%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
%{summary}.


%prep
%setup -q
cp %{SOURCE1} rebar.config


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# Empty for now
%{erlang_test}


%files
%license LICENSE
%{erlang_appdir}/



%changelog
* Mon Jun 06 2016 neoclust <neoclust> 0.1-10.mga6
+ Revision: 1020361
- imported package erlang-sd_notify

