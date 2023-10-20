class Formula1:
    def __init__(self):
        self.drivers = []  # Haydovchilar ro'yhati
        self.race_results = {}  # Yarish natijalari

    def add_driver(self, name, team):
        self.drivers.append({'name': name, 'team': team})

    def add_race_result(self, race_name, results):
        self.race_results[race_name] = results

    def get_driver_results(self, driver_name):
        driver_results = {}
        for race, results in self.race_results.items():
            if driver_name in results:
                driver_results[race] = results[driver_name]
        return driver_results

    def get_team_results(self, team_name):
        team_results = {}
        for race, results in self.race_results.items():
            for driver, position in results.items():
                if self.get_driver_team(driver) == team_name:
                    if race not in team_results:
                        team_results[race] = {}
                    team_results[race][driver] = position
        return team_results

    def get_driver_team(self, driver_name):
        for driver in self.drivers:
            if driver['name'] == driver_name:
                return driver['team']

# Formula 1 obyektini yaratamiz
f1 = Formula1()

# Haydovchilarni qo'shamiz
f1.add_driver("Lewis Hamilton", "Mercedes")
f1.add_driver("Max Verstappen", "Red Bull Racing")
f1.add_driver("Charles Leclerc", "Ferrari")
f1.add_driver("Valtteri Bottas", "Mercedes")

# Yarish natijalarini qo'shamiz
f1.add_race_result("Australian GP", {
    "Lewis Hamilton": 1,
    "Max Verstappen": 2,
    "Charles Leclerc": 3
})

f1.add_race_result("Bahrain GP", {
    "Lewis Hamilton": 2,
    "Max Verstappen": 1,
    "Valtteri Bottas": 3
})

# Haydovchi natijalarini olish
hamilton_results = f1.get_driver_results("Lewis Hamilton")
print("Lewis Hamilton natijalari:", hamilton_results)

# Komanda natijalarini olish
mercedes_results = f1.get_team_results("Mercedes")
print("Mercedes komandasining natijalari:", mercedes_results)
