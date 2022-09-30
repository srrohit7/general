# Written by Ranga Rohit Seemakurthi and Zan Lian 06-09-22

Please replace $username with your tekla username and $mn_id with marenostrum id. You can do this easily using the find and replace command on vi. :%s/$username/yourusername/g 

#VASP input files 

Checklist for VASP beginners http://aliga.iciq.es/wiki/index.php/VASP_beginners    

Useful scripts for generating run and potcar files automatically. You can also modify the vdw tags in INCAR using this scripts 

Please refer to the wiki links for more information  

http://aliga.iciq.es/wiki/index.php/Scripts_for_VASP 

for making run.sh file, use rungen and savecalc scripts: http://aliga.iciq.es/wiki/index.php/Rungen  

for making KPOINTS file use kpgen , http://aliga.iciq.es/wiki/index.php/Kpoints 

for making POTCAR file use pos2pot.py and potgenPBE5.3, http://aliga.iciq.es/wiki/index.php/Potgen 

for making vdw parameters (DFT-D2 parameters from our group) in INCAR file, use vdw POSCAR (first copy vdw and vdw-data to your bin)  

 
