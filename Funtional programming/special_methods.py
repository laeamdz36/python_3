"""Modulo de practica de metodos especiales"""

import math


class GlobalCoordinates:

    def __init__(self, latitude, longitude):

        self._lat_deg = latitude[0]
        self._lat_min = latitude[1]
        self._lat_sec = latitude[2]
        self._lat_dir = latitude[3]

        self._long_deg = latitude[0]
        self._long_min = latitude[1]
        self._long_sec = latitude[2]
        self._long_dir = latitude[3]

    @staticmethod
    def degrees_from_decimal(dec, *, lat):

        if lat:
            direction = "S" if dec < 0 else "N"
        else:
            direction = "W" if dec < 0 else "E"
        dec = abs(dec)
        degrees = int(dec)
        dec -= degrees
        minutes = int(dec * 60)
        dec -= minutes / 60
        seconds = round(dec * 3600, 1)

        return (degrees, minutes, seconds, direction)

    @staticmethod
    def decimal_from_degrees(degrees, minutes, seconds, direction):
        dec = degrees + minutes / 60 + seconds / 3600
        if direction == "S" or direction == "W":
            dec = -dec
        return round(dec, 6)

    @property
    def latitude(self):
        return self.decimal_from_degrees(
            self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir
        )

    @property
    def longitude(self):
        return self.decimal_from_degrees(
            self._long_deg, self._long_min, self._long_sec, self._long_dir
        )

    def __repr__(self) -> str:
        return (
            f"<GlobalCoordinates "
            f"lat = {self._lat_deg}°{self._lat_min}'"
            f"{self._lat_sec}\"{self._lat_dir} "
            f"lon = {self._long_deg}°{self._long_min}'"
            f"{self._long_sec}\"{self._long_dir}>"
        )

    def __str__(self):
        return (
            f"{self._lat_deg}°{self._lat_min}'"
            f"{self._lat_sec}\"{self._lat_dir} "
            f"{self._long_deg}°{self._long_min}'"
            f"{self._long_sec}\"{self._long_dir}"
        )

    def __hash__(self):
        return hash((
            self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir,
            self._long_deg, self._long_min, self._long_sec, self._long_dir
        ))


nsp = GlobalCoordinates(latitude=(37, 46, 32.6, "N"),
                        longitude=(122, 24, 39.4, "W"))
print(repr(nsp))

print(f"Impresion del contenido de la instancia {nsp}")

print(f"Print the hash value {nsp.__hash__}")
print(f"Print the hash value {nsp.__hash__}")
print(f"Print the hash value {nsp.__hash__}")
