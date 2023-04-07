#### Which code block will return the average price of each shoe_style based on the shoe_price column, in a DataFrame named inventory?

- [ ]`inventory.groupby("shoe_price").shoe_style.mean()`
- [x] `inventory.groupby("shoe_style").shoe_price.mean()`
- [ ] `inventory.groupby("shoe_price").shoe_price.mean()`
- [ ] `pd.mean(inventory["shoe_style"].groupby(shoe_price))`

#### Change a string into a timestamp in Python.

    ``` python
    import datetime
    import time
    
    time_string = "08/01/2011"

    time_stamp = time.mktime(datetime.datetime.strptime(time_string, "%d/%m/%Y").timetuple())

    print(time_stamp)
    ```


#### Which of these statements about gradient descent is true?

- [ ] The only way to optimize a set of parameters in a regression model is with a gradient descent algorithm.
- [ ] A gradient descent algorithm is needed to train a regression model.
- [x] Gradient descent is an optimization algorithm that can be used to improve a regression model.
- [ ] In regression problems, parameters can never be recalculated.

#### Which of the following code blocks creates a new Pandas DataFrame without errors? (Assume Pandas has been imported as pd).

- [ ] my_df = pd.read_data("my_file.csv")
- [ ] my_df = pd.DataFrame(1, 2, 3,'a', 'b', 'c')
- [ ] my_df = pd.Matrix( {"column1" : [1, 2, 3], "column2" : ['a', 'b', 'c'] } )
- [x] my_df = pd.DataFrame( {"column1" : [1, 2, 3], "column2" : ['a', 'b', 'c'] } )

#### Fill in the pyplot function names below.

        ``` python
        from matplotlib import pyplot as plt
        
        months = range(12)
        temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
        flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
        plt.subplot(1,2,1)
        plt.plot(temperature,months)
        plt.subplot(1,2,2)
        plt.plot(flights_to_hawaii,temperature,"o")
        plt.show()
        ```

#### Write a function called account_withdraw that takes two arguments, balance and amount. If amount is less or equal to than balance, the function should return the remaining balance, balance - amount. If amount is greater than balance, the function should return the exact string: "You have insufficient funds".

    ``` python
    def account_withdraw(balance, amount):
        if amount <= balance:
            return balance - amount
        else:
            return "You have insufficient funds"
    ```
