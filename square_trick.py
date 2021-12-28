def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):
    predicted_price = (price_per_room * num_rooms) + base_price
    base_price += learning_rate * (price - predicted_price)
    price_per_room += learning_rate * num_rooms * (price - predicted_price)
    return price_per_room, base_price
