import numpy as np
import cv2

f = cv2.imread("inpaint_before.jpeg")
mask = np.all(f[:,:] == [0,0,0], axis=-1).astype("uint8")
mask[mask[:,:] == 1] = 255
inpainted = cv2.inpaint(f, mask, 15, cv2.INPAINT_TELEA)
cv2.imwrite("inpaint_after.jpg", inpainted)
