#!/bin/bash
echo "Hello and welcome to the script!"

firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo "You are building version" $version

echo "Do you want to continue? (Enter 1 to continue or 0 to exit.)"
read versioncontinue

if [ $versioncontinue -eq 1 ]
then
  echo "OK"
  for filename in source/*
  do
    echo $filename
    if [$filename=="source/secretinfo.md"]
    then
      echo $filename " is not being copied"
    else
      echo "Copying " $filename
      cp $filename build/.
    fi
  done
  cd build/
  echo "Build version $version contains:"
  ls
  cd ..
else
  echo "Please come back when you are ready"
fi
