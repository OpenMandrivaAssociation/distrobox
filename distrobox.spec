#global debug_package %{nil}
%define _empty_manifest_terminate_build 0
 
# https://github.com/89luca89/distrobox/issues/127
%global __brp_mangle_shebangs_exclude_from %{_bindir}/distrobox-(export|init)$

Name:    distrobox
Version: 1.7.2.1
Release: 1
Summary: Another tool for containerized command line environments on Linux 
License: GPLv3
URL:     https://github.com/89luca89/distrobox/
Source0:  https://github.com/89luca89/distrobox/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildArch: noarch

BuildRequires: imagemagick

Requires: (podman or %{_bindir}/docker)
Requires: %{_bindir}/basename
Requires: %{_bindir}/find
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
 
%description
Use any linux distribution inside your terminal. Distrobox uses podman 
or docker to create containers using the linux distribution of your 
choice. Created container will be tightly integrated with the host, 
allowing to share the HOME directory of the user, external storage, 
external usb devices and graphical apps (X11/Wayland) and audio.
 
%prep
%autosetup -p1
%build
 
%install
./install -P %{buildroot}/%{_prefix}
 
%check
%{buildroot}%{_bindir}/%{name} list -V
for i in create enter export init list rm stop host-exec; do
    %{buildroot}%{_bindir}/%{name}-$i -V
done
 
 
%files
%license COPYING.md
#doc %{_docdir}/%{name}
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}*
%{_iconsdir}/hicolor/*x*/apps/terminal-distrobox-icon.png
%{_datadir}/icons/hicolor/scalable/apps/terminal-distrobox-icon.svg
%{_datadir}/bash-completion/completions/distrobox*
%{_datadir}/zsh/site-functions/
