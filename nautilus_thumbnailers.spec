%define rel 7

Summary: A collection of scripts that create thumbnails for files
Name: nautilus_thumbnailers
Version: 0.0.3
Release: %mkrel %rel
License: GPL
Group: File tools
Source: http://www.flyn.org/projects/nautilus_thumbnailers/%name.tar.bz2
Patch: nautilus_thumbnailers-0.0.3-with-gimp-2.3.patch
URL: http://www.flyn.org/projects/nautilus_thumbnailers/index.html
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
rm -rf %buildroot
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas thumbnailer

%preun
%preun_uninstall_gconf_schemas thumbnailer

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/thumbnailer.schemas
%{_bindir}/abiword-thumbnailer
%{_bindir}/dia-thumbnailer
%{_bindir}/gimp-thumbnailer
%{_bindir}/gs-thumbnailer
%{_bindir}/vfstofs
%{_mandir}//man1/nautilus_thumbnailers.1*
