#! /bin/bash

if [ "$(whoami)" != "root" ]; then
  echo -e "This install script must be run as root. Please try again with 'sudo $0'"
  exit 0;
fi

DIR=$HOME/.cmdmine

if [ ! -d "$DIR" ]; then
  mkdir $DIR
  touch $DIR/macros.dat
  chmod a+rw $DIR/macros.dat
  touch $DIR/activities.log
  chmod a+rw $DIR/activities.log
  echo "Created $DIR";
fi

cp config.json $DIR
chmod a+rw $DIR/config.json
chmod +x cmdmine
cp cmdmine /usr/bin

echo "Installation complete!"
