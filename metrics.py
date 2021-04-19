import numpy as np 
import torch
import torch.nn.functional as F
from skimage.util import img_as_float, img_as_ubyte

def avg_iou(target, prediction):
    with torch.no_grad():

        run_iou = 0.0
        batch_size = target.shape[0]
        assert batch_size == prediction.shape[0]

        target = torch.sigmoid(target)
        prediction = torch.sigmoid(prediction)

        true_mask = img_as_ubyte(target.cpu().numpy())
        convt_target = prediction.cpu().numpy()
        convt_mask = (convt_target > 0.5) * 255
        pred_mask = convt_mask.astype(np.uint8)

        for index in range(batch_size):
            truth = true_mask[index, 0]
            predicted = pred_mask[index, 0]
            run_iou += iou(truth, predicted)
            
        run_iou /= batch_size
    return run_iou  
  
def iou(im1, im2, empty_score=0.0):
    """Calculates the iou for 2 images"""

    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    im1 = im1 > 0.5
    im2 = im2 > 0.5

    intersection = np.logical_and(im1, im2)
    union = np.logical_or(im1, im2)

    union_sum = union.sum()
    if union_sum == 0:
        return empty_score

    return intersection.sum() / union_sum

def avg_dice_coeff(target, prediction):
    with torch.no_grad():
        run_dice_coeff = 0.0
        batch_size = target.shape[0]
        assert batch_size == prediction.shape[0]

        target = torch.sigmoid(target)
        prediction = torch.sigmoid(prediction)

        true_mask = img_as_ubyte(target.cpu().numpy())
        convt_target = prediction.cpu().numpy()
        convt_mask = (convt_target > 0.5) * 255
        pred_mask = convt_mask.astype(np.uint8) 

        for index in range(batch_size):
            truth = true_mask[index, 0]
            predicted = pred_mask[index, 0]
            run_dice_coeff += dice_coeff(truth, predicted)

        run_dice_coeff /= batch_size
    return run_dice_coeff

def dice_coeff(im1, im2, empty_score=1.0):
    """Calculates the dice coefficient for the images"""

    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    im1 = im1 > 0.5
    im2 = im2 > 0.5

    im_sum = im1.sum() + im2.sum()
    if im_sum == 0:
        return empty_score

    intersection = np.logical_and(im1, im2)

    return 2. * intersection.sum() / im_sum