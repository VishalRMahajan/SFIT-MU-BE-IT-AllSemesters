% Clear workspace and command window
clear; clc; close all;

% Read the input image
img = imread('moon.tif');

% Define rotation angles
angles = [90, 180, 270];

% Perform rotations using matrix transformation
for i = 1:length(angles)
    theta = deg2rad(angles(i)); % Convert angle to radians
    
    % Define rotation matrix for positive angle
    R_pos = [cos(theta) -sin(theta); sin(theta) cos(theta)];
    
    % Rotate image using built-in function
    rotated_pos = imrotate(img, angles(i), 'bilinear', 'crop');
    
    % Define rotation matrix for negative angle
    R_neg = [cos(-theta) -sin(-theta); sin(-theta) cos(-theta)];
    
    % Rotate image for negative angle
    rotated_neg = imrotate(img, -angles(i), 'bilinear', 'crop');
    
    % Display results
    figure;
    subplot(1, 3, 1); imshow(img); title('Original Image');
    subplot(1, 3, 2); imshow(rotated_pos); title(['Rotation by +', num2str(angles(i)), '°']);
    subplot(1, 3, 3); imshow(rotated_neg); title(['Rotation by -', num2str(angles(i)), '°']);
end
