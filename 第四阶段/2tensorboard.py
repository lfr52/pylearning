from torch.utils.tensorboard import SummaryWriter
import cv2
writer = SummaryWriter('logs')

img_path = 'hymenoptera_data\\train\\bees\\16838648_415acd9e3f.jpg'
img = cv2.imread(img_path)
print(img.shape)
writer.add_image('test', img, 2, dataformats="HWC")
# # y = 2x
# for i in range(100):
#     writer.add_scalar('y=2x', 2 * i, i)

writer.close()