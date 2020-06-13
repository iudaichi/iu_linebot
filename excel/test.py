import xlrd
import datetime
import pprint
import json


def excel_date(num):
    return(datetime.datetime(1899, 12, 30) + datetime.timedelta(days=num))


values_list = []
values_dict = {}
book_sheet = xlrd.open_workbook("0612.xlsx").sheets()[0]
for i in range(book_sheet.nrows):
    values_list.append(book_sheet.row_values(i))
for i, x in enumerate(values_list[2:]):
    values_dict[i] = {
        "day_of_week": x[0],
        "time_table": int(x[1]) if type(x[1]) == float else str(x[1]),
        "class_time": x[2],
        "class_name": x[3],
        "teacher_name": x[4],
        "day": excel_date(int(x[5])).strftime("%Y/%m/%d"),
        "class_room_number": str(x[6]).replace(" ", ""),
        "class_room_password": x[7]
    }
# pprint.pprint(values_dict)
with open("schedule.json") as f:
    schedule_json = json.load(f)
for schedule_value in schedule_json.values():
    print(schedule_value)
# with open("schedule.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(values_dict, indent=4))
# now = datetime.datetime.now().strftime("%Y/%m/%d")
# text = "時間割"
# for x in values_dict:
#     values_text = f"\n\n{x['day']}({x['day_of_week']})\n{x['time_table']}時間目\n{x['class_name']}\n{x['class_room_number']}\n{x['class_room_password']}\nhttps://zoom.us/j/{x['class_room_number']}?"
#     if x['day'] == now:
#         print(values_text)
#     text += values_text
# with open("schedule.txt", "w") as f:
#     f.write(text)
