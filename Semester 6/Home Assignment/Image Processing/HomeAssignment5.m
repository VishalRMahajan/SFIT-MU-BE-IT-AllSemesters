% Clear workspace and command window
clear; clc; close all;

% Read the input image
img = imread('cameraman.tif');

% Contrast adjustment
increased_contrast = imadjust(img, stretchlim(img), []);
decreased_contrast = imadjust(img, [], [0.2 0.8]);

% Brightness adjustment
increased_brightness = img + 50;
decreased_brightness = img - 50;

% Display results
figure;
subplot(2, 3, 1); imshow(img); title('Original Image');
subplot(2, 3, 2); imshow(increased_contrast); title('Increased Contrast');
subplot(2, 3, 3); imshow(decreased_contrast); title('Decreased Contrast');
subplot(2, 3, 4); imshow(increased_brightness); title('Increased Brightness');
subplot(2, 3, 5); imshow(decreased_brightness); title('Decreased Brightness');
