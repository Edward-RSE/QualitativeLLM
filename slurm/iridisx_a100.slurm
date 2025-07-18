#!/bin/bash

#SBATCH --time=00:05:00
#SBATCH --partition=swarm_a100
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --gres=gpu:1

# Load Ollama 0.3.14 and start server
# Note that 0.9.5 hangs during response generation
module load conda
module load ollama/0.3.14
ollama serve &

source activate qualitative_llm
bash DOIT $1
