import os
import numpy as np
import torch
import torch.utils.data
from PIL import Image
import torchvision.transforms as T
import cv2


class PennFudanDataset(object):
    def __init__(self, root):
        self.root = root
        self.imgs = list(sorted(os.listdir(os.path.join(root, "PNGImages"))))
        self.masks = list(sorted(os.listdir(os.path.join(root, "PedMasks"))))
        self.transform = T.ToTensor()

    def __getitem__(self, idx):
        img_path = os.path.join(self.root, "PNGImages", self.imgs[idx])
        mask_path = os.path.join(self.root, "PedMasks", self.masks[idx])
        img = Image.open(img_path).convert("RGB")
        mask = Image.open(mask_path)
        mask = np.array(mask)
        obj_ids = np.unique(mask)
        obj_ids = obj_ids[1:]
        masks = mask == obj_ids[:, None, None]
        masks = torch.as_tensor(masks, dtype=torch.uint8)

        target = {}
        target["masks"] = masks

        img = self.transform(img)

        return img, target

    def __len__(self):
        return len(self.imgs)


def main():
    dataset = PennFudanDataset('PennFudanPed')
    # data_loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=True, num_workers=1)
    data_loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=True)

    for img_tensor, target_tensor in data_loader:
        img = img_tensor[0].permute(1, 2, 0).cpu().numpy() * 255
        img = img.astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow("img", img)

        # TODO: Change the tensor(target_tensor["masks"][0][0]) into an gray image.
        # cv2.imshow("mask", mask)

        cv2.waitKey(0)

    print("Finish")


if __name__ == "__main__":
    main()
