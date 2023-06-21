import dash
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State, ClientsideFunction
#import dash_html_components as html
from dash import html
from jupyter_dash import JupyterDash
import plotly.express as px
import plotly.graph_objects as go
import json
from skimage import data
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from IPython.core.display import display, HTML


def set_parameters(img):
    global image
    global height
    global width
    image = np.array(Image.open(img))
    height = image.shape[0]
    width = image.shape[1]
    print(f'Image loaded successfully at the set size: {width} x {height} (width x height)')
    
    
    



def create_mask_canvas():
    
    # create dash app
    app = JupyterDash() 
    
    # Set up image in plotly to draw on
    fig1 = go.Figure(px.imshow(image))
    fig1.update_layout(dragmode="drawclosedpath")
    config = {
        "modeBarButtonsToAdd": [
            #"drawline",
            #"drawopenpath",
            "drawclosedpath",
            #"drawcircle",
            #"drawrect",
            "eraseshape",
        ]
    }
    fig1.update_xaxes(visible=False) 
    fig1.update_yaxes(visible=False)
    
    fig1.update_layout(height = height, width = width, paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)')
    
    # Launch dash app 
    app.layout = html.Div(
        [
            html.H2(
                "Draw polygons on image"
            ),
            dcc.Graph(id="graph1", figure=fig1, config=config, style={'width':'100%','height':'100%'}),
            # dcc.Markdown("Characteristics of shapes"),
            html.Pre(id="shape_info"),
        ]
    )
    
    @app.callback(
        Output("shape_info", "children"),
        Input("graph1", "relayoutData"),
        prevent_initial_call=True,
    )
    def on_new_annotation(relayout_data):
        if "shapes" in relayout_data:
            global relayoutdata
            relayoutdata = json.dumps(relayout_data["shapes"], indent=2)
            return ''
        else:
            return dash.no_update
    
    app.run_server(mode='inline')
    
    display(HTML('<h2>Once happy with your mask location continue the notebook</h2>'))
    
    
def check_mask_drawn():
    
    
    display(HTML('<h2>Drawn mask on original image coloured</h2>'))
    
    
    json_acceptable_string = relayoutdata.replace("'", "\"")
    polygons = json.loads(json_acceptable_string)
    paths = []
    for polygon in polygons:
        paths.append(polygon['path'])

    # Show the mask on the original image and what the mask would be saved as
    fig2 = go.Figure(px.imshow(image))
    for path in paths:
        fig2.add_shape(type="path",path=path, fillcolor="Green",line_color="Green")    

    #fig2.update_xaxes(visible=False) 
    #fig2.update_yaxes(visible=False)
    #fig2.update_layout(height = height, width = width)
    fig2.show()

    
    display(HTML('<h2>Mask to be saved</h2>'))
    
    fig3 = go.Figure(px.imshow(image))
    fig3.add_shape(type="rect",
        x0 = 0,
        y0 = 0,
        x1 = image.shape[1],
        y1 = image.shape[0],
        fillcolor="Black",
        line_color="Black"
    )

    for path in paths:
        fig3.add_shape(type="path",path=path, fillcolor="White",line_color="White")    

    fig3['layout'].update(plot_bgcolor='Black') #title="Mask that would be saved"
    fig3.update_yaxes(autorange="reversed")
    fig3.update_xaxes(visible=True) 
    fig3.update_yaxes(visible=True)
    #fig3.update_layout(height = height, width = width)

    fig3.show()
    
def save_mask(directory):
    
    json_acceptable_string = relayoutdata.replace("'", "\"")
    polygons = json.loads(json_acceptable_string)
    paths = []
    for polygon in polygons:
        paths.append(polygon['path'])
    
    #fig4 = go.Figure(px.imshow(image))
    fig4 = px.imshow(image)
    fig4.add_shape(type="rect",
        x0 = 0,
        y0 = 0,
        x1 = width,
        y1=height,
        fillcolor="Black",
        line_color="Black",
        xref = "x",
        yref = "y",
    )

    for path in paths:
        fig4.add_shape(type="path",path=path, fillcolor="White",line_color="White")    

    fig4['layout'].update(plot_bgcolor='Black',template='plotly_dark',paper_bgcolor='Black') #title="Mask that would be saved"
    fig4.update_yaxes(autorange="reversed")
    fig4.update_xaxes(visible=True) 
    fig4.update_yaxes(visible=True)
    #fig4.update_layout(height = height, width = width, template='plotly_dark')
    fig4.update_xaxes(visible=False) 
    fig4.update_yaxes(visible=False)
    fig4.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    )
    fig4.write_image(directory, height=height, width=width)
    print(f'Successfully saved the mask in the directory: {directory}')
