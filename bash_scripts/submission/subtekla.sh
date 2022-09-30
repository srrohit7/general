nowdir=`pwd`  nowdirk=${nowdir/teklahome\//} 

#ssh zlian@tekla2.iciq.es nowdir=`pwd`  nowdirk=${nowdir/teklahome\//} 'bash -s' << ENDSSH
ssh $username@tekla2.iciq.es 'bash -s' << ENDSSH
# commands to run on remote host
  cd $nowdirk;qsub run.sh
ENDSSH
