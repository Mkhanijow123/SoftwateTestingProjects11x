# def print_multi_agrs(*args):
#     for i in args:
#         print(i)
#
#
# print_multi_agrs("monika")
# print_multi_agrs("seema", "amit", "Hema")
# print_multi_agrs("Malti",10,"Shubbham",True)


def make_pizza(*toppings):
    for i in toppings:
        print(i)

shilpa=make_pizza("tomatoes","hallopino")
shweta = make_pizza("pepper", "mushrooms","pineapple")

