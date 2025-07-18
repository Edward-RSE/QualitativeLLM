#!/bin/bash

module purge              &> /dev/null
module load ollama/0.3.14 &> /dev/null
ollama pull $@
