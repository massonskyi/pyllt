__all__ = ['Observer', 'Subject']


class Observer(object):
    """
    Observer class that will be used to update the observer object when the subject object is updated
    """

    def update(self, subject: object):
        """
        Updates the observer object when the subject object is updated
        :param subject: subject object that is updated
        :return: None
        """
        pass


class Subject(object):
    """
    Subject class that will be used to update the observer object when the subject object is updated
    """

    def __init__(self):
        """
        Initializes the subject object
        """
        self._observers = []

    def attach(self, observer: Observer):
        """
        Attaches the observer object to the subject object
        :param observer: observer object that is attached to the subject object
        :return: None
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        Detaches the observer object from the subject object
        :param observer: observer object that is detached from the subject object
        :return: None
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        """
        Notifies all the attached observer objects
        :return: None
        """
        for observer in self._observers:
            observer.update(self)


if __name__ == "__main__":
    # Пример использования
    class ConcreteObserver(Observer):
        def update(self, subject):
            print(f'Observer: Reacted to the event from {subject}.')


    class ConcreteSubject(Subject):
        def __init__(self, state):
            super().__init__()
            self._state = state

        @property
        def state(self):
            return self._state

        @state.setter
        def state(self, state):
            self._state = state
            self.notify()


    subject = ConcreteSubject(10)
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.state = 20  # Observers will be notified
