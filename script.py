import codecademylib3
import pandas as pd

inventory = pd.read_csv("inventory.csv")

staten_island = inventory.head(10)

# lam = lambda row: row['product_description'] if row['location'] == "Staten Island"

product_request = staten_island[['product_description', 'location']]
# print(product_request)

seed_request = inventory[(inventory['location'] == "Brooklyn") & (inventory['product_type'] == "seeds")]
# print(seed_request)

inventory["in_stock"] = inventory['quantity'].apply(lambda x: True if x > 0 else False)

# 7
inventory['total_value'] = inventory['quantity'] * inventory['price']

# 8
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)


# 9
inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)


print(inventory)