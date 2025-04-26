import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_on_off():
    tv = Television()
    tv.power()
    tv.volume_up()  # Volume becomes 1
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Muted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Unmuted

def test_mute_when_off():
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_wraps():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down_wraps():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_channel_up_when_off():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up_behavior():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()  # Should cap at MAX_VOLUME = 2
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down_behavior():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_down()
    tv.volume_down()  # Should cap at MIN_VOLUME = 0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up_unmutes():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()  # Should unmute and increase volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down_unmutes():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
