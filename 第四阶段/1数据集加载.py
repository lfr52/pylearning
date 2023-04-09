from torch.utils.data import Dataset
import cv2
import os

class mydata(Dataset):
    def __init__(self, root_dir, label_dir):
        super().__init__()
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path) # 路径下的图片文件名称放到一个列表中



    def __getitem__(self, index):
        img_name = self.img_path[index]
        img_item_path = os.path.join(self.path, img_name)
        img = cv2.imread(img_item_path)
        label = self.label_dir
        return img, label
    
    def __len__(self):
        return len(self.img_path)

ants_dataset = mydata('hymenoptera_data\\train', 'ants')
bees_dataset = mydata('hymenoptera_data\\train', 'bees')

train_dataset = ants_dataset + bees_dataset

print(ants_dataset)
print(ants_dataset[0])
img,_ = ants_dataset[0]

cv2.imshow('pic', img)
cv2.waitKey()