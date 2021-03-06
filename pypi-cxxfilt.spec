#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cxxfilt
Version  : 0.3.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/d7/dc/71ac606f7dfa71d49e3dc126b49b18daefaf6bd953078858af30fde40702/cxxfilt-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d7/dc/71ac606f7dfa71d49e3dc126b49b18daefaf6bd953078858af30fde40702/cxxfilt-0.3.0.tar.gz
Summary  : Python interface to c++filt / abi::__cxa_demangle
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: pypi-cxxfilt-license = %{version}-%{release}
Requires: pypi-cxxfilt-python = %{version}-%{release}
Requires: pypi-cxxfilt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
============

%package license
Summary: license components for the pypi-cxxfilt package.
Group: Default

%description license
license components for the pypi-cxxfilt package.


%package python
Summary: python components for the pypi-cxxfilt package.
Group: Default
Requires: pypi-cxxfilt-python3 = %{version}-%{release}

%description python
python components for the pypi-cxxfilt package.


%package python3
Summary: python3 components for the pypi-cxxfilt package.
Group: Default
Requires: python3-core
Provides: pypi(cxxfilt)

%description python3
python3 components for the pypi-cxxfilt package.


%prep
%setup -q -n cxxfilt-0.3.0
cd %{_builddir}/cxxfilt-0.3.0
pushd ..
cp -a cxxfilt-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408943
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cxxfilt
cp %{_builddir}/cxxfilt-0.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cxxfilt/bea2c25a6aca85e33e4b56e95055f22e9e4b671e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cxxfilt/bea2c25a6aca85e33e4b56e95055f22e9e4b671e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
