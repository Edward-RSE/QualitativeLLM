#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-node=1
#SBATCH --partition=a100
#SBATCH --time=00:01:00

nvidia-smi
module load ollama
ollama serve &

bash scripts/DOIT
