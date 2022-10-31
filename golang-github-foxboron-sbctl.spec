%bcond_without check
%global goipath         github.com/foxboron/sbctl
Version:                0.9
%global tag             0.9

%gometa -f

%global common_description %{expand:
sbctl intends to be a user-friendly secure boot key manager capable of
setting up secure boot, offer key management capabilities, and keep
track of files that needs to be signed in the boot chain.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           %{goname}
Release:        1%{dist}
Summary:        :computer: Secure Boot key manager
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: asciidoc

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs README.md
%{_bindir}/*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%gopkgfiles

%changelog
%autochangelog
