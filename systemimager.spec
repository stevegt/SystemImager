%define name     systemimager
%define ver      2.0.1
%define rel      1
%define prefix   /usr

Summary: Software that automates Linux installs, software distribution, and production deployment.
Name: %name
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
Source: http://download.sourceforge.net/systemimager/%{name}-%{ver}.tar.gz
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Brian Finley <brian@baldguysoftware.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Distribution: System Installation Suite
Requires: rsync >= 2.4.6, syslinux >= 1.48, libappconfig-perl, dosfstools, /usr/bin/perl
AutoReqProv: no

%description
This is bogus and not used anywhere

%package server
Summary: Software that automates Linux installs, software distribution, and production deployment.
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Brian Finley <brian@baldguysoftware.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Distribution: System Installation Suite
Requires: rsync >= 2.4.6, syslinux >= 1.48, systemimager-common, libappconfig-perl, dosfstools, /usr/bin/perl
AutoReqProv: no

%description server
SystemImager is software that automates Linux installs, software 
distribution, and production deployment.  SystemImager makes it easy to
do installs, software distribution, content or data distribution, 
configuration changes, and operating system updates to your network of 
Linux machines. You can even update from one Linux release version to 
another!  It can also be used to ensure safe production deployments.  
By saving your current production image before updating to your new 
production image, you have a highly reliable contingency mechanism.  If
the new production enviroment is found to be flawed, simply roll-back 
to the last production image with a simple update command!  Some 
typical environments include: Internet server farms, database server 
farms, high performance clusters, computer labs, and corporate desktop
environments.

The server package contains those files needed to run a SystemImager
server.

%package common
Summary: Software that automates Linux installs, software distribution, and production deployment.
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Brian Finley <brian@baldguysoftware.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Distribution: System Installation Suite
Requires: /usr/bin/perl
AutoReqProv: no

%description common
SystemImager is software that automates Linux installs, software 
distribution, and production deployment.  SystemImager makes it easy to
do installs, software distribution, content or data distribution, 
configuration changes, and operating system updates to your network of 
Linux machines. You can even update from one Linux release version to 
another!  It can also be used to ensure safe production deployments.  
By saving your current production image before updating to your new 
production image, you have a highly reliable contingency mechanism.  If
the new production enviroment is found to be flawed, simply roll-back 
to the last production image with a simple update command!  Some 
typical environments include: Internet server farms, database server 
farms, high performance clusters, computer labs, and corporate desktop
environments.

The common package contains files common to SystemImager clients 
and servers.

%package i386boot
Summary: Software that automates Linux installs, software distribution, and production deployment.
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Brian Finley <brian@baldguysoftware.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Distribution: System Installation Suite
Requires: systemimager-server
AutoReqProv: no

%description i386boot
SystemImager is software that automates Linux installs, software 
distribution, and production deployment.  SystemImager makes it easy to
do installs, software distribution, content or data distribution, 
configuration changes, and operating system updates to your network of 
Linux machines. You can even update from one Linux release version to 
another!  It can also be used to ensure safe production deployments.  
By saving your current production image before updating to your new 
production image, you have a highly reliable contingency mechanism.  If
the new production enviroment is found to be flawed, simply roll-back 
to the last production image with a simple update command!  Some 
typical environments include: Internet server farms, database server 
farms, high performance clusters, computer labs, and corporate desktop
environments.

The i386boot package provides specific kernel, ramdisk, and fs utilities
to boot and install i386 machines during the SystemImager autoinstall
process.

%package client
Summary: Software that automates Linux installs, software distribution, and production deployment.
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Brian Finley <brian@baldguysoftware.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Distribution: System Installation Suite
Requires: systemimager-common, systemconfigurator, libappconfig-perl, rsync >= 2.4.6, /usr/bin/perl
AutoReqProv: no

%description client
SystemImager is software that automates Linux installs, software 
distribution, and production deployment.  SystemImager makes it easy to
do installs, software distribution, content or data distribution, 
configuration changes, and operating system updates to your network of 
Linux machines. You can even update from one Linux release version to 
another!  It can also be used to ensure safe production deployments.  
By saving your current production image before updating to your new 
production image, you have a highly reliable contingency mechanism.  If
the new production enviroment is found to be flawed, simply roll-back 
to the last production image with a simple update command!  Some 
typical environments include: Internet server farms, database server 
farms, high performance clusters, computer labs, and corporate desktop
environments.

The client package contains the files needed on a machine for it to
be imaged by a SystemImager server.

%changelog
* Wed Dec  5 2001 Sean Dague <sean@dague.net> 2.0.1-1
- Update SystemImager version
- Changed prefix to /usr
- Made seperate i386boot package

* Mon Nov  5 2001 Sean Dague <sean@dague.net> 2.0.0-4
- Added build section for true SRPM ability

* Mon Oct  28 2001 Sean Dague <sean@dague.net> 2.0.0-3
- Added common package

* Sat Oct 20 2001  Sean Dague <sean@dague.net> 2.0.0-2
- Recombined client and server into one spec file

* Thu Oct 18 2001 Sean Dague <sean@dague.net> 2.0.0-1
- Initial build
- Based on work by Ken Segura <ksegura@5o7.org>

%prep
%setup

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/
make all

%install
cd $RPM_BUILD_DIR/%{name}-%{version}/
make install_server_all DESTDIR=/tmp/%{name}-%{ver}-root USR=/tmp/%{name}-%{ver}-root%prefix
make install_client_all DESTDIR=/tmp/%{name}-%{ver}-root USR=/tmp/%{name}-%{ver}-root%prefix

%clean
cd $RPM_BUILD_DIR/%{name}-%{version}/
make distclean
rm -rf $RPM_BUILD_ROOT

%post server
chkconfig --add systemimager


%preun server
chkconfig --del systemimager

%files common
%defattr(-, root, root)
%prefix/bin/lsimage
%prefix/share/man/man8/lsimage*
%dir %prefix/lib/systemimager
%prefix/lib/systemimager/perl/SystemImager/Common.pm

%files i386boot
%defattr(-, root, root)
%dir %prefix/share/systemimager/i386-boot
%prefix/share/systemimager/i386-boot/*

%files server
%defattr(-, root, root)
%doc CHANGE.LOG COPYING CREDITS README TODO VERSION
%doc doc/manual/systemimager* doc/manual/html doc/manual/examples
%doc doc/autoinstall* doc/local.cfg
%dir /var/log/systemimager
%dir /var/lib/systemimager/images
%dir /var/lib/systemimager/scripts
%dir /etc/systemimager
%config /etc/systemimager/rsyncd.conf
%config /etc/systemimager/systemimager.conf
/etc/init.d/systemimager
/var/lib/systemimager/images/*
%prefix/sbin/addclients
%prefix/sbin/cpimage
%prefix/sbin/getimage
%prefix/sbin/mkautoinstallscript
%prefix/sbin/mkbootserver
%prefix/sbin/mkdhcpserver
%prefix/sbin/mkdhcpstatic
%prefix/sbin/mvimage
%prefix/sbin/pushupdate
%prefix/sbin/rmimage
%prefix/bin/mkautoinstall*
%prefix/lib/systemimager/perl/SystemImager/Server.pm
%prefix/share/man/man8/addclients*
%prefix/share/man/man8/cpimage*
%prefix/share/man/man8/getimage*
%prefix/share/man/man8/mk*
%prefix/share/man/man8/mvimage*
%prefix/share/man/man8/rmimage*

%files client
%defattr(-, root, root)
%doc CHANGE.LOG COPYING CREDITS README TODO VERSION
%dir /etc/systemimager
%config /etc/systemimager/updateclient.local.exclude
# %prefix/lib/systemimager/perl/SystemImager/Client.pm
%prefix/sbin/updateclient
%prefix/sbin/prepareclient
%prefix/share/man/man8/updateclient*
%prefix/share/man/man8/prepareclient*

