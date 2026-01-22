# Device simulation logic
# This file mocks device detection and compatibility checks

import random

class Device:
    def __init__(self):
        self.model = None
        self.ios_version = None
        self.signal_active = False

    def connect(self):
        # Simulate device connection
        self.model = random.choice([
            "iPhone X",
            "iPhone 11",
            "iPhone 13 Pro",
            "iPhone 15 Pro Max",
        ])
        self.ios_version = random.choice([
            "16.7.2",
            "17.4",
            "18.0",
        ])
        return True

    def info(self):
        return {
            "model": self.model,
            "ios": self.ios_version,
            "status": "Connected"
        }

    def activate_signal(self):
        # Mock GSM/LTE/5G activation
        self.signal_active = True
