####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Meringue"
signature_flavors = ["custard", "salt", "onion"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu:")
    for flavors1 in menu: 
      print('- "%s %s"' % (flavors1, menu[flavors1]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for flavors2 in original_flavors:
      print('- "%s"' %(flavors2))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for flavors3 in signature_flavors:
      print('- "%s"' %(flavors3))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    for flavors1 in menu: 
      if order == flavors1:
        return True
    for flavors2 in original_flavors: 
      if order == flavors2: 
        return True
    for flavors3 in signature_flavors:
      if order == flavors3: 
        return True
    print("Order does not exist")
    return False
    

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    Total = 0
    order_list = []
    order = ""
    print("Whats your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.")
    while True:
      order = input("")
      order=order.lower()
      if order != "exit":
        if is_valid_order(order)==True:
          order_list.append(order)
        
      else:
        break
      



    return order_list


def accept_credit_card(total):
    """
    Return whether an or-der is eligible for credit card payment.
    """
    if total >= 5: 
      print("This order is eligible for credit card payment")
    else:
      print("This order is not eligible for credit card payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0.0
 
    # your code goes here!
    for item in order_list:
      for flavor1 in menu:
        if flavor1==item:
          total+=menu[item]
      for flavor2 in original_flavors:
        if flavor2==item:
          total+=menu["original cupcake"]
      for flavor3 in menu:
        if flavor3==item:
          total+=menu["signature cupcake"]
      

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for item in order_list:
      print (item)
    total=get_total_price(order_list)
    print("That'll be KD %s" %(str(total)))
    accept_credit_card(total)
    print("Thank you for shopping at %s" %(cupcake_shop_name))