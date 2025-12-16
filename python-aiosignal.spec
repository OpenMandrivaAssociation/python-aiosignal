%global module aiosignal
%bcond tests 1

Name:		python-%{module}
Version:	1.4.0
Release:	2
Summary:	aiosignal: a list of registered asynchronous callbacks
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/aio-libs/aiosignal
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pip)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(frozenlist)
%endif


%{?python_provide:%python_provide python3-%{module}}

%description
A project to manage callbacks in asyncio projects.

%prep
%autosetup -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info
# Remove pytest-cov plugin entries from pytest-ini as we dont do upstream coverage tests
sed -i '21,29d' pytest.ini

%build
%py_build
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest -v
%endif

%files -n python-%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.rst

