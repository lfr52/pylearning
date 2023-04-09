from torchvision import transforms
from PIL import Image
from torch.utils.tensorboard import SummaryWriter


# # transforms.ToTensor的使用
# img_path = 'hymenoptera_data\\train\\bees\\16838648_415acd9e3f.jpg'
# img = Image.open(img_path)
# # print(img)
# writer = SummaryWriter('logs_3')
# tensor_trans = transforms.ToTensor()
# tensor_img = tensor_trans(img)
# # print(tensor_img)
# writer.add_image('tensor_img', tensor_img)

# writer.close()

# normalize的使用
writer = SummaryWriter('logs_3')
img_path = 'hymenoptera_data\\train\\bees\\16838648_415acd9e3f.jpg'
img = Image.open(img_path)
trans_totensor = transforms.ToTensor()
tensor_img = trans_totensor(img)

trans_normalize = transforms.Normalize([0.5, 0.5, 0.5], [0.5,0.5,0.5])
norm_img = trans_normalize(tensor_img)
writer.add_image('normalize', norm_img)


# resize
trans_resize = transforms.Resize((512, 512))
resize_img = trans_resize(img)
tensor_img = trans_totensor(resize_img)
writer.add_image('resize', tensor_img)



# compose
trans_resize_2 = transforms.Resize(512)
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
resize_img_2 = trans_compose(img)
writer.add_image('resize', resize_img_2, 1)

writer.close()