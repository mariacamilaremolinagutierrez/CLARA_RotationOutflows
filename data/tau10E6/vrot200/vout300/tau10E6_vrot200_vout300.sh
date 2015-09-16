#!/bin/sh
#PBS -q batch
#PBS -N tau10E6_vrot200_vout300
#PBS -l mem=128mb
#PBS -l nodes=1:ppn=12
#PBS -M mc.remolina197@uniandes.edu.co
#PBS -m abe

module load openmpi/1.8.5
cd /lustre/home/ciencias/fisica/pregrado/mc.remolina197/github/CLARA-MPI/src/
mpiexec -n 12 ./mine.x /lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E6/vrot200/vout300/tau10E6_vrot200_vout300.input