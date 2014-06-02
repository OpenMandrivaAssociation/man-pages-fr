%define LNG fr

Summary:	French man (manual) pages from the Linux Documentation Project
Name:		man-pages-fr
Version:	3.03.0
Release:	12.1
License:	GPLv2
Group:		System/Internationalization
Url:		http://manpagesfr.free.fr/
Source0:	http://manpagesfr.free.fr/download/%name-%version.tar.bz2 
Source2:	man-pages-fr-goodies.tar.bz2
Source3:	http://www.delafond.org/traducmanfr/mansupfr.tar.bz2
Source4:	http://www.delafond.org/traducmanfr/archivemansupfr.tar.bz2
Source10:	http://www.enstimac.fr/Perl/perl-all-fr-man.tar.bz2
Source11:	man-pages-fr-1.58-extras.tar.bz2
Source12:	man-pages-extras-fr-0.7.9.tar.bz2
Source13:	http://manpagesfr.free.fr/download/man-pages-sup-fr-20080606.tar.bz2
Source20:	books-fr.xpm
BuildArch:	noarch
BuildRequires:	man
Requires:	locales-fr
Requires:	man
Autoreqprov:	false

%description
A large collection of man pages (reference material) from the Linux 
Documentation Project (LDP), translated to French.  The man pages are
organized into the following sections:

        Section 1:  User commands (intro only)
        Section 2:  System calls
        Section 3:  Libc calls
        Section 4:  Devices (e.g., hd, sd)
        Section 5:  File formats and protocols (e.g., wtmp, %{_sysconfdir}passwd,
                nfs)
        Section 5:  Games (intro only)
        Section 7:  Conventions, macro packages, etc. (e.g., nroff, ascii)
        Section 8:  System administration (intro only)
        Section 9:  Kernel routines

%prep
%setup -q -a3 -a4 -a10 -a11 -a12 -a13

%build
rm -f man2/core.21??
for dis in {archive_des_mans,pagesdeman}/{debian,mandrake}; do
	rmdir $dis/* || :
	for sec in 1 2 3 4 5 7 8 9; do
		[[ -d $dis/man$sec/ ]] && mv $dis/man$sec/* pagesdeman/%{_mandir}/%{LNG}/man$sec/
	done
done

for i in man{1,2,3,4,5,6,7,8,9}; do mv pagesdeman%{_mandir}/%{LNG}/$i/* $i||true;done
for i in man{1,3,5,8}; do mv archive_des_mans/$i/* $i||true;done 
# perl man pages:
mv DocFr/* man1

%install
ln -sf iso_8859-1.7 man7/latin1.7; ln -sf iso_8859-1.7 man7iso_8859_7.7
mkdir -p %{buildroot}/%{_mandir}/%{LNG}/man{1,2,3,4,5,6,7}

# install X man pages :
for i in man{1,3,4,5,6}; do cp -a pagesdeman/usr/X11R6/man/%{LNG}/$i/*  %{buildroot}/%{_mandir}/%{LNG}/$i;done

mkdir -p %{buildroot}/var/catman/%{LNG}/cat{1,2,3,4,5,6,7,8,9,n}

for i in 1 2 3 4 5 6 7 8 9 ; do
	cp -adprf man$i %{buildroot}/%{_mandir}/%{LNG}/||:
done

#
# remove double files
#
rm %{buildroot}/%{_mandir}/%{LNG}/man1/xawtv.1*
# this one is provided by alsaconf:
rm -f %{buildroot}/%{_mandir}/%{LNG}/man8/alsaconf.8
# these come from initscripts
rm %{buildroot}/%{_mandir}/%{LNG}/{man8/usernetctl.8*,man1/{consoletype,doexec,netreport,usleep}.1*}
# these come from wireless:
rm %{buildroot}/%{_mandir}/%{LNG}/{man5/iftab.5,man7/wireless.7,man8/{iwgetid,ifrename}.8}*
# these are provided by cups now
rm %{buildroot}/%{_mandir}/%{LNG}/man*/{cancel,cups,{backend,filter}.1,lp,classes,disable,mime.{conv,type}s,printers.conf,{accept,enable,reject}.8}*
# these are provided by dpkg
rm %{buildroot}/%{_mandir}/%{LNG}/man{1/{dpkg-deb,dpkg-name,dpkg-source},5/deb{,-control},8/{cleanup-info,dpkg{,-{divert,query,scanpackages,scansources,split,statoverride}},install-info,start-stop-daemon,update-alternatives}}.*
# these come from rpm:
rm %{buildroot}/%{_mandir}/%{LNG}/man8/rpm.8*

# this lary wall perl script man page, not util linux rename tool one:
mv %{buildroot}/%{_mandir}/%{LNG}/man1/rename{,.pl}.1
# these are provided by net-tools
rm -f %{buildroot}/%{_mandir}/%{LNG}/man{1/{dnsdomainname,domainname,hostname,nisdomainname,ypdomainname}.1,5/ethers.5,8/{arp,ifconfig,netstat,plipconfig,rarp,route,slattach}.8}
# this one is provided by wireless-tools
rm -f %{buildroot}/%{_mandir}/%{LNG}/man8/iw{config,event,list,priv,spy}.8
# these are provided by vim7:
rm -f %{buildroot}/%{_mandir}/%{LNG}/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*
# this one is provided by linkchecker:
rm -f %{buildroot}/%{_mandir}/%{LNG}/man1/linkchecker.1
# these are provided by nano:
rm -f %{buildroot}/%{_mandir}/%{LNG}/man1/nano.1*
rm -f %{buildroot}/%{_mandir}/%{LNG}/man1/rnano.1*
rm -f %{buildroot}/%{_mandir}/%{LNG}/man5/nanorc*
# these are provided by fcron:
rm -f %{buildroot}/%{_mandir}/%{LNG}/man*/fcron*

# upstream packagers are ... different
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/.swp

# there is already a tzselect man page at man8/tzselect.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/tzselect.1

# nmap already provides it (#62985)
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/nmap.1

# (tpg) #conflicts with shadow-utils-4.1.5.1-5
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/chage.1
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/gpasswd.1
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/newgrp.1
rm -f %{buildroot}%{_mandir}/%{LNG}/man5/faillog.5
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/chpasswd.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/faillog.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/grpconv.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/grpunconv.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/groupadd.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/groupdel.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/groupmod.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/grpck.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/lastlog.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/newusers.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/pwck.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/pwconv.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/pwunconv.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/userdel.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/usermod.8
rm -f %{buildroot}%{_mandir}/%{LNG}/man8/vipw.8



tar jxf %SOURCE2 -C %{buildroot}/usr/share
LANG=%{LNG} DESTDIR=%{buildroot} %{_bindir}/mandb %{buildroot}/%{_mandir}/%{LNG}

mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
cat > %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron << EOF
#!/bin/bash
LANG=%{LNG} %{_bindir}/mandb %{_mandir}/%{LNG}
exit 0
EOF
chmod a+x %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron

mkdir -p  %{buildroot}/var/cache/man/%{LNG}

touch %{buildroot}/var/cache/man/%{LNG}/whatis

%postun
# 0 means deleting the package
if [ "$1" = "0" ]; then
   ## Force removing of /var/catman/%{LNG}, if there isn't any man page
   ## directory /%{_mandir}/%{LNG}
   if [ ! -d %{_mandir}/%{LNG} ] ; then
       rm -rf /var/catman/%{LNG}
   fi
fi

%post
%create_ghostfile /var/cache/man/%{LNG}/whatis root root 644

%files
%doc LISEZ_MOI changements
%dir %{_mandir}/%{LNG}
%dir /var/cache/man/%{LNG}
%ghost %config(noreplace) /var/cache/man/%{LNG}/whatis
%{_mandir}/%{LNG}/man*
%{_mandir}/%{LNG}/cat*
%{_mandir}/%{LNG}/CACHEDIR.TAG*
%{_mandir}/%{LNG}/index.db*
%attr(755,root,man) /var/catman/%{LNG}
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron

