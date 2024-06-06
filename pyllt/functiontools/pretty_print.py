import json
import re
import xml.dom.minidom
from xml.etree.ElementTree import SubElement, Element, tostring

import yaml


class PrettyPrinter:
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
        "underline": "\033[4m",
        "reset": "\033[0m"
    }
    dynamic_conditions = ['c', 's', 'r']

    def __init__(self, color="reset", style="normal"):
        self.color = self.COLORS.get(color, self.COLORS["reset"])
        self.style = self.STYLES.get(style, self.STYLES["normal"])
        self.is_printed = False
        self.auto_reset = False
        self.noplr = 0
        self.count_of_printed = 0

    def set_color(self, color):
        self.color = self.COLORS.get(color, self.COLORS["reset"])

    def set_auto_reset(self, number_of_printing_lines_reset: int = None):
        if number_of_printing_lines_reset is None:
            number_of_printing_lines_reset = 0

        self.noplr = number_of_printing_lines_reset
        self.auto_reset = True

    def set_style(self, style):
        self.style = self.STYLES.get(style, self.STYLES["normal"])

    def reset_style(self):
        if self.auto_reset and self.noplr == self.count_of_printed:
            self.style = self.STYLES["normal"]
            self.color = self.COLORS["reset"]
            self.count_of_printed = 0

    def print_text(self, text, modifier=None):
        if modifier == 'json':
            self.__print_json(text)
            return
        elif modifier == 'yaml':
            self.__print_yaml(text)
            return
        elif modifier == 'xml':
            self.__print_xml(text)
            return
        else:
            print(f"{self.style}{self.color}{text}{self.STYLES['normal']}{self.COLORS['reset']}")
            self.count_of_printed += 1
            self.reset_style()

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

        self.count_of_printed += 1
        self.reset_style()

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

        self.count_of_printed += 1
        self.reset_style()

    def __print_json(self, json_data):
        formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
        self.print_text(f"{self.color}{self.style}{formatted_json}{self.STYLES['reset']}{self.COLORS['reset']}")

    def __print_yaml(self, yaml_data):
        formatted_yaml = yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True)
        self.print_text(f"{self.color}{self.style}{formatted_yaml}{self.STYLES['reset']}{self.COLORS['reset']}")

    def __print_xml(self, xml_data):
        dom = xml.dom.minidom.parseString(xml_data)
        formatted_xml = dom.toprettyxml()
        self.print_text(f"{self.color}{self.style}{formatted_xml}{self.STYLES['reset']}{self.COLORS['reset']}")


if __name__ == "__main__":
    def generic_test_data():
        json_data = []
        for i in range(100):
            data = {
                f"key_{i}": {
                    f"subkey_{j}": {
                        f"subsubkey_{k}": f"value_{i}_{j}_{k}" for k in range(3)
                    } for j in range(3)
                } for i in range(3)
            }
            json_data.append(data)

        yaml_data = {}
        for i in range(200):
            nested_data = yaml_data
            for j in range(19):
                nested_data = nested_data.setdefault(f"key_{i}_{j}", {})
                nested_data[f"subkey_{j}"] = f"value_{i}_{j}"

        root = Element('data')
        for i in range(100):
            elem_i = SubElement(root, f"key_{i}")
            for j in range(3):
                elem_j = SubElement(elem_i, f"subkey_{j}")
                for k in range(3):
                    elem_k = SubElement(elem_j, f"subsubkey_{k}")
                    elem_k.text = f"value_{i}_{j}_{k}"
        xml_data = tostring(root, encoding='unicode')
        return  json_data,  yaml_data,  xml_data
    json_data,  yaml_data,  xml_data = generic_test_data()
    printer = PrettyPrinter()
    printer.set_auto_reset(999)  # Used for reset after printing the text

    printer.set_color("green")
    printer.set_style("bold")

    printer.print_text("Hello, World!")

    printer.print_text(json_data, 'json')
    printer.print_text(yaml_data, 'yaml')
    printer.print_text(xml_data, 'xml')

    data = [
        ["Alice", 30, "New York", 22],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]
    headers = ["Name", "Age", "City", "Score"]
    printer.print_table(data, headers)

    import numpy as np

    x = list(range(50))
    y = [np.sin(i/4) for i in x]
    printer.draw_plot(x, y, title="Sine Wave", xlabel="Time", ylabel="Amplitude")
