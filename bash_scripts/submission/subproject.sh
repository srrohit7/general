nowdir=`pwd`  nowdirk=${nowdir/"home/$username/p-mn-projects"\//} maredir=/gpfs/projects/iciq72${nowdirk}

ssh $mn_user_id@mn2.bsc.es 'bash -s' << ENDSSH
# commands to run on remote host
  cd $maredir;sbatch run.sh
ENDSSH
