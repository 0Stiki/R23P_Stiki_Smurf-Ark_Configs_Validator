# Developed For The ARK SE Community BY: R23PSolo aka Stiki-Smurf
# Contact owner@darkskymeta.com if you would like to see this program continue into ARK 2 and Grow.
# This is a Python script to search a WINDOWS EDITION ark ini file for duplicated Lines.
# Before it will run you need to complete 4 easy steps
# 1) Create a folder named files in the same folder that this script is in
# 2) Copy and Paste your ini files into the new files-folder
# 3) Create a folder named 'output' inside the files-folder
# 4) Add the name of each file that you wish to validate(include the .ini extension)
# to the file_names list below this section
# in the same format as the two file names it already includes
# (You must remove the current filenames if they are not being checked)
file_names = ['Game.ini', 'GameUserSettings.ini']
# Now Just Run This Script And check your output folder. :)


def ark_ini_windows_dupe_checker():
    start_msg = 'Initialized -- ARK SE Windows INI Config File Duplication Destroyer \n ' \
          'Developer: R23PSolo aka Stiki-Smurf || Contact: Owner@darkskymeta.com '
    input_file_path = './files/'
    output_file_path = input_file_path + 'output/'
    file_count = 0
    master_config_names_list = []
    cf_dupe_list = []
    for name in file_names:
        msg = start_msg
        file_count += 1
        with open(input_file_path + name, 'rt') as current_file:
            line_count, temp_header = 0, None
            total_header_count, dupe_header_count, good_header_count, dupe_config_count, good_config_count = 0, 0, 0, 0, 0
            dupe_headers, good_headers, dupe_configs, good_configs_by_name, good_lines = [], [], [], [], []
            msg += ('\n' + 'Working On File' + str(file_count) + ': ' + name)
            for line in current_file:
                line_count += 1
                stripped_line = None if not line.strip() else line.strip()
                line = line if not stripped_line else stripped_line
                if line[0] == '[':
                    total_header_count += 1
                    if line not in good_headers and line != temp_header:
                        if not line == temp_header:
                            temp_header = line if line not in good_headers else temp_header
                        if line == temp_header:
                            good_headers.append(line)
                            good_lines.append("\n" + temp_header if line_count != 0 else temp_header)
                            good_header_count += 1
                    else:
                        dupe_headers.append(line)
                        dupe_header_count += 1
                if '=' in line:
                    config_name, config_value = line.split('=')[0], line.split('=')[1]
                    if config_name in master_config_names_list and config_name not in cf_dupe_list:
                        cf_dupe_list.append(config_name + " From: " + name + " Line: " + str(line_count))
                    if config_name not in master_config_names_list and config_name not in cf_dupe_list:
                        master_config_names_list.append(config_name)
                    if config_name not in good_configs_by_name:
                        good_configs_by_name.append(config_name)
                        good_lines.append(line)
                        good_config_count += 1
                    elif config_name in good_configs_by_name:
                        dupe_configs.append(config_name)
                        dupe_config_count += 1
        current_file.close()
        dupe_count = dupe_header_count + dupe_config_count
        msg += '\n Validated File: ' + name + ' - Total Lines Validated: ' + str(line_count) + '--'
        msg += '\n Found' + str(dupe_count) + 'Total Duplicated Lines' if dupe_count else msg
        msg += '\n Checking' + name + 'For duplicated Header Lines' if dupe_header_count >= 1 else msg
        msg += '\n No Duplicated headers Found For: ' + name if not dupe_header_count >= 1 else "Found Header Duplication(s)"
        if dupe_header_count >= 1:
            msg += '\n Total Duplicated Header(s) Found:' + str(dupe_header_count)
            for header in dupe_headers:
                msg += '\n' + 'File' + name + 'Line:' + header + 'Was Duplicated'
        msg += '\n' + 'No More Duplicated Headers found' if dupe_header_count >= 1 else 'Proceeding...'
        msg += '\n' + "Checking " + name + " For Duplicated Configuration Lines" \
                                           "" if dupe_config_count >= 1 else 'Proceeding...'
        msg += '\n' + 'No Duplicated Configuration Lines Found For:' \
                      '' + name if not dupe_config_count >= 1 else 'Found Duplicated Configuration Lines'
        if dupe_config_count >= 1:
            msg += '\n' + 'Total Duplicated Configuration Lines(s) Found:' + str(dupe_config_count)
            for config in dupe_configs:
                msg += '\n' + 'Configuration Line:' + config + ' Was Duplicated'
        msg += '\n' + "No more Duplicated Configuration Lines Found." if dupe_config_count >= 1 else "Proceeding..."
        msg += '\n' + "Stripping Out Duplicated Line(s) And Building Output File" \
                      "" if dupe_config_count + dupe_header_count >= 1 else "Proceeding..."
        with open(f'{output_file_path}{name}', 'at') as write_to:
            for line in good_lines:
                write_to.write(line + '\n')
            write_to.close()

        msg += '\n' + f'Output File: {name} Was Successfully Created'
        msg += '\n' + f'{name} Validation: Success Total Lines Validated:{line_count}' \
                      f'Total Duplicates Removed: {dupe_header_count + dupe_config_count}'
        msg += '\n Checking For Next File'
        start_msg = msg
        # end File loop - if not next file : Auto-Pass : ELSE : Loop again with next file
    msg = '\n No Next File Found'
    msg += '\n Building List Of CROSS FILE DUPLICATIONS'
    with open(f'{output_file_path}cross_file_duplicates_log.txt', 'at') as cfd:
        for cf in cf_dupe_list:
            cfd.write(cf + "\n")
        cfd.close()
    msg += '\n Creating CROSS-FILE LINE-DUPLICATION output file.'
    msg += '\n Finished Writing Cross File Duplication lines to /output/info_logs/cross_file_duplicates.txt'
    msg += '\n Finalizing Validator'
    msg += '\n _____Validation Complete_____'
    start_msg += msg
    with open(output_file_path + 'main_info_log.txt', 'at') as log_file:
        log_file.write(start_msg)
        log_file.close()
    print(start_msg)


if __name__ == '__main__':
    ark_ini_windows_dupe_checker()
