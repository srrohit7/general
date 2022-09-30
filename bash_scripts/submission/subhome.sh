nowdir=`pwd`  nowdirk=${nowdir/"home/$username/m-mn-home"\//} maredir=/home/iciq72/$mn_user_id${nowdirk}

ssh $mn_user_id@mn2.bsc.es 'bash -s' << ENDSSH
# commands to run on remote host
  cd $maredir;sbatch run.sh
ENDSSH
