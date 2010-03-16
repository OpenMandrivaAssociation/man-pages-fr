%define LANG fr
%define __version 3.03.0
%define rel %mkrel 5
Summary:	French man (manual) pages from the Linux Documentation Project
Name:		man-pages-fr
Version:	%{__version}
Release:	%rel
License:	GPL
Group:	System/Internationalization
URL: 	http://manpagesfr.free.fr/
Source:	http://manpagesfr.free.fr/download/%name-%version.tar.bz2 
Source2: man-pages-fr-goodies.tar.bz2
Source3: http://www.delafond.org/traducmanfr/mansupfr.tar.bz2
Source4: http://www.delafond.org/traducmanfr/archivemansupfr.tar.bz2
Source10: http://www.enstimac.fr/Perl/perl-all-fr-man.tar.bz2
Source11: man-pages-fr-1.58-extras.tar.bz2
Source12: man-pages-extras-fr-0.7.9.tar.bz2
Source13: http://manpagesfr.free.fr/download/man-pages-sup-fr-20080606.tar.bz2
Source20: books-fr.xpm
Buildroot: %_tmppath/%name-root
BuildRequires: man => 1.5j-8mdk
Conflicts: rpm < 4.2, dkpg < 1.10.18, wireless-tools < 27-1mdk, urpmi < 4.5-2mdk
Conflicts: linkchecker < 2.3, vim-common < 7.0-2mdk
Requires: locales-fr, man => 1.5j-8mdk
Autoreqprov: false
BuildArchitectures: noarch
Obsoletes: man-fr, manpages-fr
Provides: man-fr, manpages-fr

%description
A large collection of man pages (reference material) from the Linux 
Documentation Project (LDP), translated to French.  The man pages are
organized into the following sections:

        Section 1:  User commands (intro only)
        Section 2:  System calls
        Section 3:  Libc calls
        Section 4:  Devices (e.g., hd, sd)
        Section 5:  File formats and protocols (e.g., wtmp, /etc/passwd,
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
		[[ -d $dis/man$sec/ ]] && mv $dis/man$sec/* pagesdeman/%_mandir/%LANG/man$sec/
	done
done

for i in man{1,2,3,4,5,6,7,8,9}; do mv pagesdeman%_mandir/%LANG/$i/* $i||true;done
for i in man{1,3,5,8}; do mv archive_des_mans/$i/* $i||true;done 
# perl man pages:
mv DocFr/* man1

%install
ln -sf iso_8859-1.7 man7/latin1.7; ln -sf iso_8859-1.7 man7iso_8859_7.7
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/%LANG/man{1,2,3,4,5,6,7}

# install X man pages :
for i in man{1,3,4,5,6}; do cp -a pagesdeman/usr/X11R6/man/%LANG/$i/*  $RPM_BUILD_ROOT/%_mandir/%LANG/$i;done

mkdir -p $RPM_BUILD_ROOT/var/catman/%LANG/cat{1,2,3,4,5,6,7,8,9,n}

for i in 1 2 3 4 5 6 7 8 9 ; do
	cp -adprf man$i $RPM_BUILD_ROOT/%_mandir/%LANG/||:
done

#
# remove doble files
#
rm $RPM_BUILD_ROOT/%_mandir/%LANG/man1/xawtv.1*
# this one is provided by alsaconf:
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man8/alsaconf.8
# these come from initscripts
rm $RPM_BUILD_ROOT/%_mandir/%LANG/{man8/usernetctl.8*,man1/{consoletype,doexec,netreport,usleep}.1*}
# these come from wireless:
rm $RPM_BUILD_ROOT/%_mandir/%LANG/{man5/iftab.5,man7/wireless.7,man8/{iwgetid,ifrename}.8}*
# these are provided by cups now
rm $RPM_BUILD_ROOT/%_mandir/%LANG/man*/{cancel,cups,{backend,filter}.1,lp,classes,disable,mime.{conv,type}s,printers.conf,{accept,enable,reject}.8}*
# these are provided by dpkg
rm $RPM_BUILD_ROOT/%_mandir/%LANG/man{1/{dpkg-deb,dpkg-name,dpkg-source},5/deb{,-control},8/{cleanup-info,dpkg{,-{divert,query,scanpackages,scansources,split,statoverride}},install-info,start-stop-daemon,update-alternatives}}.*
# these come from rpm:
rm $RPM_BUILD_ROOT/%_mandir/%LANG/man8/rpm.8*

# this lary wall perl script man page, not util linux rename tool one:
mv $RPM_BUILD_ROOT/%_mandir/%LANG/man1/rename{,.pl}.1
# these are provided by net-tools
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man{1/{dnsdomainname,domainname,hostname,nisdomainname,ypdomainname}.1,5/ethers.5,8/{arp,ifconfig,netstat,plipconfig,rarp,route,slattach}.8}
# this one is provided by wireless-tools
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man8/iw{config,event,list,priv,spy}.8
# these are provided by vim7:
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*
# this one is provided by linkchecker:
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man1/linkchecker.1
# these are provided by nano:
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man1/nano.1*
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man1/rnano.1*
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man5/nanorc*
# these are provided by fcron:
rm -f $RPM_BUILD_ROOT/%_mandir/%LANG/man*/fcron*

# upstream packagers are ... different
rm -f $RPM_BUILD_ROOT%_mandir/%LANG/man1/.swp

# there is already a tzselect man page at man8/tzselect.8
rm -f $RPM_BUILD_ROOT%_mandir/%LANG/man1/tzselect.1

tar jxf %SOURCE2 -C $RPM_BUILD_ROOT/usr/share
LANG=%LANG DESTDIR=$RPM_BUILD_ROOT %_sbindir/makewhatis $RPM_BUILD_ROOT/%_mandir/%LANG

mkdir -p $RPM_BUILD_ROOT/etc/cron.weekly
cat > $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis-%LANG.cron << EOF
#!/bin/bash
LANG=%LANG %_sbindir/makewhatis %_mandir/%LANG
exit 0
EOF
chmod a+x $RPM_BUILD_ROOT/etc/cron.weekly/makewhatis-%LANG.cron

mkdir -p  $RPM_BUILD_ROOT/var/cache/man/%LANG


%postun
# 0 means deleting the package
if [ "$1" = "0" ]; then
   ## Force removing of /var/catman/%LANG, if there isn't any man page
   ## directory /%_mandir/%LANG
   if [ ! -d %_mandir/%LANG ] ; then
       rm -rf /var/catman/%LANG
   fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,man,755)
%doc LISEZ_MOI changements
%dir %_mandir/%LANG
%dir /var/cache/man/%LANG
%verify(not md5 mtime size) /var/cache/man/%LANG/whatis
%_mandir/%LANG/man*
%attr(755,root,man)/var/catman/%LANG
%config(noreplace) %attr(755,root,root)/etc/cron.weekly/makewhatis-%LANG.cron


