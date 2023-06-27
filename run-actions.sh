#!/bin/bash
cd /home/petar/rasa-singi-upis
source /home/petar/anaconda3/etc/profile.d/conda.sh
conda activate rasabot
rasa run actions
