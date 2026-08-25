class Customer:
    VALID_STATUSES = {
        "lead",
        "prospect",
        "customer",
        "inactive"
        }
    def __init__(self, name, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        self._name = name
        self._status = status
        self._orders = []
    @property
    def name(self):
        return self._name
    @property
    def is_customer(self):
        return self._status == "customer"
    def add_order(self, order):
        return self._orders.append(order)
    @property
    def lifetime_value(self):
        return sum(order.total for order in self._orders)

class Lead:
    def __init__(self, name, budget, engagement_score, company_size, industry):
        self._name = name
        self._budget = budget
        self._engagement_score = engagement_score
        self._company_size = company_size
        self.industry = industry
        
    @property
    def name(self):
        return self._name
    @property 
    def is_qualified(self):
        return (
            (self._engagement_score >= 70 and self._budget >= 1_000_000)
            or (self._engagement_score >= 60
            and self._company_size == "enterprise"))

class SalesTeam:
    def contact(self, lead):
        print(f"Sales team is contacting {lead.name}")

class Order:
    def __init__(self, order_id, total):
        self._order_id = order_id
        self._total = total
    @property
    def order_id(self):
        return self._order_id
    @property
    def total(self):
        return self._total
    
lead = Lead(
"John Doe",
2_000_000,
85,
"large",
"Engineering"
)
sales_team = SalesTeam()
if lead.is_qualified:
    sales_team.contact(lead)

customer =  Customer("Jane Doe", "customer")
customer.add_order(Order("ORD001", 50_000))
customer.add_order(Order("ORD002", 100_000))
customer.add_order(Order("ORD003", 250_000))

print(customer.lifetime_value)
print(customer.is_customer)