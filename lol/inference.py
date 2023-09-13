import os
import numpy as np
import cv2

#ML
import tensorflow as tf
import keras.backend as K

# neural imaging
import nibabel as nib
import datetime as dt
date_time_format = '%Y_%m_%d__%H_%M_%S'


# dice loss as defined above for 4 classes
def dice_coef(y_true, y_pred, smooth=1.0):
    class_num = 4
    for i in range(class_num):
        y_true_f = K.flatten(y_true[:,:,:,i])
        y_pred_f = K.flatten(y_pred[:,:,:,i])
        intersection = K.sum(y_true_f * y_pred_f)
        loss = ((2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth))
   #     K.print_tensor(loss, message='loss value for class {} : '.format(SEGMENT_CLASSES[i]))
        if i == 0:
            total_loss = loss
        else:
            total_loss = total_loss + loss
    total_loss = total_loss / class_num
#    K.print_tensor(total_loss, message=' total dice coef: ')
    return total_loss

# define per class evaluation of dice coef
def dice_coef_necrotic(y_true, y_pred, epsilon=1e-6):
    intersection = K.sum(K.abs(y_true[:,:,:,1] * y_pred[:,:,:,1]))
    return (2. * intersection) / (K.sum(K.square(y_true[:,:,:,1])) + K.sum(K.square(y_pred[:,:,:,1])) + epsilon)

def dice_coef_edema(y_true, y_pred, epsilon=1e-6):
    intersection = K.sum(K.abs(y_true[:,:,:,2] * y_pred[:,:,:,2]))
    return (2. * intersection) / (K.sum(K.square(y_true[:,:,:,2])) + K.sum(K.square(y_pred[:,:,:,2])) + epsilon)

def dice_coef_enhancing(y_true, y_pred, epsilon=1e-6):
    intersection = K.sum(K.abs(y_true[:,:,:,3] * y_pred[:,:,:,3]))
    return (2. * intersection) / (K.sum(K.square(y_true[:,:,:,3])) + K.sum(K.square(y_pred[:,:,:,3])) + epsilon)

# Computing Precision 
def precision(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

# Computing Sensitivity      
def sensitivity(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    return true_positives / (possible_positives + K.epsilon())


# Computing Specificity
def specificity(y_true, y_pred):
    true_negatives = K.sum(K.round(K.clip((1-y_true) * (1-y_pred), 0, 1)))
    possible_negatives = K.sum(K.round(K.clip(1-y_true, 0, 1)))
    return true_negatives / (possible_negatives + K.epsilon())


custom_objects = {'accuracy' : tf.keras.metrics.MeanIoU(num_classes=4),
                                                   "dice_coef": dice_coef,
                                                   "precision": precision,
                                                   "sensitivity":sensitivity,
                                                   "specificity":specificity,
                                                   "dice_coef_necrotic": dice_coef_necrotic,
                                                   "dice_coef_edema": dice_coef_edema,
                                                   "dice_coef_enhancing": dice_coef_enhancing
}


VOLUME_SLICES = 100
IMG_SIZE = 128
VOLUME_START_AT = 22

def predict_vol(x_flair, x_ce, model, volume_start_at=VOLUME_START_AT, volume_slices=VOLUME_SLICES, img_size=IMG_SIZE):
    X = np.empty((volume_slices, img_size, img_size, 2))
    flair = x_flair
    ce = x_ce

    for j in range(volume_slices):
        X[j,:,:,0] = cv2.resize(flair[:,:,j+volume_start_at], (img_size,img_size))
        X[j,:,:,1] = cv2.resize(ce[:,:,j+volume_start_at], (img_size,img_size))

    y = model.predict(X/np.max(X), verbose=1)
    y = np.argmax(y, axis=-1).astype(np.uint16)
    y = np.concatenate((np.zeros((22,y.shape[1],y.shape[2]), dtype=np.uint16), y), axis=0)
    y = np.concatenate((y, np.zeros((flair.shape[-1]-y.shape[0],y.shape[1],y.shape[2]), dtype=np.uint16)), axis=0)
    y = np.swapaxes(y, 0, 2)
    y = cv2.resize(y, (240,240), interpolation=cv2.INTER_NEAREST)    
    y = np.swapaxes(y, 0, 1)
    print(y.shape)
    return y

def save_pred(y):
    y = nib.Nifti1Image(y, np.eye(4))
    y.header.get_xyzt_units()
    current_date_time_dt = dt.datetime.now()
    current_date_time_string = dt.datetime.strftime(current_date_time_dt, date_time_format)
    y.to_filename(f'pred_seg_mask_{current_date_time_string}.nii.gz')


model = tf.keras.models.load_model('final_model.h5', custom_objects=custom_objects)