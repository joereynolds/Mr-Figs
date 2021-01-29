class CountdownTimer:
    """
    Counts down from a number to 0 and is capable of resetting.
    This is generally used with animations. 

    i.e. After 0.125 go to the next frame and then start again.
    """

    def __init__(self, cooldown: int):
        """
        :param cooldown: The time that this countdown will countdown for (e.g. 0.250)
        """

        """
        cooldown here is unaltered.

        timer is the same but is altered per tick (or whenever else) by the program
        using it. We need cooldown to stay as it is so that we can reset our timer.


        """
        self.cooldown = cooldown
        self.timer = cooldown

    def has_ended(self) -> bool:
        return self.timer <= 0

    def decrement(self, by: int):
        """Called by other programs to decrement this timer"""
        self.timer -= by

    def reset(self):
        self.timer = self.cooldown
