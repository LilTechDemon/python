class Television:
    """
    A class to simulate a basic television with power, channel, volume, and mute functionality.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default power off, muted off,
        volume at MIN_VOLUME, and channel at MIN_CHANNEL.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the TV.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status if the TV is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the TV channel by 1, wrap to MIN_CHANNEL if at MAX_CHANNEL.
        Only works if TV is on.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the TV channel by 1, wrap to MAX_CHANNEL if at MIN_CHANNEL.
        Only works if TV is on.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume by 1 unless at MAX_VOLUME. 
        If muted, unmute first. Only works if TV is on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1 unless at MIN_VOLUME.
        If muted, unmute first. Only works if TV is on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representing the power, channel, and volume.
        Volume is shown as 0 if muted.
        """
        volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"
