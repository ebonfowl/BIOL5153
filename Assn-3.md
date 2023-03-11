1. `rsync -r mt_genomes amcampit@hpc-portal2.hpc.uark.edu:/storage/amcampit`

2. `hpcstoragecp unknown.fa`, which runs this function on unknown.fa:  

```
hpcstoragecp () {
    file=$1
    destination=$2
    scp "$file" amcampit@hpc-portal2.hpc.uark.edu://scrfs/storage/amcampit/"$destination"  
}
```

3. Created the following slurm script and ran it with `sbatch assignment3.slurm`:

```
#!/bin/bash

#SBATCH --job-name=assignment3
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=1
#SBATCH --time=0:03:00
#SBATCH -o test_%j.out
#SBATCH -e test_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=amcampit@uark.edu

export OMP_NUM_THREADS=32

module purge
module load blast

cd /storage/amcampit/mt_genomes
# job command here

cat *.fasta > genomes.fas
makeblastdb -in genomes.fas -dbtype nucl
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn
```

4. `rsync -av amcampit@hpc-portal2.hpc.uar
k.edu:/storage/amcampit/mt_genomes .`

5. a) 00:00:02  
   b) Cucurbita  
   c) I don't really know anything about genetics, but I would assume Curcubita as it has the same number of bases (1584) as unknown.fa

6. Pushed with `git -u push origin main`