class City:
    def __init__(self, location_cnt, road_cnt):
        self.location_cnt = location_cnt
        self.road_cnt = road_cnt
        self.matrix = [[0 for j in range(location_cnt)] for i in range(location_cnt)]

    def add_relation(self, location1, location2, road_type):
        self.matrix[location1-1][location2-1] = 1
        if road_type == 2:
            self.matrix[location2-1][location1-1] = 1

    def __str__(self) -> str:
        s = f"locations: {self.location_cnt}\nroads : {self.road_cnt}\n"
        for row in self.matrix:
            s += str(row) + "\n"
        return s

def readInput(filePath:str) -> list[list[int]]:
    testCases = []
    with open(filePath, "r") as file:
        city = None
        for line in file:
            inputs = list(map(int, line.strip().split()))
            if len(inputs) == 2:
                # save city
                if city != None:
                    testCases.append(city)
                # stop
                if inputs[0] == 0 and inputs[1] == 0:
                    break
                # new city
                city = City(inputs[0], inputs[1])
            else:
                city.add_relation(inputs[0], inputs[1], inputs[2])
    return testCases

def solve(city_list:list[City]) -> list[int]:
    pass

testcases = readInput("Algo/lab6/example.txt")
