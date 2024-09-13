
def drawGraph(countryNames, population):
    for i in range (len(countryNames)):
        print("%15s:" %countryNames[i], end= " ")
        for j in range(population[i]):
            print("*", end= " ")
        print()

if __name__ == "__main__":
    countryNames= []
    population = []
    for index in range(1,5):
        print("Country #" + str(index))
        country = input("Enter country name: ")
        population = input("Enter population: ")
        country.append(country)
        population.append(population)
print()
drawGraph(country, population)

