import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Читаем все строки файла
    return lines


def merge_files(input_files, output_file):
    file_info = []


    for file_name in input_files:
        file_path = os.path.join(os.getcwd(), file_name)
        lines = read_file(file_path)
        file_info.append((file_name, len(lines), lines))


    file_info.sort(key=lambda x: x[1])


    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_name, line_count, lines in file_info:
            result_file.write(f"{file_name}\n")
            result_file.write(f"{line_count}\n")
            result_file.writelines(lines)
            result_file.write("\n")


input_files = ['1.txt', '2.txt', '3.txt']
output_file = 'result.txt'

merge_files(input_files, output_file)