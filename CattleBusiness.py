class CattleBusiness:
    def __init__(self, cows):
        self.cows = cows

    def count_affected_cows(self):
        # Calculate the number of affected cows
        affected_cows = [cow for cow in self.cows if cow["health_status"] == "Sick"]
        num_affected_cows = len(affected_cows)
        return num_affected_cows

    def profit_loss_analysis(self, revenue, expenses):
        # Calculate profit or loss
        profit_loss = revenue - expenses

        # Return the result
        if profit_loss > 0:
            return f"Profit: ${profit_loss}"
        elif profit_loss < 0:
            return f"Loss: ${-profit_loss}"
        else:
            return "Break-even: No profit, no loss."

    def average_weight(self):
        # Calculate the average weight of all cows
        total_weight = sum(cow.get("weight", 0) for cow in self.cows)
        num_cows = len(self.cows)
        if num_cows > 0:
            return total_weight / num_cows
        else:
            return 0

    def total_revenue(self, price_per_kg):
        # Calculate the total revenue based on the weight of cows and the price per kg
        total_weight = sum(cow.get("weight", 0) for cow in self.cows)
        return total_weight * price_per_kg

    def feed_cost(self, cost_per_cow_per_month):
        # Calculate the total feed cost for all cows per month
        num_cows = len(self.cows)
        return num_cows * cost_per_cow_per_month

