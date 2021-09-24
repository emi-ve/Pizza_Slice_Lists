# Your code below:

toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]

prices = [2,6,1,3,2,7,2]

# count $2 slices
num_two_dollar_slices = prices.count(2)

#count length of toppings list
num_pizzas = len(toppings)
print(num_pizzas)

#change int to string, and print result in a sentence
new_string = str(num_pizzas)
print("We sell " + new_string + " different kinds of pizza!")

#create manual 2D list from previous data
pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)

#sort list
pizza_and_prices.sort(reverse=False)

#select cheapest pizza, store in variable
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#remove the most expensive slice
pizza_and_prices.pop()
print(pizza_and_prices)

#insert new pizza to list
pizza_and_prices.insert(3,[2.5,"peppers"])
print(pizza_and_prices)

#slice 3 cheapest pizzas, store in variable
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
