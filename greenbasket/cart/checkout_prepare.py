from .models import CartItem


class CartCheckout:

    def __init__(self, user):
        self.user = user
        self.cart_items = []
        self.total_amount = 0
        self.checkout_details = {'products': [], 'total': []}


    def prepare_cart_for_checkout(self):
        self.cart_items = CartItem.objects.filter(user=self.user) ##need to add a valid user code.

        if not self.cart_items:
            return False

        self.calculate_total_amount()
        self.checkout_details()
        return self.checkout_details



    def calculate_total_amount(self):
        for cart_item in self.cart_items:
            self.total_amount += cart_item.product_price * cart_item.product_quantity


    def checkout_details(self):
        for cart_item in self.cart_items:
            self.checkout_details['products'].append({'product_id': cart_item.id,
                                                      'product_name': cart_item.product_title,
                                                      'unit_price': cart_item.product_price,
                                                      'quantity': cart_item.product_quantity
                                                      })

        self.checkout_details['total'].append({'total_price': self.total_amount}) ##add if any discounds exists.. to this dictionary as key:value pair.