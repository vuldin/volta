Name:           volta
Version:        0.5.3
Release:        1%{?dist}
Summary:        The JavaScript Launcher ⚡

License:        BSD 2-CLAUSE
URL:            https://%{name}.sh
Source0:        https://github.com/volta-cli/volta/archive/v%{version}.tar.gz

# TODO - should require openssl?
Requires:       bash

# TODO
#BuildArch:

%description
Volta’s job is to manage your JavaScript command-line tools, such as node, npm, yarn, or executables shipped as part of JavaScript packages. Similar to package managers, Volta keeps track of which project (if any) you’re working on based on your current directory. The tools in your Volta toolchain automatically detect when you’re in a project that’s using a particular version of the tools, and take care of routing to the right version of the tools for you.


%prep
# this unpacks the tarball to the build root
%setup -q


# the binaries have already been built - they do not need to be re-built
#%build


# this installs into a chroot directory resembling the user's root directory
%install
# clean out the directory
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
# install the files from the tarball
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0755 shim %{buildroot}/%{_bindir}/shim


# TODO
%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/shim

%post
# TODO: this runs after install
echo "Volta installed successfully!!!!"


%changelog
* Thu May 30 2019 Michael Stewart <mikrostew@gmail.com> - 0.5.3-1
- First volta package
