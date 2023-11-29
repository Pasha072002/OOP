class Meter:
    
    def meter_a(self):
        count = 1
        while count <= 100:
            print(count, end=' ')
            count += 1

cab = Meter()

cab.meter_a()