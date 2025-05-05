clear; close all; clc;

%% List available GPS data files
folderName = 'data';
if ~exist(folderName, 'dir')
    error('Error: Directory "%s" not found.', folderName);
end

% Get all CSV files in the data directory
fileList = dir(fullfile(folderName, 'gps*.csv'));
if isempty(fileList)
    error('No GPS data files found in the "%s" directory.', folderName);
end

% Sort by date modified (newest first)
[~, sortIdx] = sort([fileList.datenum], 'descend');
fileList = fileList(sortIdx);

% Display available files
fprintf('Available GPS data files:\n');
for i = 1:length(fileList)
    fprintf('%d. %s\n', i, fileList(i).name);
end

% Add option for latest file
fprintf('\n%d. Latest file (%s)\n', length(fileList)+1, fileList(1).name);

%% Let user select a file
choice = input(sprintf('\nSelect file to plot (1-%d), or press Enter for latest: ', length(fileList)+1));
if isempty(choice)
    choice = length(fileList)+1;  % Default to latest file
end

if choice == length(fileList)+1
    selectedFile = fileList(1);  % Latest file
elseif choice >= 1 && choice <= length(fileList)
    selectedFile = fileList(choice);
else
    error('Invalid selection.');
end

fprintf('\nPlotting trajectory from: %s\n', selectedFile.name);

%% Load and plot the selected file
filePath = fullfile(folderName, selectedFile.name);
coordinates = readmatrix(filePath);

%% plot trajectory
figure(2); clf; set(gcf, 'position', [200 100 980 420]);
subplot(1,2,1); % plot coordinates on x-y cartesian axes
latitude = coordinates(:,2);
longitude = coordinates(:,3);

plot(longitude, latitude, 'k.');
grid on; set(gca, 'gridlinestyle', '--');
xlabel('Boylam'); ylabel('Enlem');
s = 0.0001;
xmax = (1+s)*max(longitude);
xmin = (1-s)*min(longitude);
ymax = (1+s)*max(latitude);
ymin = (1-s)*min(latitude);
axis([xmin, xmax, ymin, ymax]);

subplot(1,2,2); % plot coordinates on satellite image
xlim([xmin xmax]);
ylim([ymin ymax]);

% Check if plot_google_map is available
try
    plot_google_map('MapType','satellite');
    plot(longitude, latitude, 'Marker','x', 'Color', 'Yellow');
catch
    % If plot_google_map fails, just plot normal map
    plot(longitude, latitude, 'r.');
    grid on;
    warning('Could not load satellite map. Using standard plot instead.');
end

xlabel('Longitude'); ylabel('Latitude');
axis([xmin, xmax, ymin, ymax]);

fprintf('Plotted %d GPS points from %s\n', length(latitude), selectedFile.name);