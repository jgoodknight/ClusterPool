#!/bin/sh

#SBATCH -n 1
#SBATCH -t 200
#SBATCH -p aspuru-guzik
#SBATCH --mem=2000

#SBATCH -o /n/regal/aspuru-guzik_lab/jgoodknight/primeTest.out
#SBATCH -e /n/regal/aspuru-guzik_lab/jgoodknight/primeTest.err

#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END


python testfile_primes.py