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
    @property
    def is_active(self):
        return self._status == "customer"

class Lead:
    def __init__(self, name, budget, engagement_score, company_size, industry):
        self._name = name
        self._budget = budget
        self._engagement_score = engagement_score
        self.company_size = company_size
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
    
c = Customer("Nkiru", "lead")
print(c.is_active)
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