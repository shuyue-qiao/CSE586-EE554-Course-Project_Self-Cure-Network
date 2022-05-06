# CSE586-EE554-Course-Project_Self-Cure-Network

**Abstract**

The **imgs** file gives the proposed method pipeline of SCN. The **src** file has the **train.py** which is used to do training by using the dataset and **image_utils.py** is used for data augmentation. The **generate.py** file is used to add noisees to the dataset

**Train and Test**

After downloading all files, create the path to dataset. For RAD-DB dataset it needs to have the following structure: 
 ```
- datasets/raf-basic/
         EmoLabel/
             list_patition_label.txt
         Image/aligned/
	     train_00001_aligned.jpg
             test_0001_aligned.jpg
             ...
```             
**Run**
- Python train.py 


Reference:
https://arxiv.org/pdf/2002.10392.pdf.<br />
https://github.com/kaiwang960112/Self-Cure-Network. <br />
About the dataset, here is the link of how to get Real-world Affective Faces Database(RAF-DB): http://www.whdeng.cn/RAF/model1.html#dataset 

