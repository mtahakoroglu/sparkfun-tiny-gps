clear; close; clc;
%% load data from file
txtFile = true;
matFile = ~txtFile;
n = 2; % number of variables in file
if (txtFile)
    coordinates = single(load('gps data 05-May-2025 22-47-37.txt'));
    n = 3;
else
    load koordinatlar2.mat;
end
latitude = coordinates(:,n-1);
longitude = coordinates(:,n);
% dlmwrite('gap data.txt', coordinates, 'delimiter', '\t', 'precision', '%.7f')
%% plot trajectory
figure(2); clf; set(gcf, 'position', [200 100 980 420]);
subplot(1,2,1); % plot coordinates on x-y cartesian axes
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
plot_google_map('MapType','satellite');
plot(longitude, latitude, 'Marker','x', 'Color', 'Yellow');
xlabel('Longitude'); ylabel('Latitude');
axis([xmin, xmax, ymin, ymax]);
% print('-f1','gokhan-hoca-car','-dpng','-r300')
