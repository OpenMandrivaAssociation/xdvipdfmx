Summary: An extended version of DVIPDFMx with support for XeTeX output
Name: xdvipdfmx
Version: 0.4
Release: %mkrel 1
License: GPLv2+
Group: Publishing
Source: http://scripts.sil.org/svn-view/xdvipdfmx/TAGS/xdvipdfmx-%{version}.tar.gz
URL: http://scripts.sil.org/xetex_linux

Requires: tex(tex), dvipdfmx
# dvipdfmx is required because some data files are shared
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

# to build, we need various -devel packages...
BuildRequires: fontconfig-devel, freetype-devel, libpng-devel, zlib-devel, kpathsea-devel, libpaper-devel

%description
xdvipdfmx is an output driver for the XeTeX typesetting system.
It is an extended version of DVIPDFMx by Jin-Hwan Cho and Shunsaku Hirata,
which is itself an extended version of dvipdfm by Mark A. Wicks.
This driver converts XDV (extended DVI) output from the xetex program
into standard PDF that can be viewed or printed.

# # # # # # # # # #
# PREP
# # # # # # # # # #

%prep

# setup macro does standard clean-and-unpack
%setup -q

# # # # # # # # # #
# BUILD
# # # # # # # # # #

%build
chmod +x configure
%configure2_5x --with-freetype2=`freetype-config --prefix` 
make %{?_smp_mflags}

# # # # # # # # # #
# INSTALL
# # # # # # # # # #

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# # # # # # # # # #
# FILE LIST
# # # # # # # # # #

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/xdvipdfmx
%doc README AUTHORS BUGS COPYING TODO doc/tug2003.pdf index.html *.css

