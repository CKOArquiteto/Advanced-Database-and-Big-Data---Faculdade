import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Configurações da biblioteca do MongoDB
mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["eshop"]
collection = db["vendas"]

# Funções Auxiliares
def carregar_dados_mongo():
    vendas = list(collection.find({}, {'_id': 0}))
    return pd.DataFrame(vendas)

def analisar_vendas():
    df = carregar_dados_mongo()
    if not df.empty:
        resultado = df.groupby("ProductCategory").size().reset_index(name='TotalVendas')
        return resultado
    else:
        return pd.DataFrame()

# Criação da Interface do Streamlit
st.title("E-Shop Brasil - Gestão de Vendas")

menu = st.sidebar.selectbox("Menu", 
                            ["Inserir Venda", 
                             "Visualizar Vendas", 
                             "Editar Venda", 
                             "Excluir Venda", 
                             "Análises Big Data"])

if menu == "Inserir Venda":
    st.header("Cadastrar Nova Venda")

    with st.form(key="form_venda"):
        order_id = st.text_input("Order ID")
        product_category = st.text_input("Categoria do Produto")
        product_name = st.text_input("Nome do Produto")
        price = st.number_input("Preço", min_value=0.0, step=0.01)
        quantity = st.number_input("Quantidade", min_value=1, step=1)

        submit_button = st.form_submit_button(label="Salvar Venda")

    if submit_button:
        venda = {
            "OrderID": order_id,
            "ProductCategory": product_category,
            "ProductName": product_name,
            "Price": price,
            "Quantity": quantity
        }
        collection.insert_one(venda)
        st.success("Venda cadastrada com sucesso!")

elif menu == "Visualizar Vendas":
    st.header("Vendas Registradas")
    df_vendas = carregar_dados_mongo()
    st.dataframe(df_vendas)

elif menu == "Editar Venda":
    st.header("Editar Venda Existente")
    df_vendas = carregar_dados_mongo()

    if not df_vendas.empty:
        selected_order_id = st.selectbox("Selecione o Order ID para editar", df_vendas["OrderID"].tolist())
        venda = collection.find_one({"OrderID": selected_order_id})

        with st.form(key="form_edit"):
            new_category = st.text_input("Nova Categoria", value=venda["ProductCategory"])
            new_name = st.text_input("Novo Nome do Produto", value=venda["ProductName"])
            new_price = st.number_input("Novo Preço", value=venda["Price"], step=0.01)
            new_quantity = st.number_input("Nova Quantidade", value=venda["Quantity"], step=1)

            update_button = st.form_submit_button(label="Atualizar Venda")

        if update_button:
            collection.update_one(
                {"OrderID": selected_order_id},
                {"$set": {
                    "ProductCategory": new_category,
                    "ProductName": new_name,
                    "Price": new_price,
                    "Quantity": new_quantity
                }}
            )
            st.success("Venda atualizada com sucesso!")

elif menu == "Excluir Venda":
    st.header("Excluir Venda Existente")
    df_vendas = carregar_dados_mongo()

    if not df_vendas.empty:
        selected_order_id = st.selectbox("Selecione o Order ID para excluir", df_vendas["OrderID"].tolist())
        if st.button("Excluir Venda"):
            collection.delete_one({"OrderID": selected_order_id})
            st.success("Venda excluída com sucesso!")

elif menu == "Análises Big Data": 
    st.header("Análises de Vendas")
    resultado = analisar_vendas()

    if not resultado.empty:
        st.subheader("Total de Vendas por Categoria")
        st.dataframe(resultado)
    else:
        st.warning("Não há dados suficientes para análise.")
