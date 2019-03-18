#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RColorBrewer
Version  : 1.1.2
Release  : 55
URL      : http://cran.r-project.org/src/contrib/RColorBrewer_1.1-2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/RColorBrewer_1.1-2.tar.gz
Summary  : ColorBrewer Palettes
Group    : Development/Tools
License  : Apache-1.1 Apache-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n RColorBrewer

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552784133

%install
export SOURCE_DATE_EPOCH=1552784133
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RColorBrewer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RColorBrewer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RColorBrewer
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  RColorBrewer || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RColorBrewer/COPYING
/usr/lib64/R/library/RColorBrewer/DESCRIPTION
/usr/lib64/R/library/RColorBrewer/INDEX
/usr/lib64/R/library/RColorBrewer/Meta/Rd.rds
/usr/lib64/R/library/RColorBrewer/Meta/features.rds
/usr/lib64/R/library/RColorBrewer/Meta/hsearch.rds
/usr/lib64/R/library/RColorBrewer/Meta/links.rds
/usr/lib64/R/library/RColorBrewer/Meta/nsInfo.rds
/usr/lib64/R/library/RColorBrewer/Meta/package.rds
/usr/lib64/R/library/RColorBrewer/NAMESPACE
/usr/lib64/R/library/RColorBrewer/R/RColorBrewer
/usr/lib64/R/library/RColorBrewer/R/RColorBrewer.rdb
/usr/lib64/R/library/RColorBrewer/R/RColorBrewer.rdx
/usr/lib64/R/library/RColorBrewer/help/AnIndex
/usr/lib64/R/library/RColorBrewer/help/RColorBrewer.rdb
/usr/lib64/R/library/RColorBrewer/help/RColorBrewer.rdx
/usr/lib64/R/library/RColorBrewer/help/aliases.rds
/usr/lib64/R/library/RColorBrewer/help/paths.rds
/usr/lib64/R/library/RColorBrewer/html/00Index.html
/usr/lib64/R/library/RColorBrewer/html/R.css
