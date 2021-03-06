Summary:	Colubrid - lightweight WSGI publisher
Summary(pl.UTF-8):	Colubrid - lekki moduł do publikowania WSGI
Name:		python-Colubrid
Version:	0.10
Release:	4
Group:		Development/Languages/Python
License:	GPL
Source0:	http://wsgiarea.pocoo.org/colubrid/dist/Colubrid-%{version}.tar.gz
# Source0-md5:	ce52e81d8971a22064e1418064dcb700
URL:		http://wsgiarea.pocoo.org/colubrid/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools >= 0.6-0.a9.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Colubrid is a WSGI publisher which simplifies Python web developement.
If you've ever created a WSGI application without a framework of an
request handler you know how hard this can be. For the full feature
list have a look at the Features
(http://wsgiarea.pocoo.org/colubrid/features/) page.

%description -l pl.UTF-8
Colubrid to moduł do publikowania WSGI ułatwiający tworzenie WWW w
Pythonie. Ci, którzy stworzyli kiedykolwiek aplikację WSGI bez
szkieletu procedury obsługi żądań, wiedzą, jakie to może być trudne.
Pełna lista możliwości jest na stronie Features
(http://wsgiarea.pocoo.org/colubrid/features/).

%prep
%setup -q -n Colubrid-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir}/colubrid -name \*.py -exec rm -f \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/Colubrid*
%{py_sitescriptdir}/colubrid*
