"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
    

    def get_total(self):
        """Calculate price, including tax."""
        
        # if not xmas melon, then base price = 5
            # otherwise, 1.5 * base price

        # if int orders, if qty < 10, then +$3 fee

        base_price = 5
        fee = 0

        if self.species == 'Christmas melon':
            base_price *= 1.5

        if self.order_type == 'international' and self.qty < 10:
            fee = 3

        total = (1 + self.tax) * self.qty * base_price + fee

        return round(total, 2)


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    """Initialize melon order attributes."""

    order_type = "domestic"
    tax = 0.08


    def __init__(self, species, qty):
        super().__init__(species, qty)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    """Initialize melon order attributes."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
