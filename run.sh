echo "Run DOLG + cosface"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name dolg \
          --config_name dolg_b5_step3 \
          --trainCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/train.csv \
          --valCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/val.csv \
          --loss_name cosface 

echo "Run DOLG + arcface_dynamicmargin"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name dolg \
          --config_name dolg_b5_step3 \
          --trainCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/train.csv \
          --valCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/val.csv \
          --loss_name arcface_dynamicmargin

echo "Run DOLG + CE_smooth_loss"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name dolg \
          --config_name dolg_b5_step3 \
          --trainCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/train.csv \
          --valCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/val.csv \
          --loss_name CE_smooth_loss	

echo "Run DOLG + circleloss"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name dolg \
          --config_name dolg_b5_step3 \
          --trainCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/train.csv \
          --valCSVPath /content/drive/MyDrive/AIC_HCM/Image_Retrieval_from_Visual_Data/data/val.csv \
          --loss_name circleloss			  

		  