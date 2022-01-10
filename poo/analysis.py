import pandas
import json

# 1 - Loading the JSON file, the first part is the QPI Query which needs to be discarded

# 1.1 Loading the file 
text_data = ""
with open("Amazon_vestes_rando_homme.json", "r") as f:
    text_data = f.read()

# 1.2 Find the response part in the file and convert to a json dictionary
key_response = "/* ********** Response ********** */"
key_start_idx = text_data.find(key_response)
truncacted_text = text_data[key_start_idx+len(key_response):]
json_data = json.loads(truncacted_text)

# 2 - Analyse the data, iterate over the values and put into a list that 
# can be converted to a CSV file
search_result = json_data["SearchResult"]
items = search_result["Items"]

# create an empty list which we will fill over time
list_data = []
for item in items:
    item_info = item["ItemInfo"]
    item_output = {"ASIN": item["ASIN"],
                 "WebsiteSalesRank": item["BrowseNodeInfo"]["WebsiteSalesRank"]["SalesRank"] if "WebsiteSalesRank" in item["BrowseNodeInfo"] else "NA",
                 "ManufacturerName": item_info["ByLineInfo"]["Manufacturer"]["DisplayValue"] if "Manufacturer" in item_info["ByLineInfo"] else "NA",
                 "ProductGroup": item_info["Classifications"]["ProductGroup"]["DisplayValue"] if "ProductGroup" in item_info["Classifications"] else "NA"}
    # look for the price (we will take the first price we find)
    offers = item["Offers"]["Listings"]
    if len(offers) == 0:
        price = "NA"
    else:
        price = offers[0]["Price"]["Amount"]
    item_output["Price"] = price
    list_data.append(item_output)

# output the result to a csv via the pandas library
df = pandas.DataFrame(list_data)

# save the output as a CSV file
df.to_csv("Result.csv")