import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'mukul123')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'ecommerce')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'ecommerce_test')