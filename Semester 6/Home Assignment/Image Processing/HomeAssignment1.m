% Clear workspace and command window
clear; clc; close all;

% Read two uncorrelated grayscale images
img1 = imread('cameraman.tif'); % Image 1
img2 = imread('rice.png');      % Image 2

% Convert images to double for mathematical operations
img1 = im2double(img1);
img2 = im2double(img2);

% Resize second image to match the size of the first
img2 = imresize(img2, size(img1));

% Sum the two images
sum_img = img1 + img2;
sum_img = mat2gray(sum_img); % Normalize between 0 and 1

% Calculate contrast using standard deviation
contrast_img1 = std(img1(:));
contrast_img2 = std(img2(:));
contrast_sum = std(sum_img(:));

% Display images with contrast values
figure;
subplot(1,3,1); imshow(img1); title(['Image 1 (Contrast: ', num2str(contrast_img1, 3), ')']);
subplot(1,3,2); imshow(img2); title(['Image 2 (Contrast: ', num2str(contrast_img2, 3), ')']);
subplot(1,3,3); imshow(sum_img); title(['Sum Image (Contrast: ', num2str(contrast_sum, 3), ')']);

% Plot histograms of all images
figure;
subplot(1,3,1); imhist(img1); title('Histogram of Image 1');
subplot(1,3,2); imhist(img2); title('Histogram of Image 2');
subplot(1,3,3); imhist(sum_img); title('Histogram of Sum Image');

% Display contrast values in the command window
disp(['Contrast of Image 1: ', num2str(contrast_img1)]);
disp(['Contrast of Image 2: ', num2str(contrast_img2)]);
disp(['Contrast of Summed Image: ', num2str(contrast_sum)]);
