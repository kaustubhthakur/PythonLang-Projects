class LiquidityPool:
    def __init__(self,initial_reserve_a,initial_reserve_b):
        self.reserve_a = initial_reserve_a
        self.reserve_b = initial_reserve_b

    def add_liquidity(self,amount_a,amount_b):
        if amount_a<=0 or amount_b<=0:
            raise ValueError("Invalid Liwuidity amount")
        
        liquidity_minted = 0
        if self.reserve_a ==0 and self.reserve_b==0:
            liquidity_minted = min(amount_a,amount_b)
        else :
            liquidity_minted = min(amount_a * (self.reserve_b / self.reserve_a),
            amount_b * (self.reserve_a / self.reserve_b))

        
        self.reserve_a+=amount_a
        self.reserve_b+=amount_b

        return liquidity_minted

    def remove_liquidity(self,liquidity):
        if liquidity<=0:
            raise ValueError("invalid liwuidity amount")
        
        amount_a = liquidity * (self.reserve_a / (self.reserve_a + self.reserve_b))
        amount_b = liquidity * (self.reserve_b / (self.reserve_a + self.reserve_b))

        self.reserve_a -= amount_a
        self.reserve_b -= amount_b

        return amount_a, amount_b


    def trade(self,amount_in,reserve_in,reserve_out):
        if amount_in <= 0:
            raise ValueError("Invalid trade amount")

        amount_out = (amount_in * reserve_out) / (reserve_in + amount_in)
        return amount_out


initial_reserve_a=1000
initial_reserve_b=500


simulator = LiquidityPool(initial_reserve_a,initial_reserve_b)
liquidity_minted = simulator.add_liquidity(500,250)
print("Liwquidity minted",liquidity_minted)

amount_a, amount_b = simulator.remove_liquidity(liquidity_minted)
print("Amount A:", amount_a)
print("Amount B:", amount_b)

amount_in = 100
reserve_in = initial_reserve_a
reserve_out = initial_reserve_b
amount_out = simulator.trade(amount_in, reserve_in, reserve_out)
print("Amount Out:", amount_out)
