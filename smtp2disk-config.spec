Name:           smtp2disk-config
Version:        2
Release:        0%{?dist}
Summary:        A user for queing the SMTP messages to disk instead of delivery.

Group:          Development/Libraries
License:        BSD
URL:            http://127.0.0.1
Source0:        http://127.0.0.1/smtp2disk-config-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	smtp2disk-user
Requires:	postfix
Requires:	procmail
Requires:	emailAddress2Folder >= 2
BuildRequires:	smtp2disk-user

BuildArch:      noarch


%description 
This creates the smtp2disk user account, required by other programs.

%prep
%setup -q -c smtp2disk-config-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS=vendor
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "$RPM_BUILD_ROOT/home/smtp2disk/Maildir/"
cp .forward "$RPM_BUILD_ROOT/home/smtp2disk/.forward"
cp .procmailrc "$RPM_BUILD_ROOT/home/smtp2disk/.procmailrc"

#make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
#find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
#find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
#chmod -R u+w $RPM_BUILD_ROOT/*

#for file in Changes; do
#  iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
#  mv -f "${file}_" "$file"
#done


%clean 
rm -rf $RPM_BUILD_ROOT

%post
chmod go+rx ~smtp2disk/


%files
%defattr(644,smtp2disk,smtp2disk,755)
/home/smtp2disk/.forward
/home/smtp2disk/.procmailrc
/home/smtp2disk/Maildir/


%changelog
* Sun Jan 28 2018 Jason Pyeron <support@pdinc.us> - 2-0
- leverage TO/FROM foldering

* Tue May 28 2013 Jason Pyeron <support@pdinc.us> - 1-1
- make home dir readable

* Tue May 28 2013 Jason Pyeron <support@pdinc.us> - 1-0
- initial build

