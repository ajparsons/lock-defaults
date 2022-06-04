#/bin/bash


if (curl -Ls https://pypi.org/pypi/$pythonPackage/json | grep "Error code 404")
then
    remoteExists=0
else
    remoteExists=1
fi

localVersion=$(poetry version --short)
diff=0

if [ $remoteExists -eq 1 ]
then
    latestVersion=$(curl -Ls https://pypi.org/pypi/$pythonPackage/json | jq -r .info.version)
    if [ "$localVersion" != "$latestVersion" ]
    then
        diff=1
    fi
fi

echo '::set-output version_difference::$diff'
echo '::set-output remote_exists::$remoteExists'