# QualitativeLLM

QualitativeLLM is a Python project for using local LLMs for qualitative research.

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
