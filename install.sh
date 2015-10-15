#! /bin/bash

chmod +x ./cmdmine

DIR=$HOME/.cmdmine

if [ ! -d "$DIR" ]; then
  mkdir $DIR
  touch $DIR/macros.dat
  touch $DIR/activities.log
  cp cmdmine $DIR/cmdmine
  echo "Created $DIR";

  if [ -d "$HOME/bin" ]; then
    ln -s $DIR/cmdmine $HOME/bin/cmdmine
  else
    echo "export PATH=$DIR:\$PATH" >> $HOME/.profile
    source $HOME/.profile
  fi
fi

cp config.json $DIR

echo "Installation complete!"
