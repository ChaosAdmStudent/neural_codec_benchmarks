#!/bin/bash

#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=64G
#SBATCH --time=05:00:00
#SBATCH -J dcvc_training
#SBATCH --partition=gpunodes
#SBATCH --nodelist=gpunode7
#SBATCH --gres=gpu:rtx_4090:1
#SBATCH --output=training_output_%N.out
#SBATCH --error=training_output_%N.err

conda init 
conda activate dcvc
export CUDA_PATH=/usr/local/cuda/bin

python test_video.py   --i_frame_model_name cheng2020-anchor   --i_frame_model_path checkpoints/cheng2020-anchor-3-e49be189.pth.tar   --test_config dataset_config_example.json   --cuda true   --cuda_device 0   --worker 1   --output_json_result_path DCVC_result_psnr.json   --model_type psnr   --recon_bin_path recon_bin_folder_psnr   --model_path checkpoints/model_dcvc_quality_0_psnr.pth