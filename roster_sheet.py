import xlsxwriter
from datetime import datetime


def create_roster(employee, hotel, time_data, entries, date_data):
    workbook = xlsxwriter.Workbook('specsheet.xlsx')
    current_datetime = datetime.today().date().timetuple()
    str_current_datetime = str(current_datetime)
    a__ = datetime.now()
    a_ = a__.strftime("%a, %d %b %Y %H-%M-%S")

    worksheet = workbook.add_worksheet()

    header = workbook.add_format(
        {'align': 'center', 'font_size': 13, 'font': 'Arial', 'bold': True, 'bottom': 1, 'top': 1, 'right': 1,
         'left': 1, 'border_color': '#2C3333',
         'bg_color': '#16FF00'})

    subH = workbook.add_format(
        {'align': 'center', 'font_size': 9, 'font': 'Arial', 'bold': True, 'bottom': 1, 'top': 1, 'right': 1, 'left': 1,
         'border_color': '#2C3333',
         'bg_color': '#FDFF00'})

    subH_blank = workbook.add_format(
        {'align': 'center', 'font_size': 9, 'font': 'Arial', 'bold': True, 'bottom': 1, 'top': 1, 'right': 1, 'left': 1,
         'border_color': '#2C3333',
         'bg_color': '#E3F4F4'})

    column_width = [{'name': 'A:A', 'size': 5}, {'name': 'B:B', 'size': 9}, {'name': 'C:C', 'size': 20},
                    {'name': 'D:D', 'size': 22},
                    {'name': 'E:E', 'size': 25}, {'name': 'F:F', 'size': 12}, {'name': 'G:G', 'size': 10},
                    ]

    for i in column_width:
        worksheet.set_column(i['name'], i['size'])

    # worksheet.write('A1', 'Flow Control Commune Pvt Ltd', )
    worksheet.merge_range('A1:G1', "DUTY ROSTER", header)
    worksheet.merge_range('A2:C2', f"DATE: {date_data[0]}", header)
    worksheet.merge_range('D2:G2', f"{date_data[2]}, {date_data[1]}", header)
    worksheet.write('A3', 'S.NO', subH)
    worksheet.write('B3', 'No of Staff', subH)
    worksheet.write('C3', 'STAFF', subH)
    worksheet.write('D3', 'HOTEL', subH)
    worksheet.write('E3', 'DUTY TIME', subH)
    worksheet.write('F3', 'PICK UP TIME', subH)
    worksheet.write('G3', 'REMARK', subH)

    for i in range(len(employee)):
        if entries[i].absent == 'none':
            worksheet.write(f'A{4 + i}', i + 1, subH_blank)
            worksheet.write(f'B{4 + i}', i + 1, subH_blank)
            worksheet.write(f'C{4 + i}', employee[i], subH)
            worksheet.write(f'D{4 + i}', hotel[i], subH)
            if time_data[i]['timeIn2'] == '00:00':
                worksheet.write(f'E{4 + i}', f"{time_data[i]['timeIn1']} - {time_data[i]['timeOut1']}", subH)
            else:
                worksheet.write(f'E{4 + i}',
                                f"{time_data[i]['timeIn1']} - {time_data[i]['timeOut1']}/{time_data[i]['timeIn2']} - {time_data[i]['timeOut2']}",
                                subH)
            worksheet.write(f'F{4 + i}', f"{time_data[i]['pickUp']}/{time_data[i]['pickUp2']}", subH)
            worksheet.write(f'G{4 + i}', entries[i].remark, subH)
        else:
            worksheet.write(f'A{4 + i}', i + 1, subH_blank)
            worksheet.write(f'B{4 + i}', i + 1, subH_blank)
            worksheet.write(f'C{4 + i}', employee[i], subH)
            worksheet.merge_range(f'D{4 + i}:G{4 + i}', entries[i].absent, header)

    workbook.close()
