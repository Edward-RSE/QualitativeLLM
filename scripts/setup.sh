#!/bin/bash

module purge       &> /dev/null 
module load ollama &> /dev/null

ollama pull qwen2:7b

