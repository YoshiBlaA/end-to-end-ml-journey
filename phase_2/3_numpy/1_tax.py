"""
Price table with tax

You have this array:
    import numpy as np

    prices = np.array([[100, 250, 300],
                    [450, 125, 575],
                    [200, 350, 480]])  # 3 products, 3 regions
                    
Requirements:

    - Apply a different tax rate to each region using broadcasting: taxes = np.array([0.08, 0.15, 0.20])
    - Calculate the final price for each product in each region
    - Find the most expensive product per region using np.max(axis=0)
    - Find the cheapest product per region using np.min(axis=0)

Expected output:
    === Price Table with Tax ===
    Original prices:
    [[100 250 300]
    [450 125 575]
    [200 350 480]]

    Final prices (with tax):
    [[108.   287.5  360. ]
    [486.   143.75 690. ]
    [216.   402.5  576. ]]

    Most expensive per region: [486.   402.5  690. ]
    Cheapest per region:       [108.   143.75 360. ]
"""

if __name__ == "__main__":

    import numpy as np

    prices = np.array([[100, 250, 300],
                        [450, 125, 575],
                        [200, 350, 480]])
    
    taxes = np.array([0.08, 0.15, 0.20])
    
    final_prices = prices + (taxes * prices)
    
    most_expensive_per_region = np.max(final_prices, axis=0)
    cheapest_per_region = np.min(final_prices, axis=0)
    
    print("=== Price Table with Tax ===")
    print("Original prices:")
    print(prices, "\n")
    
    print("Final prices (with tax):")
    print(final_prices, "\n")
    
    print("Most expensive per region:", most_expensive_per_region)
    print("Cheapest per region:      ", cheapest_per_region)