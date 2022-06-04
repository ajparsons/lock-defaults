#/bin/bash


if (curl -Ls https://pypi.org/pypi/$pythonPackage/json | grep "Error code 404")
then
    remoteExists=0
else
    remoteExists=1
fi

localVersion=$(python -m poetry version --short)
diff=0

if [ $remoteExists -eq 1 ]
then
    latestVersion=$(curl -Ls https://pypi.org/pypi/$pythonPackage/json | jq -r .info.version)
    if [ "$localVersion" != "$latestVersion" ]
    then
        diff=1
    fi
fi

if [ $diff -eq 1 ]
then
    echo '::set-output name=version_difference::true'
else
    echo '::set-output name=version_difference::false'
fi

if [ $remoteExists -eq 1 ]
then
    echo '::set-output name=remote_exists::true'
else
    echo '::set-output name=remote_exists::false'
fi