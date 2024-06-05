from abc import ABC, abstractmethod

from model.strategy import CowardlyStrategy, PassiveStrategy


class State(ABC):
    @abstractmethod
    def enter_state(self, mob):
        pass

    @abstractmethod
    def execute(self, mob):
        pass


class NormalState(State):
    def enter_state(self, mob):
        passive_strategy = PassiveStrategy()
        mob.strategy = passive_strategy

    def execute(self, mob):
        mob.strategy.execute()


class PanicState(State):
    def enter_state(self, mob):
        print("here")
        coward_strategy = CowardlyStrategy()
        mob.strategy = coward_strategy

    def execute(self, mob):
        mob.strategy.execute()
