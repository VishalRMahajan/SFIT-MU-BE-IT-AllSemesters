% Clear workspace and command window
clear; clc; close all;

% Read a grayscale image
f = imread('rice.png');
f = im2double(f); % Convert to double for computation

% Get the size of the image
[N, ~] = size(f);

% Create g(x, y) based on the given formula
g = 2 * f; % Initialize g with 2*f(x, y)
for x = 1:N
    for y = 1:N
        if y > 1
            g(x, y) = g(x, y) + f(x, y-1); % f(x, y-1)
        end
        if y < N
            g(x, y) = g(x, y) + f(x, y+1); % f(x, y+1)
        end
    end
end

% Normalize g to keep pixel values between 0 and 1
g = mat2gray(g);

% Display original and transformed images
figure;
subplot(1,2,1); imshow(f); title('Original Image f(x, y)');
subplot(1,2,2); imshow(g); title('Transformed Image g(x, y)');

% Plot histograms
figure;
subplot(1,2,1); imhist(f); title('Histogram of f(x, y)');
subplot(1,2,2); imhist(g); title('Histogram of g(x, y)');

% Calculate contrast using standard deviation
contrast_f = std(f(:));
contrast_g = std(g(:));

% Display contrast values
disp(['Contrast of Original Image: ', num2str(contrast_f)]);
disp(['Contrast of Transformed Image: ', num2str(contrast_g)]);
