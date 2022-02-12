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
