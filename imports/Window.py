from imports.Colors import bc


class Window:
    lines = []  # list for storing screen lines
    size = 1    # number of screen lines
    bar = '#'   # default pattern for window bar
    width = 60  # console window width
    cursor = 0  # current cursor position

    def __init__(self, user_lines, w=60):
        self.width = w
        self.bar = bc.FGYELLOW + self.bar * self.width + bc.ENDC
        self.lines.append(self.bar)
        for line in user_lines:
            self.lines.append(line)
        self.lines.append(self.bar)
        self.size = len(self.lines)
        print(bc.ESC + str(self.size) + bc.DOWNBYN)
        self.cursor = self.size

    def updateLine(self, num, text, centered=True):
        if centered is not None:
            text = '  ' + ' ' * int((self.width - len(text)) / 2 - 2) + text
        self.lines[num] = text

    def printWindow(self):
        print(bc.ESC + str(self.cursor + 1) + bc.UPBYN)
        for i in range(0, self.size):
            print(bc.CLEAR)
        print(bc.ESC + str(self.size + 1) + bc.UPBYN)
        for i in range(0, self.size):
            print(self.lines[i])
        self.cursor = self.size

    def updateAndPrint(self, num, text, centered=True):
        self.updateLine(num, text, centered)
        self.printWindow()

    def setCursor(self, line):
        if line > self.cursor:
            print(bc.ESC + str(line - self.cursor) + bc.DOWNBYN)
        elif line < self.cursor:
            print(bc.ESC + str(self.cursor - line + 1) + bc.UPBYN)
        self.cursor = line + 1

    def inputText(self, text=None, line=None, no_offset=None):
        if line is not None:
            self.setCursor(line)
        self.cursor += 1 if no_offset is None else 0
        return str(input(text if text is not None else ''))
