import tinycss2


class CSSParser:
    def __init__(self, css_file):
        with open(css_file, 'r') as file:
            self.css_rules = tinycss2.parse_stylesheet(file.read(), skip_whitespace=True)

    def get_styles(self, selector):
        styles = {}
        for rule in self.css_rules:
            if rule.type == 'qualified-rule':
                rule_selector = ''.join([token.serialize() for token in rule.prelude]).strip()
                if rule_selector == selector:
                    for decl in tinycss2.parse_declaration_list(rule.content):
                        if decl.type == 'declaration':
                            prop = decl.name.lower()
                            value = ''.join([token.serialize() for token in decl.value]).strip()
                            styles[prop] = value
        return styles


def color_to_gl(color):
    if isinstance(color, str):
        rgb = tuple(map(int, color.replace('rgb(', '').replace(')', '').split(',')))
        return tuple(c / 255.0 for c in rgb)
    if isinstance(color, tuple):
        return tuple(c / 255.0 for c in color)
    return color