from scipy import special, optimize
import model.map


objective_fun = lambda x: \
        sum (
            i#x[i] - map['connections'][0]
            for i in range(len(x))
        )

x0 = [2, 3]

print (objective_fun (x0))

print(model.map.roads_list)