#!/bin/bash

#SBATCH --time=01:00:00
#SBATCH --partition=amd
#SBATCH --mem=16G
#SBATCH --ntasks=1
#SBATCH --nodes=1


# 0.3.14 takes ~300 seconds to start the llama runner
module load ollama/0.3.14
# 0.9.5 hangs after starting the llama runner (~few seconds), doesn't generate a response
# module load ollama/0.9.5
ollama serve &

sleep 15

status_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:11434)

if [ "$status_code" -eq 200 ]; then
    curl -s http://localhost:11434/api/generate -d \
        '{"model": "rouge/qwen2-7b-instruct", "prompt": "What is the capital of France?", "stream": false}'
else
    echo "Ollama server did not start."
fi

