#global debug_package %{nil}
 
# https://github.com/89luca89/distrobox/issues/127
%global __brp_mangle_shebangs_exclude_from %{_bindir}/distrobox-(export|init)$

Name:    distrobox
Version: 1.4.1
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
 
install -d -m0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 docs/*.md %{buildroot}%{_docdir}/%{name}
 
# Move the icon 
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/1200x1200/apps
mv %{buildroot}%{_datadir}/icons/terminal-distrobox-icon.png \
   %{buildroot}%{_datadir}/icons/hicolor/1200x1200/apps
 
# Generate more icon sizes
for sz in 16 22 24 32 36 48 64 72 96 128 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  convert terminal-distrobox-icon.png -resize ${sz}x${sz} \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/terminal-distrobox-icon.png
done
 
%check
%{buildroot}%{_bindir}/%{name} list -V
for i in create enter export init list rm stop host-exec; do
    %{buildroot}%{_bindir}/%{name}-$i -V
done
 
 
%files
%license COPYING.md
%doc %{_docdir}/%{name}
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}*
%{_iconsdir}/hicolor/*x*/apps/terminal-distrobox-icon.png
%{_datadir}/bash-completion/completions/distrobox*
