Summary: A collection of scripts that create thumbnails for files
Name: nautilus_thumbnailers
Version: 0.0.3
Release: 10
License: GPL
Group: File tools
Source: http://www.flyn.org/projects/nautilus_thumbnailers/%name.tar.bz2
Patch: nautilus_thumbnailers-0.0.3-with-gimp-2.3.patch
URL: https://www.flyn.org/projects/nautilus_thumbnailers/index.html
BuildArch: noarch
Requires: nautilus
Requires: dia
Requires: gimp >= 2.3
Requires: ghostscript
BuildRequires: GConf2
Requires(post): GConf2
Requires(postun): GConf2

%description
This package provides scripts to generate thumbnails for several file 
formats commonly used in the GNOME environment. When using these 
scripts with the nautilus file manager, for example, icons for PDF 
files will present the same appearance as the document itself. This 
has long been the case with images, but this package extends this 
technique to formats like PDF, PostScript and GIMP XCF.

%prep
%setup -q
%patch -p1 -b .gimp

%build
./configure --prefix=%_prefix --libdir=%_libdir --disable-schemas-install
%make

%install
%makeinstall

%preun
%preun_uninstall_gconf_schemas thumbnailer

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/thumbnailer.schemas
%{_bindir}/abiword-thumbnailer
%{_bindir}/dia-thumbnailer
%{_bindir}/gimp-thumbnailer
%{_bindir}/gs-thumbnailer
%{_bindir}/vfstofs
%{_mandir}//man1/nautilus_thumbnailers.1*


%changelog
* Mon Jul 25 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.0.3-8mdv2012.0
+ Revision: 691512
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.0.3-7mdv2011.0
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.0.3-7mdv2008.0
+ Revision: 57440
- spec fixes
- Import nautilus_thumbnailers



* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.0.3-1mdv2007.0
- Rebuild

* Thu Dec  8 2005 Götz Waschk <waschk@mandriva.org> 0.0.3-6mdk
- replace prereq
- update patch for gimp 2.3
- mkrel

* Tue Dec  7 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.3-5mdk
- use gimp2_2

* Wed Oct  6 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.3-4mdk
- oops, gimp2_0

* Tue Oct  5 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.3-3mdk
- use gimp 2.0 (Laurent Mouillart)

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.3-2mdk
- build fix

* Sun Nov  9 2003 Götz Waschk <waschk@linux-mandrake.com> 0.0.3-1mdk
- add abiword thumbnailer
- new version

* Mon Oct 27 2003 Götz Waschk <waschk@linux-mandrake.com> 0.0.2-2mdk
- fix buildrequires

* Mon Oct 27 2003 Götz Waschk <waschk@linux-mandrake.com> 0.0.2-1mdk
- new version

* Tue Sep  2 2003 Götz Waschk <waschk@linux-mandrake.com> 0.0.1-2mdk
- fix schema uninstallation

* Mon Sep  1 2003 Götz Waschk <waschk@linux-mandrake.com> 0.0.1-1mdk
- initial package
