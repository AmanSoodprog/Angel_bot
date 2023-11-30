import redis

# Connect to the Redis server
redis_host = 'redis-10435.c321.us-east-1-2.ec2.cloud.redislabs.com'
redis_port = 10435
redis_db = 0
redis_password = 'wYYoKplw6iKoE9FIcewxehUIiiVmbNIb'  # Replace with your actual Redis password

redis_client = redis.StrictRedis(
    host=redis_host, port=redis_port, db=redis_db, password=redis_password
)

# Sample data for 10 stocks
stocks_data = {
    'stock1': {'position': 'long', 'buy_price': 100, 'target_price': 120, 'stop_loss': 90},
    'stock2': {'position': 'short', 'buy_price': 50, 'target_price': 40, 'stop_loss': 60},
    # Add data for other stocks similarly
}

# Store data in Redis
for stock_symbol, stock_params in stocks_data.items():
    redis_key = f'stock:{stock_symbol}'
    for param_key, param_value in stock_params.items():
        redis_client.hset(redis_key, param_key, param_value)

# Retrieve data from Redis
for stock_symbol in stocks_data.keys():
    redis_key = f'stock:{stock_symbol}'
    stored_data = redis_client.hgetall(redis_key)
    print(f"Stock {stock_symbol} data: {stored_data}")
