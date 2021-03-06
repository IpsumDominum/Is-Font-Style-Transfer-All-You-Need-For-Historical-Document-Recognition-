# Model training

### Preparing the data for training.

Please put generated data, the "Style_Transfer_Data" folder, into this directory for style transfer training.
Put "segmented" and labels, (rename "labels.pkl" as "train_labels.pkl") and put in data folder for lstm and attend_show_and_tell training.

### Train models
```
python train --['lstm','style','attend'] --checkpoint_num
```
#ie:
```
python lstm 0
```

When checkpoint_num == 0, the model trains from scratch.

### Test models

Put model checkpoints into models/folder, where folder is "LSTMONLY", for instance.
Then run
```
python test --['lstm','style','attend'] --checkpoint_num
```

### CPU and GPU 
Please edit train.py and test.py and comment out the suitable lines specifying the device.

### Loss Curve
The current training parameters will probably overfit... 
![loss](loss.PNG)

### Visual Results
![v_1](v_1.PNG)
![v_2](v_2.PNG)
![v_3](v_3.PNG)
![v_4](v_4.PNG)

