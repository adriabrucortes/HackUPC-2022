
import gradio as gr
import pandas as pd
import datetime

#Per obtenir l'ID mes gran i sumarli 1 per obtindre un de nou 
#Es te per suposat que l'ID sempre comença per "RR" 
sales = pd.read_csv('/home/martini/Escritorio/Vscode/sales.csv')
max_id = sales['ID'].max()


#interficie on es ficaran les dades
textbox1 = gr.inputs.Textbox("text", label="PRODUCT ID", placeholder= "Product ID ...")
textbox2 = gr.inputs.Textbox("text", label="PRIZE", placeholder= "Price of the product (€) ...")
textbox3 = gr.inputs.Textbox("text", label="LOCATION", placeholder= "Location (number) ...")
textbox4 = gr.inputs.Textbox("text", label="DATE", placeholder= "Date (yyyy-mm-dd) ...")
textbox5 = gr.outputs.Label(type="auto", label="PREDICTION")
    
#donem per suposat que la data esta be
def stonks(Product_ID, Price, Location, Date): 
    price = float(Price)
    global max_id
    max_id_num = max_id.replace("R", "")
    max_id_num = int(max_id_num) + 1
    max_id_num = str(max_id_num).rjust(len(str(max_id_num))+2, "R")
    max_id = max_id_num
    product = pd.DataFrame({
        'SKU': [int(Product_ID)],
        'price': [price],
        'geoCluster': [Location],
        'date': [Date],
        'ID': [max_id]
    })

    database = pd.read_csv('/home/martini/Escritorio/Vscode/sku.csv')
   
    table=pd.merge(product, database, on='SKU')
    if len(table) == 0:
        return 'No es troba el producte'
    return f"Product ID: {Product_ID}\nPrice: {'%.2f'%price} €\nLocation: {Location}\nDate: {Date}\nID: {max_id}"
   

demo = gr.Interface(
    fn=stonks,
    inputs=[textbox1, textbox2, textbox3, textbox4],
    outputs=[textbox5],
)

demo.launch()
