cd /usr/local/MATLAB/R2017b/bin
./matlab


python2环境激活
source /home/chengpeisong/py2env/bin/activate

python ros_lane_detect.py --model-path model_best_enet.pth

python2 ros_lane_detect.py --model-path model_best_enet.pth

python train.py --train-path home/data/tusimple/train_set/ --epoch 100 --batch-size 2 --lr 0.001 --img-size 224 224



/home/chengpeisong/Downloads/Codes-for-Lane-Detection-master/ERFNet-CULane-PyTorch/tools/prob2lines/output/output/vgg_SCNN_DULR_w9_iou0.5_split.txt



ERFNet训练与测试

cd /home/chengpeisong/Downloads/Codes-for-Lane-Detection-master/ERFNet-CULane-PyTorch

sh ./train_erfnet_auxloss.sh

测试

sh ./test_erfnet_auxloss.sh

matlab里面进行main.m

进入 cd tools/lane_evaluation

     make

     sh Run.sh

tensorboard --logsir="trained/02/0329/"
