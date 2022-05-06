# CSE586-EE554-Course-Project_Self-Cure-Network
We used **kaiwang960112**'s self cure network as a reference to achive this work. <br />
Here is the link to his work site: https://github.com/kaiwang960112/Self-Cure-Network. <br />
And here is the link to their paper: https://arxiv.org/pdf/2002.10392.pdf.<br />
About the dataset, here is the link of how to get Real-world Affective Faces Database(RAF-DB): http://www.whdeng.cn/RAF/model1.html#dataset 




**Abstract**

Based on kaiwang960112's work, we modify **train.py**, **generate.py**, and **image_utils.py** a little bit to fit with the dataset that we got from him. In this work, we only use RAF-DB to replicate his work.
The **imgs** file gives the proposed method pipeline of SCN. The **src** file has the **train.py** which is used to do training by using the dataset and **image_utils.py** is used for data augmentation. The **generate.py** file is used to add noisees to the dataset

**Train and Test**
- According **kaiwang960112**,

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
