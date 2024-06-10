# import re
#
#
# class TextProcessor:
#     COLORS = {
#         "blue": "\033[34m",
#         "green": "\033[32m",
#         "reset": "\033[0m"
#     }
#
#     STYLES = {
#         "bold": "\033[1m",
#         "normal": "\033[22m"
#     }
#
#     def pyllt(self):
#         self.color = self.COLORS["reset"]
#         self.style = self.STYLES["normal"]
#
#     def dynamic_text(self, text):
#         pattern = re.compile(r"^\{[^}]*\}\{[^}]*\}.*\{[^}]*\}.*r.*$", re.IGNORECASE)
#         parts = pattern.split(text)
#         result = []
#
#         color = self.color
#         style = self.style
#
#         for part in parts:
#             if part is None:
#                 continue
#             elif part.startswith("{c:"):
#                 color_code = part[3:-1]
#                 color = self.COLORS.get(color_code, self.COLORS["reset"])
#             elif part.startswith("{s:"):
#                 style_code = part[3:-1]
#                 style = self.STYLES.get(style_code, self.STYLES["normal"])
#             elif part == "{r}":
#                 color = self.COLORS["reset"]
#                 style = self.STYLES["normal"]
#             else:
#                 result.append(f"{style}{color}{part}{self.STYLES['normal']}{self.COLORS['reset']}")
#
#         return ''.join(result)
#
#
# # Example usage
# text_processor = TextProcessor()
# text = "{c:blue}{s:bold}Hello, {c:green}World{r}!"
# result = text_processor.dynamic_text(text)
# print(result)
import re



# Test the function
text = "{c:blue}{s:bold}Hello, {c:green}World{r}! I NEED {c:blue}{s:bold}, {c:green}{R}"
color_matches, style_matches = regex_compiler(text)
print("Color Matches:", color_matches)
print("Style Matches:", style_matches)