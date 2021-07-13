import sys
import cv2 as cv
import numpy as np

def main():
    firstImage = 'C:\images\man.jpg'
    secondImage = 'C:\images\stars.jpg'

    image1 = cv.imread(cv.samples.findFile(firstImage))
    image2 = cv.imread(cv.samples.findFile(secondImage))

    image1_dim = (image1.shape[1], image1.shape[0])

    image2 = cv.resize(image2, image1_dim, interpolation = cv.INTER_AREA)

    gray_image1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
    gray_image2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)

    # git merge carl_sagan earth
    image3 = cv.subtract(gray_image1, gray_image2)

    cv.imshow('Image 1', image1)
    cv.imshow('Image 2', image2)
    cv.imshow('Image 1 Gray', gray_image1)
    cv.imshow('Image 2 Gray', gray_image2)
    cv.imshow('Result', image3)
    cv.waitKey(0)

if __name__ == "__main__":
    main()