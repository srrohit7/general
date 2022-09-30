#!/usr/bin/env python 
# by Konstantin
# adapted from shifu Qiang
# 7 Avg 2019
#################################################################################
#  									       	 #
# Read your POSCAR and generate POTCAR with pseudopotentials redomended by VASP #
#										 #	
#################################################################################

import subprocess
print("***"*10)
print("Removing OLD POTCAR...")
print("***"*10)
subprocess.call("rm POTCAR", shell = True)
print("Generating NEW POTCAR...")
print("***"*10)
f = open ("POSCAR", mode='r')
pos_elem = f.readlines()[5].split()
elem = ""
for i in pos_elem:
 if i == "Li":
  elem += "Li_sv "
 elif i == "Na":
  elem += "Na_pv "
 elif i == "K":
  elem += "K_sv "
 elif i == "Ca":
  elem += "Ca_sv "
 elif i == "Sc":
  elem += "Sc_sv "
 elif i == "Ti":
  elem += "Ti_sv "
 elif i == "V":
  elem += "V_sv "
 elif i == "Cr":
  elem += "Cr_pv "
 elif i == "Mn":
  elem += "Mn_pv "
 elif i == "Ga":
  elem += "Ga_d "
 elif i == "Ge":
  elem += "Ge_d "
 elif i == "Rb":
  elem += "Rb_sv "
 elif i == "Sr":
  elem += "Sr_sv "
 elif i == "Y":
  elem += "Y_sv "
 elif i == "Zr":
  elem += "Zr_sv "
 elif i == "Nb":
  elem += "Nb_sv "
 elif i == "Mo":
  elem += "Mo_sv "
 elif i == "Tc":
  elem += "Tc_pv "
 elif i == "Ru":
  elem += "Ru_pv "
 elif i == "Rh":
  elem += "Rh_pv "
 elif i == "In":
  elem += "In_d "
 elif i == "Sn":
  elem += "Sn_d "
 elif i == "Cs":
  elem += "Cs_sv "
 elif i == "Ba":
  elem += "Ba_sv "
 elif i == "Pr":
  elem += "Pr_3 "
 elif i == "Nd":
  elem += "Nd_3 "
 elif i == "Pm":
  elem += "Pm_3 "
 elif i == "Sm":
  elem += "Sm_3 "
 elif i == "Eu":
  elem += "Eu_2 "
 elif i == "Gd":
  elem += "Gd_3 "
 elif i == "Tb":
  elem += "Tb_3 "
 elif i == "Dy":
  elem += "Dy_3 "
 elif i == "Ho":
  elem += "Ho_3 "
 elif i == "Er":
  elem += "Er_3 "
 elif i == "Tm":
  elem += "Tm_3 "
 elif i == "Yb":
  elem += "Yb_2 "
 elif i == "Lu":
  elem += "Lu_3 "
 elif i == "Hf":
  elem += "Hf_pv "
 elif i == "Ta":
  elem += "Ta_pv "
 elif i == "W":
  elem += "W_pv "
 elif i == "Tl":
  elem += "Tl_d "
 elif i == "Pb":
  elem += "Pb_d "
 elif i == "Bi":
  elem += "Bi_d "
 elif i == "Po":
  elem += "Po_d "
 elif i == "At":
  elem += "At_d "
 elif i == "Fr":
  elem += "Fr_sv "
 elif i == "Ra":
  elem += "Ra_sv "
 else:
  elem = elem + i + " "
subprocess.call("potgenpbe5.3 " + elem, shell = True)
f.close()
print("Done")
print("***"*10)
print('NEW POTCAR containes .....')
print("***"*10)
subprocess.call("grep TIT POTCAR| awk '{print $4}' | xargs -n100", shell = True)
print("***"*10)
print("Elements in POSCAR") 
print("***"*10)
subprocess.call("sed -n 6p POSCAR", shell = True)
