__all__ = ['Visitor', 'Element']


class Visitor(object):
    """
    This class is used to visit the AST elements
    """

    def visit(self, __element):
        """
        This method is used to visit the AST elements
        :param __element: element to be visited
        :return: None
        """
        method_name = 'visit_' + __element.__class__.__name__
        method = getattr(self, method_name, self.generic_visit)
        return method(__element)

    def generic_visit(self, __element):
        """
        This method is used to visit the AST elements
        :param __element:  element to be visited
        :return: None
        """
        raise NotImplementedError(f'No visit_{__element.__class__.__name__} method')


class Element(object):
    """
    This class is used to represent the elements of the AST tree and to be used by the Visitor class
    to visit the AST elements and to return the resultant AST tree after visiting the elements
    """

    def accept(self, __visitor):
        """
        This method is used to accept the visitor and to visit the AST elements
        :param __visitor: visitor to be used to visit the AST elements
        :return: None
        """
        return visitor.visit(self)


if __name__ == '__main__':
    # Пример использования
    class MyElement(Element):
        def __init__(self, value):
            self.value = value


    class MyVisitor(Visitor):
        def visit_MyElement(self, element):
            return element.value * 2


    element = MyElement(10)
    visitor = MyVisitor()

    print(visitor.visit(element))  # Output: 20
