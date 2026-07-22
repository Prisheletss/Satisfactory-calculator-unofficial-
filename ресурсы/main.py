import pandas
import sys
import pwinput
from colorama import Fore, Style, init

init()





def _1_in_1_out(filename):
    file = pandas.read_excel(filename)
    file = file.to_dict(orient='records')

    keys = {
        "outputs names": "output name",
        "outputs counts": "output count",
        "inputs names": "input name",
        "inputs counts": "input count",
        "types": "тип"
    }

    ans = {}
    for i in keys:
        ans[i] = []
    ans["power"] = []

    e = int(list(file[0].keys())[-1])


    for i in file:
        for j in keys:
            ans[j].append(i[keys[j]])
        ans["power"].append(e)

    
    return ans





def _2_in_1_out(filename):
    file = pandas.read_excel(filename)
    file = file.to_dict(orient='records')

    keys_1 = {
        "outputs names": "output name",
        "outputs counts": "output count"
    }

    keys_2 = {
        "inputs names": "input name",
        "inputs counts": "input count"
    }

    ans = {}
    for i in keys_1:
        ans[i] = []
    for i in keys_2:
        ans[i] = []
    ans["types"] = []
    ans["power"] = []

    e = int(list(file[0].keys())[-1])


    for i in file:
        for j in keys_1:
            ans[j].append(i[keys_1[j]])
        for j in keys_2:
            ans[j].append([i[f"{keys_2[j]} 1"], i[f"{keys_2[j]} 2"]])
        ans["types"].append(i["тип"])
        ans["power"].append(e)

    
    return ans





def power_calc(W0, N, N0):
    k = N/N0
    if (k % 1) > 0:
        k = int(k) + 1
    x = (N/k)/N0
    #print(W0, N, N0, k, x)
    return k*W0*(x**1.32)





def calculate(target_name, target_count):
    for crafter in crafters:
        for k in range(len(crafter["outputs names"])):
            if target_name != crafter["outputs names"][k]: continue
            """
            print("base: ")
            for i in crafter.keys():
                print(f"{i}: {crafter[i][k]}")

            print('')
            print("calculated: ")
            """
            
            N0 = crafter["outputs counts"][k]
            x = target_count / N0
            for i in crafter.keys():
                if i != "power":
                    try:
                        test = int(crafter[i][k])
                        print(f"{i}:")
                        print('\t', f"{printed}: {int(crafter[i][k])*x}")
                    except ValueError:
                        printed = crafter[i][k]
                        
                    except TypeError:
                        try:
                            test = int(crafter[i][k][0])
                            print(f"{i}:")
                            for j in range(len(crafter[i][k])):
                                print('\t', f"{printed[j]}: {int(crafter[i][k][j])*x}")
                        except:
                            printed = crafter[i][k]
                
                else:
                    print("power:", power_calc(crafter["power"][k], target_count, N0))


            print('\n\n\n')






melter = _1_in_1_out("рецепты/печь.xlsx")
constructor = _1_in_1_out("рецепты/конструктор.xlsx")
assembler = _2_in_1_out("рецепты/ассемблер.xlsx")

crafters = [melter, constructor, assembler]

base = open("рецепты/база.txt", 'r', -1, "utf-8").readlines()



target_name = input(
    Style.BRIGHT + Fore.GREEN +
    "target resource name: " + Fore.MAGENTA
)

target_count = int(input(
    Style.BRIGHT + Fore.GREEN +
    "target resource count: " + Fore.MAGENTA
))

print(Style.RESET_ALL + '\n')

calculate(target_name, target_count)






                    




    




























