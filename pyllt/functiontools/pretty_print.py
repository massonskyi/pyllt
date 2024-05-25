class PrettyPrinter:
    # ANSI escape codes for colors and styles
    COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[39m"
    }

    STYLES = {
        "normal": "\033[0m",
        "bold": "\033[1m",
        "underline": "\033[4m"
    }

    def __init__(self, color="reset", style="normal"):
        self.color = self.COLORS.get(color, self.COLORS["reset"])
        self.style = self.STYLES.get(style, self.STYLES["normal"])

    def set_color(self, color):
        self.color = self.COLORS.get(color, self.COLORS["reset"])

    def set_style(self, style):
        self.style = self.STYLES.get(style, self.STYLES["normal"])

    def print_text(self, text):
        print(f"{self.style}{self.color}{text}{self.STYLES['normal']}{self.COLORS['reset']}")

    def print_table(self, data, headers):
        # Normalize the length of each row
        max_len = max(len(headers), max(len(row) for row in data))
        normalized_data = [row + [""] * (max_len - len(row)) for row in data]
        normalized_headers = headers + [""] * (max_len - len(headers))

        table = [normalized_headers] + normalized_data
        col_widths = [max(len(str(item)) for item in col) for col in zip(*table)]
        row_separator = '+' + '+'.join('-' * (width + 2) for width in col_widths) + '+'

        def format_row(row):
            return '|' + '|'.join(f' {str(item).ljust(width)} ' for item, width in zip(row, col_widths)) + '|'

        print(self.color + self.style + row_separator)
        print(format_row(normalized_headers))
        print(row_separator)
        for row in normalized_data:
            print(format_row(row))
        print(row_separator + self.STYLES['normal'] + self.COLORS['reset'])

    def draw_plot(self, x, y, title="Plot", xlabel="X-axis", ylabel="Y-axis"):
        # Normalize y values to fit in console rows (20 rows for example)
        min_y, max_y = min(y), max(y)
        norm_y = [int((val - min_y) / (max_y - min_y) * 19) for val in y]
        max_x = max(x)
        plot_width = 50

        plot = [[' ' for _ in range(plot_width)] for _ in range(20)]

        for i, val in enumerate(norm_y):
            if i < plot_width:
                plot[19 - val][i] = '*'

        print(f"{self.color}{self.style}{title}")
        for row in plot:
            print(''.join(row))
        print(ylabel.rjust(10))
        print(xlabel.center(plot_width))
        print(self.STYLES['normal'] + self.COLORS['reset'])


# Пример использования
printer = PrettyPrinter()

# Настройка шрифта и цвета
printer.set_color("green")
printer.set_style("bold")

# Печать текста
printer.print_text("Hello, World!")

# Печать таблицы
data = [
    ["Alice", 30, "New York", 22],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
headers = ["Name", "Age", "City", "Score"]
printer.print_table(data, headers)

# Рисование графика
import numpy as np

x = list(range(50))
y = [np.sin(i / 5.0) for i in x]
printer.draw_plot(x, y, title="Sine Wave", xlabel="Time", ylabel="Amplitude")
