
class NotInRange(Exception):
    def __init__(self,message="The Value is not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    b=6
    assert a == b