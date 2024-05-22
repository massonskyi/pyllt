__all__ = ['Mediator']


class Mediator:
    """
    This class is the mediator between the clients and the server.
    """

    def notify(self, sender, event):
        """
        Notify the clients about the event.
        """

        pass


class BaseComponent:
    """
    This class is the base class for all components.
    """

    def __init__(self, __mediator=None):
        """
        Constructor.
        :param __mediator: The mediator. It is used to notify the clients about the event.
        """
        self._mediator = __mediator

    @property
    def mediator(self):
        """
        Get the mediator.
        """
        return self._mediator

    @mediator.setter
    def mediator(self, __mediator):
        """
        Set the mediator.
        """

        self._mediator = __mediator


if __name__ == '__main__':
    # Пример использования
    class ConcreteMediator(Mediator):
        def __init__(self, component1, component2):
            self._component1 = component1
            self._component1.mediator = self
            self._component2 = component2
            self._component2.mediator = self

        def notify(self, sender, event):
            if event == 'A':
                print('Mediator reacts on A and triggers B.')
                self._component2.do_c()
            elif event == 'D':
                print('Mediator reacts on D and triggers C.')
                self._component1.do_b()


    class Component1(BaseComponent):
        def do_a(self):
            print('Component 1 does A.')
            self.mediator.notify(self, 'A')

        def do_b(self):
            print('Component 1 does B.')


    class Component2(BaseComponent):
        def do_c(self):
            print('Component 2 does C.')

        def do_d(self):
            print('Component 2 does D.')
            self.mediator.notify(self, 'D')


    component1 = Component1()
    component2 = Component2()
    mediator = ConcreteMediator(component1, component2)

    component1.do_a()
    component2.do_d()
