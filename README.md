# QualitativeLLM

QualitativeLLM is a Python project for using local LLMs for qualitative research.

## Repository structure

- conda - environment file for using anaconda navigator SDK
- input - inputs for the scripts
- output - output for the script
- scripts - three pythons scripts, using openai, ollama or anaconda ai SDK
- slurm - scripts to use on iridisx, including submission scripts

Note that `scripts/anaconda_main.py` doesn't work on Iridis X because there is no way to launch the Anaconda AI
Navigator GUI which is required for some reason. Also note that `scripts/openai_main.py` doesn't work on Iridis either,
because the compute nodes can't access the internet.

## Iridis X

It is possible to run a local LLM on Iridis X using Ollama, where Ollama 0.3.14 is installed. To install a specific
Ollama model, you can use the the `setup_ollama_model.sh` script with the name of model you wish to install. This should
be done on the login node, as these are the only nodes with an internet connection.

```shell
bash slurm/setup_ollama_model.sh rouge/qwen2-7b-instruct
```

Once the model is installed, a job can be submitted to a GPU node using either `slurm/iridisx_l4.slurm`,
`slurm/iridisx_a100.slurm` or `slurm/iridisx_h100.slurm`. All of these use the ECS SWARM cluster.

```shell
sbatch slurm/iridisx_l4.slurm rouge/qwen2-7b-instruct
```
