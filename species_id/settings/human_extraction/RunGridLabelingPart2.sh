#!/bin/bash

EXPERIMENT_DIR=/data/mdesnoye/fish/experiments/human_extraction/grid_labeling2/

mkdir -p ${EXPERIMENT_DIR}

src/ExtractGridClassification.py \
--blob_dir /data/mdesnoye/fish/tank_videos/extracted_fish_newframeid/20110102/xmlBlobs \
--experiment_dir ${EXPERIMENT_DIR} \
--output_prefix grid_labeling \
--image_list /data/mdesnoye/fish/tank_videos/extracted_fish_newframeid/20110102/humanLabels.txt \
--neg_blob_list /data/mdesnoye/fish/tank_videos/extracted_fish_newframeid/20110102/negList.txt \
--num_neg_blobs 5.0 \
--shape_dict_filename /data/mdesnoye/fish/experiments/extraction081011/20110102/osurf.dict \
--use_opponent_surf \
--video_ids "['10-52-48-', '11-02-48-', '11-23-48-', '11-22-48-']" \
--random_seed 9836298 \
__log:=${EXPERIMENT_DIR}/rosout.log > ${EXPERIMENT_DIR}/stdout.log 2> ${EXPERIMENT_DIR}/stderr.log
