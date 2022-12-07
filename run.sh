echo "Run swin + cosface"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name swin \
          --config_name swin_224_b3 \
          --trainCSVPath data/train.csv \
          --valCSVPath data/val.csv \
          --loss_name cosface 

echo "Run swin + arcface_dynamicmargin"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name swin \
          --config_name swin_224_b3 \
          --trainCSVPath data/train.csv \
          --valCSVPath data/val.csv \
          --loss_name arcface_dynamicmargin

echo "Run swin + CE_smooth_loss"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name swin \
          --config_name swin_224_b3 \
          --trainCSVPath data/train.csv \
          --valCSVPath data/val.csv \
          --loss_name CE_smooth_loss	

echo "Run swin + circleloss"
python -u -m torch.distributed.launch --nproc_per_node=1 \
          train.py \
          --model_name swin \
          --config_name swin_224_b3 \
          --trainCSVPath data/train.csv \
          --valCSVPath data/val.csv \
          --loss_name circleloss			  

		  