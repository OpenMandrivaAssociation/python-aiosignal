# Created by pyp2rpm-3.3.5
%global pypi_name aiosignal

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        2
Summary:        aiosignal: a list of registered asynchronous callbacks
Group:          Development/Python
License:        Apache 2
URL:            https://github.com/aio-libs/aiosignal
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
A project to manage callbacks in asyncio projects.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
#pytest

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

