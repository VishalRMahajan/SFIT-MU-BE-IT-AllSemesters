% Clear workspace and command window
clear; clc; close all;

% Read two grayscale images
img1 = imread('cameraman.tif'); % Image 1
img2 = imread('rice.png');      % Image 2

% Convert images to binary (black & white)
img1 = imbinarize(img1);
img2 = imbinarize(img2);

% Logical Operations
and_img = img1 & img2;
nand_img = ~and_img;

or_img = img1 | img2;
nor_img = ~or_img;

xor_img = xor(img1, img2);
xnor_img = ~xor_img;

% Display Logical Operations
figure;
subplot(2,3,1); imshow(and_img); title('AND Operation');
subplot(2,3,2); imshow(nand_img); title('NAND Operation');
subplot(2,3,3); imshow(or_img); title('OR Operation');
subplot(2,3,4); imshow(nor_img); title('NOR Operation');
subplot(2,3,5); imshow(xor_img); title('XOR Operation');
subplot(2,3,6); imshow(xnor_img); title('XNOR Operation');
