# Advanced AI Trust Score Simulation with Risk Signals and Fallback Logic

class AddressProfile:
    def __init__(self, address):
        self.address = address
        self.tx_volume = 0
        self.tx_count = 0
        self.reputation = 100
        self.flags = []
        self.cooldown = False

    def add_transaction(self, volume, gas_used, timestamp):
        self.tx_volume += volume
        self.tx_count += 1

        # Signal: whale detection
        if volume > 10000:
            self.flags.append("whale_activity")
            self.reputation -= 15

        # Signal: high gas usage
        if gas_used > 8000000:
            self.flags.append("gas_spike")
            self.reputation -= 5

        # Signal: TX frequency (if too fast in a short time frame)
        if self.tx_count > 5 and timestamp < 60:
            self.flags.append("tx_burst")
            self.reputation -= 10

        # Fallback: trigger cooldown for risky profiles
        if self.reputation < 50:
            self.cooldown = True

    def analyze_trust(self):
        score = max(self.reputation, 0)
        if self.cooldown:
            return "Cooldown - Manual Review", score
        elif score < 50:
            return "Low Trust", score
        elif score < 80:
            return "Medium Trust", score
        else:
            return "High Trust", score

# Example Simulation
user = AddressProfile("0xDEF456")
user.add_transaction(volume=12000, gas_used=9000000, timestamp=30)
user.add_transaction(volume=300, gas_used=7000000, timestamp=10)
user.add_transaction(volume=500, gas_used=8500000, timestamp=5)

trust_status, trust_score = user.analyze_trust()

print(f"Address: {user.address}")
print(f"Trust Status: {trust_status}")
print(f"Trust Score: {trust_score}")
print(f"Flags: {user.flags}")
print(f"Cooldown: {user.cooldown}")
