
cd ..
CUDA_VISIBLE_DEVICES=2,3 python train_dota.py \
./configs/DOTA_hbb/retinanet_r50_fpn_2x_dota_org_fix.py \
--gpus 2 \
--no-validate \
--work-dir ./results/retinanet_hbb_tv_org_fix

