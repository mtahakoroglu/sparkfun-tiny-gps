% sparkfun_tiny_gps.m
% gelen koordinatları RAM'de tutmak yerine bir txt dosyasına yazdırma 
% eklendi. Ardından plot_trajectory.m koşturulacak.
clear; clc;
s = serialport('COM8', 9600);
packetNumber = single(0); % packet number
startByte = uint8('h');
packetLength = 9; % in terms of bytes w/o the startByte  
packetByteArray = uint8(zeros(1, packetLength));
coordinate = single(zeros(1,2)); % (latitude, longitude)
realTimeTrajectory = true; writeTextFile = true;
if (realTimeTrajectory)
    f = figure(1); clf; grid on; hold on;
    set(gca, 'gridlinestyle', '--');
    set(f, 'KeyPressFcn', @(src, event) set(f, 'UserData', event.Key)); % Set up key detection
    set(f, 'UserData', ''); % Initialize UserData to store pressed key
end
if (writeTextFile)
    % Create gps-data folder if it doesn't exist
    folderName = 'data';
    if ~exist(folderName, 'dir')
        mkdir(folderName);
    end
    
    dateCharFormat = datestr(now);
    for i=1:length(dateCharFormat)
        if (dateCharFormat(i) == ':')
            dateCharFormat(i) = '-';
        end
    end
    dateCharFormat(length(dateCharFormat)+1:length(dateCharFormat)+4) = '.csv';
    textFileName = fullfile(folderName, ['gps data ', dateCharFormat]);
end
while (true) % i <= n yerine sonsuz döngüye
    % Check for ESC or 'q' key press
    if realTimeTrajectory
        key = get(f, 'UserData');
        if strcmp(key, 'escape') || strcmp(key, 'q')
            fprintf('Key "%s" pressed. Stopping data collection...\n', key);
            break;
        end
    end
    if ( read(s, 1, 'uint8') == startByte )
        if (packetNumber == 0)
            flush(s);
            fprintf('The serial port buffer is flushed. Data transfer begins now.\n')
        else
            % read in the packet in terms of bytes (as Gabriel did in his PPM reader code)
            for i = 1:1:packetLength
                packetByteArray(i) = uint8(read(s,1,'uint8'));
            end
            coordinate(1) = typecast(packetByteArray(1:4), 'single');
            coordinate(2) = typecast(packetByteArray(5:8), 'single');
            % do our own checksum on the data packet
            checksum = uint8(0); % initialize to zero before we start
            for i = 1:packetLength-1
                checksum = bitxor(checksum, packetByteArray(i), 'uint8'); %this is a standard bitwise XOR checksum
            end
            checksum = bitxor(checksum, startByte);
            if (checksum == packetByteArray(9))
                % coordinate(1) = read(s, 1, 'single');
                % coordinate(2) = read(s, 1, 'single');
                fprintf('NumOfBytesAvailable = %i    Packet = %i    Latitude = %.7f    Longitude = %.7f\n', ...
                    s.NumBytesAvailable, packetNumber, coordinate(1), coordinate(2));
                if (realTimeTrajectory)
                    plot(coordinate(2), coordinate(1), 'k.');
                end
                if (writeTextFile)
                    packetAndCoordinate = [packetNumber coordinate];
                    if (packetNumber == 1)
                        % Add header for CSV file
                        fid = fopen(textFileName, 'w');
                        fprintf(fid, 'Packet,Latitude,Longitude\n');
                        fclose(fid);
                        % Write data with comma delimiter
                        dlmwrite(textFileName, packetAndCoordinate, 'delimiter', ',', 'precision', '%.7f', '-append');
                    else
                        dlmwrite(textFileName, packetAndCoordinate, '-append', 'delimiter', ',', 'precision', '%.7f');
                    end
                end
            end
        end
        if f.CurrentCharacter > 0
            break;
        end
        packetNumber = packetNumber+1; % next packet
    end
end
delete(s);
fprintf('Serial port is terminated.\n')
%% plot captured data
% clearvars -except textFileName; clc;
data = readmatrix(textFileName); % Use readmatrix instead of load for CSV files
figure(2); clf;
plot(data(:,3), data(:,2), 'k.');
grid on; set(gca, 'gridlinestyle', '--');
xlabel('Boylam'); ylabel('Enlem');
