import random
new_file = open("0.1noise.txt","w+")
with open("list_patition_label.txt","r") as file:
	for line in file:
		line = line.strip()
		img_path, label = line.split(' ', 1)
		number = random.uniform(0,1)
		new_label = random.randint(1,7)
		if img_path.startswith("test"):
			new_file.write(img_path + ' ' + str(label) +'\n')
			continue
		if number <= 0.1:
			while(1):
				new_label = random.randint(1,7)
				if new_label != int(label):
					new_file.write(img_path + ' ' + str(new_label) +'\n')
					break
		else:
			new_file.write(img_path + ' ' + str(label) +'\n')