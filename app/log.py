class Logger:
    def __init__(self,**kwargs) -> None:
        self.saveaddr = kwargs["save"] or "test.log"
        