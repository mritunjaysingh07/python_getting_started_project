import pprint
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    # Your code here
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        for key, val in delivery.items():
            if(val['batsman'] == 'RT Ponting'):
                count = count+1
    return count

deliveries_count(data)
