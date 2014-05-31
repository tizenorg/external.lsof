#
# Please submit bugfixes or comments via http://bugs.meego.com/
#

Name:           lsof
Version:        4.82
Release:        1
License:        BSD-style
Summary:        A utility which lists open files on a Linux/UNIX system
Group:          Development/Debuggers

Url:            ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof
# lsof contains licensed code that we cannot ship.  Therefore we use
# upstream2downstream.sh script to remove the code before shipping it.
#
# The script you can found in CVS or download from:
# http://cvs.fedoraproject.org/viewcvs/rpms/lsof/devel/upstream2downstream.sh
#
%define lsofrh lsof_4.82-rh
Source0:        %{lsofrh}.tar.bz2

# 184338 - allow lsof access nptl threads
Patch1:         lsof_4.81-threads.patch

%description
Lsof stands for LiSt Open Files, and it does just that: it lists
information about files that are open by the processes running on a
UNIX system.

%prep
%setup -q -n %{lsofrh}
%patch1 -p1

%build
LSOF_VSTR=2.6.16 LINUX_BASE=/proc ./Configure -n linux

make DEBUG="%{optflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sbindir}
install -p -m 0755 lsof %{buildroot}%{_prefix}/sbin
mkdir -p %{buildroot}%{_mandir}/man8
install -p lsof.8 %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}/usr/share/license
cp LICENSE.lsof %{buildroot}/usr/share/license/%{name}

%clean
rm -rf %{buildroot}

%docs_package

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_sbindir}/lsof
/usr/share/license/%{name}

