def get_title():
    # time.sleep(2)
    # pyautogui.getWindowsWithTitle("Reminder")[0].maximize()
    print(GetWindowText(GetForegroundWindow()))


def position_cursor():
    x, y = pyautogui.position()
    print(x, y)


def hp():
    x1, y1, x2, y2 = 280, 71, 359, 114
    filename = 'hp.png'
    x = 1

    while True:
        screen = np.array(ImageGraab.grab(bbox=(x1, y1, x2, y2)))
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        print(x)
        if x == 2:
            cv2.destroyAllWindows()
            break

    img = cv2.imread(filename)
    text = pytesseract.image_to_string(img)


def locate_on_screen():
    print(pyautogui.locateOnScreen("name.jpeg", grayscale=False,
                                        confidence=.8))


def color_and_position():
    x, y = position_cursor_on_screen()
    pix = pyautogui.pixel(x, y)
    print(f"Цвет выбранного pix: {pix}, x = {x}, y = {y}")
    time.sleep(0.10)


def color_pixel():
    while True:
        pix = pyautogui.pixel(x, y)
        print(pix)


def position_cursor():
    x, y = pyautogui.position()
    print(x, y)


def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    second = sec % 60
    return "%02d:%02d:%02d" % (hour, min, second)

# 4 test task

import xlsxwriter


def make_report_about_top3(students_avg_scores):
    top_array = []
    for key, value in students_avg_scores.items():
        top_array.append(value)
    top_array.sort(reverse=True)
    top_3 = top_array[:3]

    top_3_names = []
    for key, value in students_avg_scores.items():
        for i in range(0, len(top_3)):
            if value == top_3[i]:
                top_3_names.append(key)
    return top_3_names

names = make_report_about_top3(students_avg_scores)

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

for i in range(len(names)):
    worksheet.write(f'A{i+1}]', f'{names[i]}')
workbook.close()



know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_athlets(know_english, sportsmen, more_than_20_years):
    candidate = []
    for i in range(len(know_english)):
        if know_english[i] in sportsmen and know_english[i] in more_than_20_years:
            candidate.append(know_english[i])
    print(candidate)
    return candidate

find_athlets(know_english, sportsmen, more_than_20_years)




names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark",
         "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names, birthday_years, genders):
    for i in range(len(names)):
        if genders[i] == 'Female':
            names[i] = 'nope'
            birthday_years[i] = 'nope'

    for i in range(len(names)):
        if birthday_years[i] != 'nope' and birthday_years[i] != None:
            if 2021 - int(birthday_years[i]) < 18 or 2021 - int(birthday_years[i]) > 30:
                names[i] = 'nope'

    peron_list = []
    unknown = []
    for i in range(len(names)):
        if names[i] != 'nope' and birthday_years[i] != 'nope':
            if birthday_years[i] != None and genders[i] != None:
                peron_list.append(names[i])
            elif birthday_years[i] == None or genders[i] == None:
                unknown.append(names[i])
    print(f'Подходят: {peron_list}')
    print(f'unknown: {unknown}')
    return peron_list


get_inductees(names, birthday_years, genders)




candidates = [
 {"name": "1",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "101",  "scores": {"math": 61, "russian_language": 59, "computer_science": 48}, "extra_scores":0},
 {"name": "102",  "scores": {"math": 59, "russian_language": 61, "computer_science": 49}, "extra_scores":0},
 {"name": "2",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "3",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "4",  "scores": {"math": 52, "russian_language": 90, "computer_science": 86},  "extra_scores":1},
 {"name": "5",  "scores": {"math": 85, "russian_language": 79, "computer_science": 67},  "extra_scores":1},
 {"name": "6",  "scores": {"math": 38, "russian_language": 58, "computer_science": 43},  "extra_scores":2},
 {"name": "7",  "scores": {"math": 35, "russian_language": 45, "computer_science": 35},  "extra_scores":8},
 {"name": "8",  "scores": {"math": 34, "russian_language": 86, "computer_science": 69},  "extra_scores":8}, {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "9",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "10",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1},
 {"name": "11",  "scores": {"math": 52, "russian_language": 90, "computer_science": 86},  "extra_scores":1},
 {"name": "12",  "scores": {"math": 85, "russian_language": 79, "computer_science": 67},  "extra_scores":1},
 {"name": "13",  "scores": {"math": 38, "russian_language": 58, "computer_science": 43},  "extra_scores":2},
 {"name": "14",  "scores": {"math": 35, "russian_language": 45, "computer_science": 35},  "extra_scores":8},
 {"name": "15",  "scores": {"math": 34, "russian_language": 86, "computer_science": 69},  "extra_scores":8},
]


def find_top_20(candidates):
    top_array = []

    for i in range(len(candidates)):
        top_array.append([candidates[i]['scores']['math'] +
                  candidates[i]['scores']['russian_language'] + candidates[i]['scores']['computer_science']
                  + candidates[i]['extra_scores'], candidates[i]['scores']['math'] + candidates[i]['scores']['computer_science'],
                          candidates[i]['name']])

    top_array.sort(reverse=True)
    print(top_array)

    # get 20 students
    n = 20
    if top_array[n][0] == top_array[n + 1][0]:
        # get all except one
        new_result = top_array[:n]
        print('got')
        # build new array with challenger
        x = 1
        index = [[top_array[n][1], top_array[n][2]]]
        # get index matches element
        while top_array[n][0] == top_array[n + x][0]:
            index.append([top_array[n + x][1], top_array[n + x][2]])
            x += 1
        index.sort(reverse=True)
        new_result.append(index[0])
        print('new result: ', new_result)
    else:
        print(top_array[:n + 1])


find_top_20(candidates)

# end 4 task
