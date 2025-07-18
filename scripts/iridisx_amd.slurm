#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-node=1
#SBATCH --partition=amd
#SBATCH --mem=64G
#SBATCH --time=00:05:00

module load ollama conda
source activate qualitative_llm
nvidia-smi
ollama serve &
bash DOIT

