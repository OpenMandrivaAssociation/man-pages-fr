%define LNG fr

Summary:	French man (manual) pages from the Linux Documentation Project
Name:		man-pages-fr
Version:	3.03.0
Release:	10
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
		[[ -d $dis/man$sec/ ]] && mv $dis/man$sec/* pagesdeman/%_mandir/%LNG/man$sec/
	done
done

for i in man{1,2,3,4,5,6,7,8,9}; do mv pagesdeman%_mandir/%LNG/$i/* $i||true;done
for i in man{1,3,5,8}; do mv archive_des_mans/$i/* $i||true;done 
# perl man pages:
mv DocFr/* man1

%install
ln -sf iso_8859-1.7 man7/latin1.7; ln -sf iso_8859-1.7 man7iso_8859_7.7
rm -rf %{buildroot}
mkdir -p %{buildroot}/%_mandir/%LNG/man{1,2,3,4,5,6,7}

# install X man pages :
for i in man{1,3,4,5,6}; do cp -a pagesdeman/usr/X11R6/man/%LNG/$i/*  %{buildroot}/%_mandir/%LNG/$i;done

mkdir -p %{buildroot}/var/catman/%LNG/cat{1,2,3,4,5,6,7,8,9,n}

for i in 1 2 3 4 5 6 7 8 9 ; do
	cp -adprf man$i %{buildroot}/%_mandir/%LNG/||:
done

#
# remove doble files
#
rm %{buildroot}/%_mandir/%LNG/man1/xawtv.1*
# this one is provided by alsaconf:
rm -f %{buildroot}/%_mandir/%LNG/man8/alsaconf.8
# these come from initscripts
rm %{buildroot}/%_mandir/%LNG/{man8/usernetctl.8*,man1/{consoletype,doexec,netreport,usleep}.1*}
# these come from wireless:
rm %{buildroot}/%_mandir/%LNG/{man5/iftab.5,man7/wireless.7,man8/{iwgetid,ifrename}.8}*
# these are provided by cups now
rm %{buildroot}/%_mandir/%LNG/man*/{cancel,cups,{backend,filter}.1,lp,classes,disable,mime.{conv,type}s,printers.conf,{accept,enable,reject}.8}*
# these are provided by dpkg
rm %{buildroot}/%_mandir/%LNG/man{1/{dpkg-deb,dpkg-name,dpkg-source},5/deb{,-control},8/{cleanup-info,dpkg{,-{divert,query,scanpackages,scansources,split,statoverride}},install-info,start-stop-daemon,update-alternatives}}.*
# these come from rpm:
rm %{buildroot}/%_mandir/%LNG/man8/rpm.8*

# this lary wall perl script man page, not util linux rename tool one:
mv %{buildroot}/%_mandir/%LNG/man1/rename{,.pl}.1
# these are provided by net-tools
rm -f %{buildroot}/%_mandir/%LNG/man{1/{dnsdomainname,domainname,hostname,nisdomainname,ypdomainname}.1,5/ethers.5,8/{arp,ifconfig,netstat,plipconfig,rarp,route,slattach}.8}
# this one is provided by wireless-tools
rm -f %{buildroot}/%_mandir/%LNG/man8/iw{config,event,list,priv,spy}.8
# these are provided by vim7:
rm -f %{buildroot}/%_mandir/%LNG/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*
# this one is provided by linkchecker:
rm -f %{buildroot}/%_mandir/%LNG/man1/linkchecker.1
# these are provided by nano:
rm -f %{buildroot}/%_mandir/%LNG/man1/nano.1*
rm -f %{buildroot}/%_mandir/%LNG/man1/rnano.1*
rm -f %{buildroot}/%_mandir/%LNG/man5/nanorc*
# these are provided by fcron:
rm -f %{buildroot}/%_mandir/%LNG/man*/fcron*

# upstream packagers are ... different
rm -f %{buildroot}%_mandir/%LNG/man1/.swp

# there is already a tzselect man page at man8/tzselect.8
rm -f %{buildroot}%_mandir/%LNG/man1/tzselect.1

# nmap already provides it (#62985)
rm -f %{buildroot}%_mandir/%LNG/man1/nmap.1

tar jxf %SOURCE2 -C %{buildroot}/usr/share
LANG=%LNG DESTDIR=%{buildroot} %{_bindir}/mandb %{buildroot}/%_mandir/%LNG

mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
cat > %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron << EOF
#!/bin/bash
LANG=%LNG %{_bindir}/mandb %_mandir/%LNG
exit 0
EOF
chmod a+x %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron

mkdir -p  %{buildroot}/var/cache/man/%LNG

touch %{buildroot}/var/cache/man/%LNG/whatis

%postun
# 0 means deleting the package
if [ "$1" = "0" ]; then
   ## Force removing of /var/catman/%LNG, if there isn't any man page
   ## directory /%_mandir/%LNG
   if [ ! -d %_mandir/%LNG ] ; then
       rm -rf /var/catman/%LNG
   fi
fi

%post
%create_ghostfile /var/cache/man/%LNG/whatis root root 644

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,man,755)
%doc LISEZ_MOI changements
%dir %_mandir/%LNG
%dir /var/cache/man/%LNG
%ghost %config(noreplace) /var/cache/man/%LNG/whatis
%_mandir/%LNG/man*
#%_mandir/%LNG/whatis
%attr(755,root,man) /var/catman/%LNG
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron




%changelog
* Thu Apr 07 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.03.0-8
+ Revision: 651790
- fix nmap.1 conflict with nmap (#62985)

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 3.03.0-7mdv2011.0
+ Revision: 609320
- rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 3.03.0-6mdv2011.0
+ Revision: 609302
- fix build
- fix typos
- fix build
- rebuild
- rebuilt for 2010.1

* Fri Oct 09 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 3.03.0-4mdv2010.0
+ Revision: 456473
- Don't ship duplicated tzselect man pages (#20326).

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.03.0-3mdv2009.1
+ Revision: 351573
- rebuild

* Wed Aug 27 2008 Thierry Vignaud <tv@mandriva.org> 3.03.0-2mdv2009.0
+ Revision: 276585
- new release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.59.0-2mdv2009.0
+ Revision: 223173
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- update 3rd party source

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 03 2007 Thierry Vignaud <tv@mandriva.org> 2.59.0-1mdv2008.1
+ Revision: 114632
- new release

* Wed Aug 29 2007 Thierry Vignaud <tv@mandriva.org> 2.39.1-4mdv2008.0
+ Revision: 74687
- kill useless prereq
- fix conflict with fcron (#25085)

* Mon Jul 02 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.39.1-3mdv2008.0
+ Revision: 47173
- remove rpm 'Icon:' field from spec, it was causing submit problems
  and is not used anyway (the .xpm file is now declared as a source)
- remove extra verbosity: use %%setup -q and remove -v from cp calls
- X manpages are now on standard manpagedir, since /usr/X11R6/man is obsolete

* Mon Jun 04 2007 Thierry Vignaud <tv@mandriva.org> 2.39.1-2mdv2008.0
+ Revision: 35254
- fix conflict with alsaconf (#30471)

* Mon Apr 23 2007 Thierry Vignaud <tv@mandriva.org> 2.39.1-1mdv2008.0
+ Revision: 17418
- new release


* Wed Dec 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.68.0-4mdv2007.0
+ Revision: 100614
- Import man-pages-fr

* Wed Dec 20 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.68.0-4mdv2007.1
- fix conflict with nano (#27541)

* Thu May 11 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.68.0-4mdk
- fix more conflicts

* Thu May 11 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.68.0-3mdk
- fix another conflict with vim-7.0

* Wed May 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.68.0-2mdk
- new release
- new source URL
- fix conflict with vim-7.0
- update source 3
- rediff patch 0
- kill patch 6 (fixed upstream)

* Mon Aug 15 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.64.0-1mdk
- new release
- new URL
- kill patches 7 & 8
- rediff patch 0

* Sun Jul 10 2005 Eskild Hustvedt <eskild@mandriva.org> 1.58.0-19mdk
- Drop nano manpages (fixes bug #16766)
- Make rpmlint a bit happier
- %%mkrel
  (what on earth am I updating French manpages for?)

* Thu Feb 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-18mdk
- updates
- add: gpal.1, gpasm.1, gpdasm.1, gplib.1, gplink.1, gputils.1, gpvc.1, gpvo.1,
  kino.1, ps2ascii.1

- patch 8: typo fix (#13909)

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-17mdk
- fix conflict wit latest linkchecker

* Tue Jan 04 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-16mdk
- fix conflicts with latest wireless-tools

* Thu Dec 23 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-15mdk
- add:
  o cbreak.3x, curs_inopts.3x, echo.3x, halfdelay.3x, intrflush.3x, keypad.3x,
	meta.3x, nocbreak.3x, nodelay.3x, noecho.3x, noqiflush.3x, noraw.3x,
	notimeout.3x, qiflush.3x, raw.3x, timeout.3x, typeahead.3x, wtimeout.3x
  o bb.1, cdappend.1, cdbkup.1, cdcat.1, cdrstr.1, cdsplit.1, linkchecker.1,
    sg.1, yppasswd.1
  o shadow.3
  o console.apps.5, console.perms.5
  o domainname.8, faillog.8, groupadd.8, groupdel.8, groupmod.8, grpck.8,
	grpconv.8, grpunconv.8, lastlog.8, mkswap.8, nisdomainname.8, pwck.8,
	pwconv.8, pwunconv.8, ypdomainname.8
- update:
  o abook.1, dnsdomainname.1, hostname.1, mergelib.1x, nano.1, nano-tiny.1,
    pppoe-wrapper.1, tkpppoe.1, xawtv.1
  o aliases.5, iftab.5, nanorc.5, shadow.5
  o wireless.7
  o adsl-connect.8, adsl-setup.8, adsl-start.8, adsl-status.8, adsl-stop.8,
	hdparm.8, ifrename.8, iwconfig.8, iwevent.8, iwgetid.8, iwlist.8, iwpriv.8,
	iwspy.8, pam.8, rmmod.8

* Sat Sep 11 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-14mdk
- add:
  o switchdesk.1, xchat.1
  o ip6tables-restore.8, ip6tables-save.8, ip6tables.8
- update: iptables.8

* Fri Sep 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-13mdk
- fix conflict with wireless package
- add: abook.1, libtool.1, iftab.5, wireless.7, ifrename.8
- update:
  o nano.1, wget.1
  o nanorc.5
  o iwconfig.8, iwevent.8, iwgetid.8, iwlist.8, iwpriv.8, iwspy.8

* Fri Aug 27 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-12mdk
- add:
  o abc2abc.1, abc2midi.1, autoconf.1, automake.1, hostname.1, midi2abc.1
  o ethers.5
  o arp.8, ifconfig.8, mii-tool.8, nameif.8, plipconfig.8, rarp.8, route.8, slattach.8
- update: iptables.8, iptables-restore.8, iptables-save.8
- patch 7: fix many typos in epoll.4

* Sat Jul 31 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-11mdk
- add:
  o xf86cfg.1x
  o nsgmls.1, onsgmls.1, osgmlnorm.1, ospam.1, ospent.1, osx.1, sgmlnorm.1,
    spam.1, spent.1, sx.1
  o initscript.5

* Sat Jun 12 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-10mdk
o mergelib.1x, xf86config.1x, xsetmode.1x, xsetpointer.1x
  o addchnstr.3x, addchstr.3x, curs_addchstr.3x, mvaddchnstr.3x, mvaddchstr.3x,
    mvwaddchnstr.3x, mvwaddchstr.3x, waddchnstr.3x, waddchstr.3x
  o xhextris.6A
- update: showrgb.1x, showcfont.1, slocate.1
- locate.1 is now a alias of slocate.1

* Sat May 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-9mdk
- add: 
  o kbd_mode.1, showcfont.1, xmlif.1, xmlto.1, ybmtopbm.1, zeisstopnm.1
  o showrgb.1x
  o urpm.3
  o PAIR_NUMBER.3x, attr_get.3x, attr_off.3x, attr_on.3x, attr_set.3x,
	attroff.3x, attron.3x, attrset.3x, chgat.3x, color_set.3x, curs_attr.3x,
	mvchgat.3x, mvwchgat.3x, standend.3x, standout.3x, wattr_get.3x,
	wattr_off.3x, wattr_on.3x, wattr_set.3x, wattroff.3x, wattron.3x,
	wattrset.3x, wchgat.3x, wcolor_set.3x, wstandend.3x, wstandout.3x
  o install-catalog.8, kbd-compat.8

* Thu Apr 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-8mdk
- urpm* man pages were moved into urpmi package

* Tue Apr 06 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-7mdk
- fix conflict with new wireless-tools package
- add:
  o cvs.1, date.1, distcc.1, distccd.1, igal.1, joe.1, sitecopy.1, sitecopy.1,
    xscanimage.1
  o xferfaxlog.4f
  o at.allow.5, at.deny.5, sane-epson.5
  o iwevent.8, iwgetid.8, iwlist.8, iwpriv.8, iwspy.8, renice.8
- update: alsactl.1, alsamixer.1

* Tue Feb 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-6mdk
- add conflict tag in order to force package ordering so that updates get
  performed smoother
- update indent.1 and iwconfig.8

* Tue Feb 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-5mdk
- add dialog.1 and syslog.conf.5

* Sun Feb 08 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-4mdk
- update aplay.1 and eject.1
- add:
  o a2p.1, avimerge.1, indent.1, jade.1, openjade.1, pg_dump.1, pg_dumpall.1,
    rxvt.1, seq.1
  o aliases.5
  o debugreiserfs.8
  o logrotate.8, sysklogd.8, syslogd.8

* Sun Feb 08 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58.0-3mdk
- fix conflict with dpkg

