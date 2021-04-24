#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kerberos
Version  : 1.3.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/34/18/9c86fdfdb27e0f7437b7d5a9e22975dcc382637b2a68baac07843be512fc/kerberos-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/18/9c86fdfdb27e0f7437b7d5a9e22975dcc382637b2a68baac07843be512fc/kerberos-1.3.0.tar.gz
Summary  : Kerberos high-level interface
Group    : Development/Tools
License  : Apache-2.0
Requires: kerberos-python = %{version}-%{release}
Requires: kerberos-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : e2fsprogs-dev
BuildRequires : krb5-dev
BuildRequires : python3-dev

%description
==================

%package python
Summary: python components for the kerberos package.
Group: Default
Requires: kerberos-python3 = %{version}-%{release}

%description python
python components for the kerberos package.


%package python3
Summary: python3 components for the kerberos package.
Group: Default
Requires: python3-core
Provides: pypi(kerberos)

%description python3
python3 components for the kerberos package.


%prep
%setup -q -n kerberos-1.3.0
cd %{_builddir}/kerberos-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133487
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
