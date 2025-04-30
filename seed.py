from faker import Faker
from pymongo import MongoClient
import random

fake = Faker('pt_BR')

# Conexão com o MongoDB (ajuste se necessário)
client = MongoClient("mongodb://mongo:27017/")
db = client["eshop"]
collection = db["vendas"]

# Categorias e produtos fictícios
categorias = {
    "Eletrônicos": ["Smartphone", "Notebook", "Fone de Ouvido", "Monitor"],
    "Roupas": ["Camiseta", "Calça Jeans", "Tênis", "Jaqueta"],
    "Livros": ["Romance", "Ficção Científica", "Autoajuda", "Técnico"],
    "Alimentos": ["Arroz", "Feijão", "Chocolate", "Biscoito"],
    "Móveis": ["Cadeira", "Mesa", "Estante", "Sofá"]
}

# Geração de 1000 registros
for _ in range(1000):
    categoria = random.choice(list(categorias.keys()))
    produto = random.choice(categorias[categoria])

    venda = {
        "OrderID": fake.uuid4(),
        "ProductCategory": categoria,
        "ProductName": produto,
        "Price": round(random.uniform(10.0, 5000.0), 2),
        "Quantity": random.randint(1, 5),
        "Customer": {
            "Name": fake.name(),
            "Email": fake.email(),
            "CPF": fake.cpf()
        },
        "DeliveryAddress": {
            "Street": fake.street_name(),
            "City": fake.city(),
            "State": fake.estado_sigla(),
            "CEP": fake.postcode()
        },
        "PurchaseDate": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    }

    collection.insert_one(venda)

print("✅ 1000 vendas com dados completos inseridas com sucesso.")