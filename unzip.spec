Name:           unzip
Version:        6.0
Release:        51
Summary:        A utility for unpacking zip files
License:        Info-ZIP,Public Domain
URL:            http://www.info-zip.org/UnZip.html
Source:         http://downloads.sourceforge.net/infozip/unzip60.tar.gz

Patch0001:      unzip-6.0-bzip2-configure.patch
Patch0002:      unzip-6.0-exec-shield.patch
Patch0003:      unzip-6.0-close.patch
Patch0004:      unzip-6.0-attribs-overflow.patch
Patch0005:      unzip-6.0-configure.patch
Patch0006:      unzip-6.0-manpage-fix.patch
Patch0007:      unzip-6.0-fix-recmatch.patch
Patch0008:      unzip-6.0-symlink.patch
Patch0009:      unzip-6.0-caseinsensitive.patch
Patch0010:      unzip-6.0-format-secure.patch
Patch0011:      unzip-6.0-valgrind.patch
Patch0012:      unzip-6.0-x-option.patch
Patch0013:      unzip-6.0-overflow.patch
Patch0014:      unzip-6.0-cve-2014-8139.patch
Patch0015:      unzip-6.0-cve-2014-8140.patch
Patch0016:      unzip-6.0-cve-2014-8141.patch
Patch0017:      unzip-6.0-overflow-long-fsize.patch
Patch0018:      unzip-6.0-heap-overflow-infloop.patch
Patch0019:      unzip-6.0-alt-iconv-utf8.patch
Patch0020:      unzip-6.0-alt-iconv-utf8-print.patch
Patch0021:      0001-Fix-CVE-2016-9844-rhbz-1404283.patch
Patch0022:      unzip-6.0-timestamp.patch
Patch0023:      unzip-6.0-cve-2018-1000035-heap-based-overflow.patch

Patch6000:      CVE-2018-18384.patch
Patch6001:      CVE-2019-13232-pre.patch
Patch6002:      CVE-2019-13232.patch
Patch6003:      CVE-2019-13232-fur1.patch
Patch6004:      backport-CVE-2021-4217.patch
Patch9000:      CVE-2019-13232-fur2.patch
Patch9001:      CVE-2022-0530.patch
Patch9002:      CVE-2022-0529.patch

BuildRequires:  bzip2-devel gcc

%description
UnZip is an extraction utility for archives compressed in .zip format.
UnZip will list, test, or extract files from a .zip archive, commonly found on MS-DOS systems.
The default behavior (with no options) is to extract all files into the current directory
(and subdirectorie below it) from the specified zipfile.

%package help
Summary: Man pages for unzip

%description help
Package help includes man pages for unzip.

%prep
%autosetup -n %{name}60 -p1

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIE"
%make_build -f unix/Makefile CF_NOOPT="-I. -DUNIX $RPM_OPT_FLAGS -DNOMEMCPY -DIZ_HAVE_UXUIDGID -DNO_LCHMOD" \
                      LFLAGS2="-Wl,-z,relro -pie" generic_gcc

%install
%make_install -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 INSTALL="cp -p"

%check
make check -f unix/Makefile

%files
%license LICENSE COPYING.OLD
%doc README BUGS
%{_bindir}/*

%files help
%{_mandir}/man1/*

%changelog
* Sat Mar 4 2023 yanglongkang <yanglongkang@h-partners.com> - 6.0-51
- add "PIE" compiler options

* Tue Sep 6 2022 dongyuzhen <dongyuzhen@h-partners.com> - 6.0-50
- fix CVE-2021-4217

* Tue May 10 2022 shixuantong <shixuantong@h-partners.com> - 6.0-49
- enable check test suite

* Wed Feb 23 2022 tianwei <tianwei@h-partners.com> - 6.0-48
- fix CVE-2022-0529 CVE-2022-0530

* Thu Jun 10 2021 shixuantong <shixuantong@huawei.com> - 6.0-47
- add gcc to BuildRequires and revert unzip-6.0-crc-builtin.patch

* Tue May 12 2021 openEuler hanzhelii <18221254@bjtu.edu.cn> - 6.0-46
- add unzip-6.0-crc-builtin.patch

* Mon Mar 2 2020 openEuler Buildteam <buildteam@openeuler.org> - 6.0-45
- delete garbled characters

* Mon Mar 2 2020 openEuler Buildteam <buildteam@openeuler.org> - 6.0-44
- fix CVE-2019-13232

* Tue Dec 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 6.0-43
- Delete unneeded patch

* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 6.0-42
- Revert CVE-2019-13232

* Fri Sep 20 2019 Zaiwang Li<lizaiwang1@huawei.com> - 6.0-41
- Init Package
