import cv2

def rotate(img):
    # Reading the image
    image = img

    # dividing height and width by 2 to get the center of the image
    height, width = image.shape[:2]
    # get the center coordinates of the image to create the 2D rotation matrix
    center = (width / 2, height / 2)

    # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)

    # rotate the image using cv2.warpAffine
    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
    return rotated_image